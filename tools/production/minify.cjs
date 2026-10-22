'use strict';
// Build-time transforms only; no decoder, minifier or source map ships to players.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const terser=require('terser'),CleanCSS=require('clean-css');
const options={ecma:2020,module:false,toplevel:false,
 compress:{defaults:false,dead_code:true,evaluate:true,booleans:true,conditionals:true,
 comparisons:true,unused:true,if_return:true,sequences:true,join_vars:true,drop_debugger:true,keep_fargs:true},
 mangle:{toplevel:false,properties:false},keep_classnames:true,
 format:{comments:false,ascii_only:true,semicolons:true},sourceMap:false};
async function main(){
 const task=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
 const versions={terser:require('terser/package.json').version,cleanCSS:require('clean-css/package.json').version};
 const settings=JSON.stringify({options,css:{level:1,rebase:false,inline:['none']},versions,transform:'production-v1-remove-review-links'});
 const results=[];
 for(const row of task.files){
  const original=fs.readFileSync(row.input,'utf8');let code=original;
  if(row.name==='js/care-ui.js'){
   const lines=code.split('\n'),found=lines.map((s,i)=>s.includes('function developerTools(){return `<details')?i:-1).filter(i=>i>=0);
   if(found.length!==1)throw Error('Review-tools source changed; audit production-only exclusion.');
   lines[found[0]]=" function developerTools(){return '';}";code=lines.join('\n');
  }
    // Preserve gameplay expressions exactly: local-name mangling is sufficient deterrence.
    // Literal-only art banks/transports retain their already verified compact output.
    const preserveExpressions=row.kind==='.js'&&!row.name.startsWith('assets/')&&!row.name.endsWith('-data.js');
    const effective=preserveExpressions?{...options,compress:false}:options;
    const key=crypto.createHash('sha256').update(settings).update(preserveExpressions?'runtime-preserve-expressions-v2':'').update(row.name).update(code).digest('hex'),cached=path.join(task.cache,key+row.kind);let output;
  if(fs.existsSync(cached))output=fs.readFileSync(cached,'utf8');
  else{
   if(row.kind==='.css'){
    const r=new CleanCSS({level:1,rebase:false,inline:['none'],sourceMap:false}).minify(code);
    if(r.errors.length)throw Error(row.name+': '+r.errors.join('; '));output=r.styles;
   }else{const r=await terser.minify(code,effective);if(!r.code||r.map)throw Error('Invalid protected output: '+row.name);output=r.code;}
   fs.writeFileSync(cached,output);
  }
  fs.writeFileSync(row.output,output);
  results.push({name:row.name,beforeBytes:Buffer.byteLength(original),afterBytes:Buffer.byteLength(output),cacheKey:key,outputSha256:crypto.createHash('sha256').update(output).digest('hex')});
 }
 fs.writeFileSync(task.result,JSON.stringify({versions,options,runtimeOptions:{...options,compress:false},results},null,2));
 console.log('Minified '+results.length+' files; public properties and registry identifiers preserved.');
}
main().catch(e=>{console.error(e.stack);process.exit(1)});
