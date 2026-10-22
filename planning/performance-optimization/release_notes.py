from pathlib import Path
import json
r=Path(__file__).resolve().parents[2];m=json.loads((r/'DIST/build-manifest.json').read_text())
text=f'''## Current release — v4.3.0, 2026-10-22

Performance optimization is implemented with60FPS default, optional30FPS, independent biological time, on-demand native sheets, bounded caches, cached scenery, covered/hidden suspension and five graphics controls. The current DIST has{m['sourceFiles']}source files ({m['sourceBytes']:,}bytes); its manifest records exact source hashes. GitHub Pages/local-save integration, both browsers'382-sheet checks, tutorial, equipment/offline, breeding and economy tests pass. The performance and five-minute-soak suites bring the final browser assertions to17,025with zero final failures. All2368original protected assets remain unchanged. The current Pages and portable source ZIPs are rebuilt and CRC/hash checked. See AQUARIUM_LIFE_PERFORMANCE_OPTIMIZATION_REPORT.md and tests/performance-evidence/release-validation.json for exact evidence and environmental limits. Physical GPU utilization and Netflix/audio synchronization were not measured. Native production remains382sheets/6112cells across110/113usable entries; the separate18-sheet shrimp artwork gap remains.

Earlier release sections below are historical and do not describe current counts or runtime.

'''
for name in ['GITHUB_PAGES_BUILD_REPORT.md','TEST_REPORT.md']:
 p=r/name;s=p.read_text(encoding='utf8');s=s.replace('\n\n','\n\n'+text,1);p.write_text(s,encoding='utf8')
