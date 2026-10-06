from pathlib import Path
import re
p=Path('public/index.html');s=p.read_text()
s=s.replace('<span class="small-label">Ihre Zeit bei STILL</span>','').replace('<span class="small-label">Ihr persönlicher Reiseentwurf</span>','')
for label in ['Kurz raus','Gemeinsam sein','Ganz bei sich']:s=s.replace('<span>'+label+'</span>','')
paths={'↗':'M5 19 19 5M5 5h14v14','→':'M4 12h16m-6-6 6 6-6 6','←':'M20 12H4m6-6-6 6 6 6','↓':'M12 4v16m-6-6 6 6 6-6'}
for glyph,path in paths.items():
 svg=f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="{path}"/></svg>'
 s=s.replace(glyph,svg)
p.write_text(s)
p=Path('public/styles.css');s=p.read_text();s+='''\n.icon{width:22px;height:22px;flex-shrink:0;vertical-align:middle}.gallery-controls .icon{width:20px;height:20px}.closing a>span .icon{width:65px;height:65px}.arrangement-list>button{grid-template-columns:1.4fr 1.3fr 60px}.quick-plan>div{display:block}.quick-plan p{margin:0}.hero-foot .icon{width:18px;height:18px}.footer-links .icon{width:14px;height:14px}\n@media(max-width:780px){.arrangement-list>button{grid-template-columns:1fr 50px}.round-arrow{grid-row:1/3}.quick-plan>div{text-align:center}.closing a>span .icon{width:42px;height:42px}}\n''';p.write_text(s)
