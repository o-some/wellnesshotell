import subprocess,json
from pathlib import Path
r=Path.cwd();out=r/'docs/qa/refinement';cli='/Users/eleftheriossamouladas/CAF-Workspace/premium-mac-20260919/browser-tools/node_modules/.bin/agent-browser'
def run(*a):
 p=subprocess.run([cli,'--session','wellness-refine',*a],capture_output=True,text=True);assert p.returncode==0,p.stderr;return p.stdout.strip()
def ev(js):
 s=run('eval',js)
 for i in range(3):
  try:s=json.loads(s)
  except:break
  if not isinstance(s,str):break
 return s
run('open','http://localhost:4173/');run('set','media','light','reduced-motion');report={'widths':[]}
for w in [360,390,768,1024,1280,1440,1920,2560]:
 run('set','viewport',str(w),'900');report['widths'].append(ev('JSON.stringify({width:innerWidth,scrollWidth:document.documentElement.scrollWidth})'))
for w,h,name in [(1366,768,'laptop'),(1440,1000,'desktop'),(390,844,'mobile')]:
 run('set','viewport',str(w),str(h));run('open','http://localhost:4173/');ev("document.querySelectorAll('img').forEach(i=>i.loading='eager')");run('wait','--load','networkidle');ev("window.scrollTo({top:document.querySelector('#genuss').offsetTop-82,behavior:'instant'})");run('wait','200');run('screenshot',str(out/(name+'-genuss.png')));run('screenshot',str(out/(name+'-full.png')),'--full')
report['images']=ev("JSON.stringify([...document.images].map(i=>({src:i.getAttribute('src'),loaded:i.complete&&i.naturalWidth>0})))")
report['reduced']=ev("JSON.stringify({image:getComputedStyle(document.querySelector('.food-main img')).transform,light:getComputedStyle(document.querySelector('.food'),'::before').animationName})")
run('set','viewport','1440','1000');run('set','media','light');run('open','http://localhost:4173/');ev("window.scrollTo({top:document.querySelector('#genuss').offsetTop,behavior:'instant'})");run('wait','350');report['active_effects']=ev("JSON.stringify({inView:document.querySelector('.food').classList.contains('in-view'),light:getComputedStyle(document.querySelector('.food'),'::before').animationName,lightState:getComputedStyle(document.querySelector('.food'),'::before').animationPlayState,depth:getComputedStyle(document.querySelector('.food-main img')).transform,progress:getComputedStyle(document.querySelector('.reading-progress')).transform})")
run('click','#tab-ruhe');report['room_switch']=ev("document.querySelector('#room-title').textContent");run('click','#tab-licht');run('click','#tab-see');report['rapid_switch']=ev("document.querySelector('#room-title').textContent");run('click','.motion-toggle');report['paused']=ev("JSON.stringify({light:getComputedStyle(document.querySelector('.food'),'::before').animationName,depth:getComputedStyle(document.querySelector('.food-main img')).transform})")
run('click','.planner-submit');report['planner']=run('is','visible','#plan-result');report['errors']=run('errors');(out/'report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False));print(json.dumps(report,indent=2,ensure_ascii=False))
(out/'a11y.json').write_text(run('a11y','--json'))
