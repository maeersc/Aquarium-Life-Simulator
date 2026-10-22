import base64
import json
import time

def run(client,root,name):
    client.navigate(root/'tests/sprite-audit.html')
    for _ in range(100):
        if client.evaluate('window.SPRITE_AUDIT?.ready'):break
        time.sleep(.05)
    report=client.evaluate('SPRITE_AUDIT')
    (root/'tests'/f'{name}-eye-after.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    client.call('Emulation.setDeviceMetricsOverride',{'width':1280,'height':900,'deviceScaleFactor':1,'mobile':False})
    shot=client.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
    (root/'assets/previews'/f'{name}-eye-after.png').write_bytes(base64.b64decode(shot['data']))
    print(json.dumps(report['samples']),flush=True)
    return 0
