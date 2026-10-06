const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const reduced=matchMedia('(prefers-reduced-motion: reduce)');let paused=reduced.matches;
const header=$('#header'),menu=$('.menu-toggle'),nav=$('#navigation');
function closeMenu(){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Menü öffnen')}
menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';nav.classList.toggle('open',open);menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Menü schließen':'Menü öffnen')});$$('a',nav).forEach(a=>a.addEventListener('click',closeMenu));document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){closeMenu();menu.focus()}});matchMedia('(min-width:781px)').addEventListener('change',closeMenu);
const motion=$('.motion-toggle');function setMotion(){document.documentElement.classList.toggle('no-motion',paused);motion.setAttribute('aria-pressed',String(paused));motion.textContent=paused?'Bewegung fortsetzen':'Bewegung pausieren';motion.setAttribute('aria-label',motion.textContent);if(paused)document.getAnimations().forEach(a=>{if(a.effect?.target?.id==='room-image')a.cancel()})}motion.addEventListener('click',()=>{paused=!paused;setMotion()});reduced.addEventListener('change',e=>{paused=e.matches;setMotion()});setMotion();
let ticking=false;
const parallax=$$('[data-parallax]'),breathing=$('.breathing-scene'),ritualFrames=$$('.ritual .image-frame');
function onScroll(){
 header.classList.toggle('scrolled',scrollY>90);
 document.documentElement.style.setProperty('--reading-progress',String(scrollY/Math.max(1,document.documentElement.scrollHeight-innerHeight)));
 const dining=$('#genuss');
 if(dining){const d=dining.getBoundingClientRect();const shift=paused||innerWidth<=780?0:Math.max(-18,Math.min(18,(innerHeight/2-d.top-d.height/2)*.045));dining.style.setProperty('--dining-shift',shift+'px')}
 if(!paused){
  const mobileFactor=innerWidth<=780 ? .35 : 1;
  for(const el of parallax){
   const r=el.parentElement.getBoundingClientRect();
   if(r.bottom>0&&r.top<innerHeight){
    const distance=(innerHeight/2-r.top-r.height/2)*Number(el.dataset.parallax)*mobileFactor;
    el.style.transform=`translate3d(0,${Math.max(-r.height*.13,Math.min(r.height*.13,distance))}px,0)`;
   }
  }
 }
 updateCinematic();ticking=false;
}
addEventListener('scroll',()=>{if(!ticking){requestAnimationFrame(onScroll);ticking=true}},{passive:true});onScroll();
if('IntersectionObserver'in window){const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.remove('pending');observer.unobserve(entry.target)}})},{threshold:.12});$$('.reveal').forEach(el=>{if(el.getBoundingClientRect().top>innerHeight)el.classList.add('pending');observer.observe(el)})}
let toastTimer;function toast(text){$('#toast').textContent=text;$('#toast').classList.add('visible');clearTimeout(toastTimer);toastTimer=setTimeout(()=>$('#toast').classList.remove('visible'),3200)}
const rooms={see:{name:'See Suite',image:'suite',alt:'Suite mit hellem Leinenbett und weitem Blick auf den See',text:'Aufwachen mit Weitblick. Barfuß zum Fenster. Und erst einmal nichts vorhaben. Unsere großzügige Wohnidee verbindet sanfte Naturtöne mit der Ruhe des Wassers.',features:['Weite & Wasserblick','Warmes Holz & weiches Leinen','Raum für gemeinsame Zeit']},ruhe:{name:'Ruhe Studio',image:'room-studio',alt:'Ruhiges Studio mit gemütlichem Bett und Sitzbereich',text:'Ein Lieblingsplatz nur für Sie. Zurückhaltende Farben, ein gutes Buch und das Gefühl, angekommen zu sein. Ein kompakter Rückzugsort für eine bewusste Pause.',features:['Gemütlicher Wohn- und Schlafbereich','Ein Platz zum Lesen','Die kleine Auszeit für sich']},licht:{name:'Licht Refugium',image:'room-sea',alt:'Lichtes Zimmer mit Blick auf das Wasser',text:'Den Vorhang öffnen und den Tag hereinlassen. Ein lichtes Zimmerkonzept, in dem der Blick nach draußen gehört und der Morgen gerne etwas länger dauern darf.',features:['Licht & offener Ausblick','Sanfte Farben und klare Linien','Zeit für einen langsamen Morgen']}};let selectedRoom='see';
const tabs=$$('[role=tab]');function activateRoom(key,focus=false){selectedRoom=key;const room=rooms[key];tabs.forEach(t=>{const active=t.dataset.room===key;t.setAttribute('aria-selected',String(active));t.tabIndex=active?0:-1;if(active&&focus)t.focus()});$('#room-panel').setAttribute('aria-labelledby','tab-'+key);$('#room-title').textContent=room.name;$('#room-copy').textContent=room.text;$('#room-image').src='assets/'+room.image+'.webp';$('#room-image').alt=room.alt;$('#room-features').replaceChildren(...room.features.map(text=>{const li=document.createElement('li');li.textContent=text;return li}));$('.room-counter').textContent=`0${Object.keys(rooms).indexOf(key)+1} / 03`;const img=$('#room-image');img.getAnimations().forEach(a=>a.cancel());if(!paused&&img.animate)img.animate([{opacity:.35,transform:'scale(1.035)'},{opacity:1,transform:'scale(1)'}],{duration:700,easing:'cubic-bezier(.16,1,.3,1)'})}
tabs.forEach((t,i)=>{t.addEventListener('click',()=>activateRoom(t.dataset.room));t.addEventListener('keydown',e=>{let next;if(e.key==='ArrowRight')next=(i+1)%tabs.length;if(e.key==='ArrowLeft')next=(i+tabs.length-1)%tabs.length;if(e.key==='Home')next=0;if(e.key==='End')next=tabs.length-1;if(next!==undefined){e.preventDefault();activateRoom(tabs[next].dataset.room,true)}})});
function goPlan(){location.hash='auszeit'}$('#select-room').addEventListener('click',()=>{$('#room-select').value=rooms[selectedRoom].name;toast(rooms[selectedRoom].name+' für Ihren Entwurf vorgemerkt.');goPlan()});$$('.choose-interest').forEach(b=>b.addEventListener('click',()=>{const input=$$('input[name=interest]').find(i=>i.value===b.dataset.interest);if(input)input.checked=true;toast(b.dataset.interest+' für Ihren Entwurf vorgemerkt.');goPlan()}));
const arrival=$('#arrival'),departure=$('#departure');function dateString(date){return `${date.getFullYear()}-${String(date.getMonth()+1).padStart(2,'0')}-${String(date.getDate()).padStart(2,'0')}`}function plusDays(value,days){const d=new Date(value+'T12:00:00');d.setDate(d.getDate()+days);return dateString(d)}const today=dateString(new Date());arrival.min=today;arrival.value=plusDays(today,14);departure.value=plusDays(arrival.value,2);departure.min=plusDays(arrival.value,1);
arrival.addEventListener('change',()=>{if(!arrival.value)return;departure.min=plusDays(arrival.value,1);if(departure.value<=arrival.value)departure.value=plusDays(arrival.value,2)});
let selectedPackage='Individuelle Auszeit';$$('[data-package]').forEach(b=>b.addEventListener('click',()=>{selectedPackage=b.dataset.package;if(!arrival.value||arrival.value<today)arrival.value=plusDays(today,14);departure.value=plusDays(arrival.value,Number(b.dataset.nights));toast(selectedPackage+' ist im Reiseplaner vorbereitet.');goPlan()}));
let planText='';$('#planner-form').addEventListener('submit',e=>{e.preventDefault();const error=$('#date-error');arrival.removeAttribute('aria-invalid');departure.removeAttribute('aria-invalid');let invalid=null;if(!arrival.value||arrival.value<today){error.textContent='Bitte wählen Sie eine Anreise ab heute.';invalid=arrival}else if(!departure.value||departure.value<=arrival.value){error.textContent='Bitte wählen Sie eine Abreise nach Ihrer Anreise.';invalid=departure}if(invalid){invalid.setAttribute('aria-invalid','true');invalid.focus();return}error.textContent='';const nights=Math.round((Date.parse(departure.value)-Date.parse(arrival.value))/86400000),fmt=v=>new Intl.DateTimeFormat('de-DE',{day:'numeric',month:'long',year:'numeric'}).format(new Date(v+'T12:00:00')),interests=$$('input[name=interest]:checked').map(i=>i.value);planText=`STILL · Ihr persönlicher Reiseentwurf\n\n${selectedPackage}\n${fmt(arrival.value)} – ${fmt(departure.value)}\n${nights} ${nights===1?'Nacht':'Nächte'} · ${$('#guests').value} ${$('#guests').value==='1'?'Gast':'Gäste'}\nZimmerwunsch: ${$('#room-select').value}\nIhre Wünsche: ${interests.length?interests.join(', '):'Einfach zur Ruhe kommen'}\n\nHotelkonzept — keine Buchung, keine Reservierung und keine geprüfte Verfügbarkeit. Es wurden keine Daten versendet.\nhttps://o-some.github.io/wellnesshotell/`;$('#plan-summary').textContent=planText.split('\n').slice(2,7).join('\n');$('#plan-result').hidden=false;$('#plan-result').focus({preventScroll:true});$('#plan-result').scrollIntoView({behavior:paused?'instant':'smooth',block:'center'})});
$('#download-plan').addEventListener('click',()=>{const url=URL.createObjectURL(new Blob([planText],{type:'text/plain;charset=utf-8'})),a=document.createElement('a');a.href=url;a.download='STILL-Reiseentwurf.txt';document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);toast('Ihr Reiseentwurf wurde zum Speichern bereitgestellt.')});$('#edit-plan').addEventListener('click',()=>{arrival.focus();arrival.scrollIntoView({behavior:paused?'instant':'smooth',block:'center'})});
const gallery=$('#gallery'),prev=$('#gallery-prev'),next=$('#gallery-next');function galleryState(){const figures=$$('figure',gallery),step=figures[1].offsetLeft-figures[0].offsetLeft,index=Math.round(gallery.scrollLeft/step);$('#gallery-status').textContent=`${Math.min(index+1,5)} / 5`;prev.disabled=gallery.scrollLeft<8;next.disabled=gallery.scrollLeft>=gallery.scrollWidth-gallery.clientWidth-8}function slide(dir){const figures=$$('figure',gallery);gallery.scrollBy({left:dir*(figures[1].offsetLeft-figures[0].offsetLeft),behavior:paused?'instant':'smooth'})}prev.addEventListener('click',()=>slide(-1));next.addEventListener('click',()=>slide(1));gallery.addEventListener('scroll',galleryState,{passive:true});addEventListener('resize',galleryState);gallery.addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key==='ArrowLeft'){e.preventDefault();slide(e.key==='ArrowRight'?1:-1)}});galleryState();

