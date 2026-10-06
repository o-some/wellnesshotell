import subprocess,json
from pathlib import Path
cli='/Users/eleftheriossamouladas/CAF-Workspace/premium-mac-20260919/browser-tools/node_modules/.bin/agent-browser'
out=Path('docs/cinematic-expansion').resolve()
def run(*a):
 p=subprocess.run([cli,'--session','wellness-cinema',*a],capture_output=True,text=True);assert p.returncode==0,p.stderr;return p.stdout.strip()
def ev(js):
 s=run('eval',js)
 for _ in range(3):
  try:s=json.loads(s)
  except:break
  if not isinstance(s,str):break
 return s
run('open','http://localhost:4173/');run('wait','--load','networkidle');(out/'interactive.txt').write_text(run('snapshot','-i'))
report={'widths':[]}
run('set','media','light','reduced-motion')
ev("document.querySelectorAll('img').forEach(i=>i.loading='eager')");run('wait','--load','networkidle')
for w in [360,390,768,1024,1280,1440,1920,2560]:
 run('set','viewport',str(w),'900');report['widths'].append(ev('JSON.stringify({width:innerWidth,scrollWidth:document.documentElement.scrollWidth})'))
for w,h,name in [(1440,1000,'desktop'),(390,844,'mobile')]:
 run('set','viewport',str(w),str(h));ev('window.scrollTo({top:0,behavior:"instant"})');run('screenshot',str(out/(name+'-hero.png')))
 for selector,label in [('.breathing-scene','dawn'),('.rituals','spa'),('.evening','dusk')]:
  ev(f"window.scrollTo({{top:document.querySelector('{selector}').offsetTop-80,behavior:'instant'}})");run('wait','150');run('screenshot',str(out/(name+'-'+label+'.png')))
 run('screenshot',str(out/(name+'-full.png')),'--full')
report['images']=ev("JSON.stringify([...document.images].map(i=>({src:i.getAttribute('src'),loaded:i.complete&&i.naturalWidth>0})))")
report['reduced']=ev("JSON.stringify({frame:getComputedStyle(document.querySelector('.breathing-frame')).clipPath,depth:getComputedStyle(document.querySelector('.breathing-frame img')).transform,evening:getComputedStyle(document.querySelector('.evening>img')).transform})")
run('set','viewport','1440','1000');run('set','media','light');run('open','http://localhost:4173/');run('wait','--load','networkidle')
ev("window.scrollTo({top:document.querySelector('.breathing-scene').offsetTop+360,behavior:'instant'})");run('wait','200');report['active']=ev("JSON.stringify({frame:getComputedStyle(document.querySelector('.breathing-frame')).clipPath,depth:getComputedStyle(document.querySelector('.breathing-frame img')).transform})")
run('click','.motion-toggle');report['paused']=ev("JSON.stringify({frame:getComputedStyle(document.querySelector('.breathing-frame')).clipPath,depth:getComputedStyle(document.querySelector('.breathing-frame img')).transform})")
run('click','#tab-ruhe');report['room']=ev("document.querySelector('#room-title').textContent")
run('click','#select-room');report['roomInPlanner']=ev("document.querySelector('#room-select').value")
run('click','.planner-submit');report['planner']=run('is','visible','#plan-result')
run('set','viewport','390','844');run('click','.menu-toggle');report['menuOpen']=run('is','visible','#navigation');run('press','Escape');report['menuClosed']=ev("document.querySelector('.menu-toggle').getAttribute('aria-expanded')==='false'")
report['errors']=run('errors');(out/'report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False));print(json.dumps(report,ensure_ascii=False))
(out/'a11y.json').write_text(run('a11y','--json'))
assert all(x['width']==x['scrollWidth'] for x in report['widths'])
assert all(x['loaded'] for x in report['images'])
assert report['reduced']['depth']=='none' and report['paused']['depth']=='none'
assert report['roomInPlanner']=='Ruhe Studio' and report['planner']=='true'
assert not report['errors']
