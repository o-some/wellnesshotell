import subprocess,json
from pathlib import Path
cli='/Users/eleftheriossamouladas/CAF-Workspace/premium-mac-20260919/browser-tools/node_modules/.bin/agent-browser'
out=Path('docs/cinematic-expansion').resolve()
def run(*a):
 p=subprocess.run([cli,'--session','wellness-cinema-live',*a],capture_output=True,text=True);assert p.returncode==0,p.stderr;return p.stdout.strip()
def ev(js):
 s=run('eval',js)
 for _ in range(3):
  try:s=json.loads(s)
  except:break
  if not isinstance(s,str):break
 return s
run('open','https://o-some.github.io/wellnesshotell/?v=still-cinema-3');run('set','viewport','1440','1000');run('wait','--load','networkidle');(out/'live-interactive.txt').write_text(run('snapshot','-i'))
ev("document.querySelectorAll('img').forEach(i=>i.loading='eager')");run('wait','--load','networkidle')
report={'images':ev("JSON.stringify([...document.images].map(i=>({src:i.getAttribute('src'),loaded:i.complete&&i.naturalWidth>0})))")}
ev("window.scrollTo({top:document.querySelector('.breathing-scene').offsetTop+360,behavior:'instant'})");run('wait','200');report['active']=ev("JSON.stringify({frame:getComputedStyle(document.querySelector('.breathing-frame')).clipPath,overflow:document.documentElement.scrollWidth>innerWidth})")
run('screenshot',str(out/'live-dawn.png'))
run('click','#tab-licht');run('click','#select-room');run('wait','1000');report['room']=ev("document.querySelector('#room-select').value");run('snapshot','-i');run('click','.planner-submit');run('wait','1000');report['planner']=run('is','visible','#plan-result');report['errors']=run('errors')
(out/'live-browser.json').write_text(json.dumps(report,indent=2,ensure_ascii=False));print(json.dumps(report,ensure_ascii=False))
assert all(i['loaded'] for i in report['images']) and not report['active']['overflow']
assert report['room']=='Licht Refugium' and report['planner']=='true' and not report['errors']
run('close')