// Only visible scenes spend animation time; hidden tabs stop all ambient loops.
if('IntersectionObserver' in window){const sceneObserver=new IntersectionObserver(entries=>{for(const entry of entries)entry.target.classList.toggle('in-view',entry.isIntersecting)},{threshold:0});$$('.light-scene,.hero').forEach(el=>sceneObserver.observe(el))}
document.addEventListener('visibilitychange',()=>document.documentElement.classList.toggle('page-hidden',document.hidden));
addEventListener('resize',()=>{if(innerWidth<=780)parallax.forEach(el=>el.style.removeProperty('transform'));onScroll()});

// One scroll clock drives the cinematic chapter and bounded editorial depth.
function updateCinematic(){
 const mobile=innerWidth<=780,still=paused;
 if(breathing){
  const r=breathing.getBoundingClientRect();
  if(r.bottom>0&&r.top<innerHeight){
   const progress=Math.max(0,Math.min(1,mobile?(innerHeight-r.top)/(innerHeight+r.height):-r.top/Math.max(1,r.height-innerHeight)));
   breathing.style.setProperty('--frame-inset',still?'0%':((mobile?2.2:4)*(1-progress))+'%');
   breathing.style.setProperty('--breathe-shift',still?'0px':(progress*(mobile?32:36)-(mobile?16:18))+'px');
   breathing.style.setProperty('--word-shift',still||mobile?'0px':(-progress*18)+'px');
  }
 }
 for(const el of ritualFrames){
  const r=el.getBoundingClientRect();
  if(r.bottom>0&&r.top<innerHeight){
   const shift=still||mobile?0:Math.max(-22,Math.min(22,(innerHeight/2-r.top-r.height/2)*.05));
   el.style.setProperty('--ritual-shift',shift+'px');
  }
 }
}
motion.addEventListener('click',onScroll);
reduced.addEventListener('change',onScroll);
