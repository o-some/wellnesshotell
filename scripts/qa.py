import subprocess,json
from pathlib import Path
root=Path.cwd();out=root/'docs/qa';cli='/Users/eleftheriossamouladas/CAF-Workspace/premium-mac-20260919/browser-tools/node_modules/.bin/agent-browser'
def run(*args):
 p=subprocess.run([cli,'--session','wellness',*args],capture_output=True,text=True);assert p.returncode==0,p.stderr;return p.stdout.strip()
def ev(s):
 raw=run('eval',s)
 try:return json.loads(raw)
 except:return raw
report={'engine':'agent-browser Chromium, desktop emulation (not real iOS)','widths':[]}
for w in [360,375,390,393,430,768,1280,1440,1920,2560]:
 run('set','viewport',str(w),'900');report['widths'].append(ev('JSON.stringify({width:innerWidth,height:innerHeight,client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth,overflow:document.documentElement.scrollWidth>innerWidth})'))
run('set','viewport','1440','1000');run('set','media','light','reduced-motion');run('reload');ev("document.querySelectorAll('img').forEach(i=>i.loading='eager')");run('wait','--load','networkidle');run('screenshot',str(out/'desktop-full.png'),'--full');run('screenshot',str(out/'desktop-hero.png'))
report['images']=ev("JSON.stringify([...document.images].map(i=>({src:i.getAttribute('src'),loaded:i.complete&&i.naturalWidth>0})))")
run('click','#tab-ruhe');report['room_tab']=ev("document.querySelector('#room-title').textContent")
run('press','ArrowRight');report['room_keyboard']=ev("document.querySelector('#room-title').textContent")
run('click','#select-room');report['room_selected']=ev("document.querySelector('#room-select').value")
ev("document.querySelector('#arrival').value='2026-11-10';document.querySelector('#arrival').dispatchEvent(new Event('change'));document.querySelector('#departure').value='2026-11-09'");run('click','.planner-submit');report['invalid_date']=ev("document.querySelector('#date-error').textContent")
ev("document.querySelector('#departure').value='2026-11-13'");run('check','input[value="Sauna & Wärme"]');run('click','.planner-submit');report['valid_plan']=ev("document.querySelector('#plan-summary').textContent");run('download','#download-plan',str(out/'downloaded-plan.txt'));report['download_exists']=(out/'downloaded-plan.txt').exists();run('screenshot',str(out/'planner-desktop.png'))
run('set','viewport','390','844');run('open','http://localhost:4173/');ev("document.querySelectorAll('img').forEach(i=>i.loading='eager')");run('wait','--load','networkidle');run('screenshot',str(out/'mobile-hero.png'));run('screenshot',str(out/'mobile-full.png'),'--full')
run('click','.menu-toggle');report['mobile_menu']=ev("document.querySelector('.menu-toggle').getAttribute('aria-expanded')");run('screenshot',str(out/'mobile-menu.png'));run('press','Escape');report['escape_closes_menu']=ev("document.querySelector('.menu-toggle').getAttribute('aria-expanded')")
run('scrollintoview','#gallery');before=ev("document.querySelector('#gallery').scrollLeft");run('click','#gallery-next');report['gallery_next']=ev("document.querySelector('#gallery').scrollLeft");run('scroll','down','500');report['vertical_scroll']=ev('scrollY');run('click','#gallery-prev');report['gallery_previous']=ev("document.querySelector('#gallery').scrollLeft")
report['reduced_motion']=ev("JSON.stringify({media:matchMedia('(prefers-reduced-motion: reduce)').matches,animation:getComputedStyle(document.querySelector('.hero-image')).animationName})")
report['errors']=run('errors');report['console']=run('console');
(out/'browser-report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False));print(json.dumps(report,indent=2,ensure_ascii=False))
print(run('a11y','--json'));(out/'a11y.json').write_text(run('a11y','--json'))
