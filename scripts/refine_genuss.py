from pathlib import Path
r=Path.cwd();p=r/'public/index.html';s=p.read_text();s=s.replace('href="styles.css"','href="styles.css?v=still-light-2"').replace('src="app.js"','src="app.js?v=still-light-2"')
s=s.replace('<section class="food section"','<section class="food section light-scene"').replace('<div class="food-main reveal">','<div class="food-main reveal dining-depth">').replace('<figure class="breakfast reveal">','<figure class="breakfast reveal dining-detail">')
s=s.replace('assets/breakfast.webp','assets/breakfast-v2.webp').replace('assets/breakfast-640.webp','assets/breakfast-v2-640.webp').replace('assets/breakfast-1000.webp','assets/breakfast-v2-1000.webp')
s=s.replace('Liebevoll gedeckter Frühstückstisch mit Waffeln, Früchten und Eiern','Ruhiges Frühstück mit Croissant und Keramikgeschirr am See').replace('class="pool-scene parallax-scene"','class="pool-scene parallax-scene light-scene"')
s=s.replace('<header class="header" id="header">','<div class="reading-progress" aria-hidden="true"></div>\n<header class="header" id="header">')
p.write_text(s)
p=r/'public/styles.css';s=p.read_text();s+='''
/* STILL refinement: morning light joins the dining story into one composition. */
.food{position:relative;isolation:isolate;overflow:hidden;background:#ecebe4}
.food-layout{grid-template-areas:"main copy" "main breakfast";grid-template-columns:1.06fr 1fr;gap:32px 8%;align-items:start;position:relative;z-index:1}
.food-main{grid-area:main;height:100%;min-height:650px;overflow:hidden;box-shadow:0 24px 65px #314b4917}
.food-main img{transform:scale(1.07) translate3d(0,var(--dining-shift,0px),0);object-position:43% center}
.food-copy{grid-area:copy;padding-top:12px}
.breakfast{grid-area:breakfast;width:100%;margin:0;align-self:end}
.breakfast img{height:265px;object-position:center;box-shadow:0 18px 40px #314b4912}
.breakfast figcaption{padding-top:14px}
.food:before{content:"";position:absolute;z-index:0;inset:-40%;pointer-events:none;background:linear-gradient(112deg,transparent 32%,#fff8de88 46%,#fffdf622 50%,transparent 60%);transform:translateX(-12%);animation:morning-light 22s ease-in-out infinite alternate;animation-play-state:paused}
.light-scene.in-view:before,.light-scene.in-view:after{animation-play-state:running}
.pool-scene:after{content:"";position:absolute;inset:35% -10% -20%;pointer-events:none;background:repeating-radial-gradient(ellipse at 30% 40%,transparent 0 45px,#f1fbff1c 50px,transparent 58px 94px);mix-blend-mode:soft-light;opacity:.4;transform:rotate(-8deg) scale(1.2);animation:water-light 18s ease-in-out infinite alternate;animation-play-state:paused}
.pool-caption,.scene-tag{z-index:2}
.reading-progress{position:fixed;z-index:40;top:0;left:0;width:100%;height:2px;transform:scaleX(var(--reading-progress,0));transform-origin:left;background:#a5bfc3;pointer-events:none}
.button{position:relative;overflow:hidden;isolation:isolate}
.button:after{content:"";position:absolute;inset:-50% -80%;pointer-events:none;background:linear-gradient(110deg,transparent 42%,#ffffff24 50%,transparent 58%);transform:translateX(-45%);transition:transform 1.1s var(--ease)}
.button:hover:after,.button:focus-visible:after{transform:translateX(45%)}
.gallery figure img{transition:transform 1.2s var(--ease),box-shadow 1.2s var(--ease)}
.gallery figure:hover img{transform:translateY(-5px);box-shadow:0 20px 40px #1838421a}
.room-picture{background:#e0e8e5}
.page-hidden *, .page-hidden *:before,.page-hidden *:after{animation-play-state:paused!important}
.hero:not(.in-view) .hero-image,.hero:not(.in-view) .mist{animation-play-state:paused}
.no-motion .food-main img{transform:none!important}.no-motion *:before,.no-motion *:after{animation:none!important;transition:none!important}
@keyframes morning-light{from{transform:translateX(-12%) rotate(-3deg);opacity:.45}to{transform:translateX(14%) rotate(3deg);opacity:.85}}
@keyframes water-light{from{transform:translate3d(-1%,-2%,0) rotate(-8deg) scale(1.2);opacity:.22}to{transform:translate3d(3%,3%,0) rotate(-4deg) scale(1.25);opacity:.48}}
@media(max-width:1100px) and (min-width:781px){.food-layout{gap:26px 6%}.food-main{min-height:640px}.breakfast img{height:235px}}
@media(max-width:780px){.food-layout{grid-template-areas:"copy" "main" "breakfast";grid-template-columns:1fr;gap:30px}.food-main{height:380px;min-height:0}.food-copy{padding-top:0}.breakfast{width:86%;margin:0 0 0 auto}.breakfast img{height:230px}.food-main img{transform:none}.food:before{animation-duration:28s}.pool-scene:after{display:none}.gallery figure:hover img{transform:none}}
@media(prefers-reduced-motion:reduce){.food-main img{transform:none}.button:after{display:none}.reading-progress{transition:none}}
''';p.write_text(s)
p=r/'public/app.js';s=p.read_text();s=s.replace("motion.setAttribute('aria-label',motion.textContent)}", "motion.setAttribute('aria-label',motion.textContent);if(paused)document.getAnimations().forEach(a=>{if(a.effect?.target?.id==='room-image')a.cancel()})}")
s=s.replace("header.classList.toggle('scrolled',scrollY>90);", "header.classList.toggle('scrolled',scrollY>90);document.documentElement.style.setProperty('--reading-progress',String(scrollY/Math.max(1,document.documentElement.scrollHeight-innerHeight)));const dining=$('#genuss');if(dining){const d=dining.getBoundingClientRect();const shift=paused||innerWidth<=780?0:Math.max(-18,Math.min(18,(innerHeight/2-d.top-d.height/2)*.045));dining.style.setProperty('--dining-shift',shift+'px')}")
s=s.replace("$('.room-counter').textContent=`0${Object.keys(rooms).indexOf(key)+1} / 03`}", "$('.room-counter').textContent=`0${Object.keys(rooms).indexOf(key)+1} / 03`;const img=$('#room-image');img.getAnimations().forEach(a=>a.cancel());if(!paused&&img.animate)img.animate([{opacity:.35,transform:'scale(1.035)'},{opacity:1,transform:'scale(1)'}],{duration:700,easing:'cubic-bezier(.16,1,.3,1)'})}")
s+='''\n// Only visible scenes spend animation time; hidden tabs stop all ambient loops.
if('IntersectionObserver' in window){const sceneObserver=new IntersectionObserver(entries=>{for(const entry of entries)entry.target.classList.toggle('in-view',entry.isIntersecting)},{threshold:0});$$('.light-scene,.hero').forEach(el=>sceneObserver.observe(el))}
document.addEventListener('visibilitychange',()=>document.documentElement.classList.toggle('page-hidden',document.hidden));
addEventListener('resize',()=>{if(innerWidth<=780)parallax.forEach(el=>el.style.removeProperty('transform'));onScroll()});
''';p.write_text(s)
