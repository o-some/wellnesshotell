import subprocess,json
from pathlib import Path
cli='/Users/eleftheriossamouladas/CAF-Workspace/premium-mac-20260919/browser-tools/node_modules/.bin/agent-browser'
out=Path('docs/third-scene').resolve()
def run(*a):
 p=subprocess.run([cli,'--session','third-scene',*a],capture_output=True,text=True);assert p.returncode==0,p.stderr;return p.stdout.strip()
def ev(js):
 s=run('eval',js)
 for _ in range(3):
  try:s=json.loads(s)
  except:break
  if not isinstance(s,str):break
 return s
run('open','http://localhost:4173/');run('wait','--load','networkidle');run('snapshot','-i');run('set','media','light','reduced-motion')
ev("document.querySelectorAll('img').forEach(i=>i.loading='eager')");run('wait','--load','networkidle')
r={'widths':[],'sequence':ev("JSON.stringify([document.querySelector('#natur').id,document.querySelector('#natur').nextElementSibling.id,document.querySelector('#natur').nextElementSibling.nextElementSibling.id])")}
for w in [360,390,768,1024,1440,1920,2560]:
 run('set','viewport',str(w),'900');r['widths'].append(ev('JSON.stringify({width:innerWidth,scrollWidth:document.documentElement.scrollWidth})'))
for w,h,name in [(1440,1000,'desktop'),(390,844,'mobile')]:
 run('set','viewport',str(w),str(h))
 for offset,label in [(-80,'scene'),(-h+160,'transition')]:
  ev(f"window.scrollTo({{top:document.querySelector('#geborgen').offsetTop+({offset}),behavior:'instant'}})");run('wait','150');run('screenshot',str(out/(name+'-'+label+'.png')))
r['images']=ev("JSON.stringify([...document.images].map(i=>({src:i.getAttribute('src'),loaded:i.complete&&i.naturalWidth>0})))")
r['reduced']=ev("getComputedStyle(document.querySelector('#geborgen>img')).transform")
run('set','viewport','1440','1000');run('set','media','light');run('open','http://localhost:4173/');ev("window.scrollTo({top:document.querySelector('#geborgen').offsetTop-100,behavior:'instant'})");run('wait','200');r['active']=ev("getComputedStyle(document.querySelector('#geborgen>img')).transform")
run('click','.motion-toggle');r['paused']=ev("getComputedStyle(document.querySelector('#geborgen>img')).transform")
run('click','#geborgen .text-link');run('wait','500');r['link']=ev('location.hash');run('click','.planner-submit');r['planner']=run('is','visible','#plan-result');r['errors']=run('errors')
(out/'report.json').write_text(json.dumps(r,indent=2,ensure_ascii=False));print(json.dumps(r,ensure_ascii=False))
assert r['sequence']==['natur','abend','geborgen']
assert all(x['width']==x['scrollWidth'] for x in r['widths']) and all(i['loaded'] for i in r['images'])
assert r['paused']=='none' and r['reduced']=='none' and r['link']=='#auszeit' and r['planner']=='true' and not r['errors']
