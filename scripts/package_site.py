from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
import json,re,hashlib,shutil
root=Path.cwd(); assets=root/'public/assets';sources=[r for r in json.loads((root/'docs/image-sources.json').read_text()) if r['id'] not in ['room','room-sea']]
for name in ['hero','suite','pool','lounge','dinner','room','room-sea']:
 im=Image.open(assets/(name+'.webp'));sources.append({'id':name,'file':name+'.webp','source':'OpenAI native image generation','role':'fictional architecture/food concept','dimensions':im.size})
for row in sources:row['sha256']=hashlib.sha256((assets/row['file']).read_bytes()).hexdigest()
(root/'docs/image-manifest.json').write_text(json.dumps(sources,indent=2,ensure_ascii=False))
# Responsive candidates use their actual image widths; preserve generated originals privately.
s=(root/'public/index.html').read_text()
def responsive(m):
 tag=re.sub(r' srcset="[^"]*"| sizes="[^"]*"','',m[0]);name=re.search(r'src="assets/([^\"]+)\.webp"',tag)[1];im=Image.open(assets/(name+'.webp'));tag=re.sub(r'width="\d+" height="\d+"',f'width="{im.width}" height="{im.height}"',tag)
 if name=='hero' or 'id="room-image"' in tag:return tag
 variants=[(f'{name}-{w}.webp',Image.open(assets/f'{name}-{w}.webp').width) for w in (640,1000)];variants.append((name+'.webp',im.width));srcset=', '.join('assets/'+f+' '+str(w)+'w' for f,w in variants)
 return tag[:-1]+f' srcset="{srcset}" sizes="(max-width:780px) 100vw, 65vw">'
s=re.sub(r'<img[^>]+src="assets/[^\"]+\.webp"[^>]*>',responsive,s);(root/'public/index.html').write_text(s)
head='<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><link rel="stylesheet" href="styles.css"><link rel="icon" href="assets/favicon.svg"><title>{title} · STILL</title></head><body><main class="wrap legal"><a href="./">← Zurück zu STILL</a>'
legal='''<h1>Ein Konzept.<br><em>Kein Versprechen.</em></h1><p>STILL ist ein frei gestaltetes Wellnesshotel- und Webdesignkonzept für das Kundenprojekt Wellnesshotel. Es gibt keinen realen Hotelbetrieb, keine buchbaren Angebote und keinen hier dargestellten tatsächlichen Standort.</p><h2>Der Reiseplaner</h2><p>Alle Eingaben werden ausschließlich im aktuellen Browser-Tab verarbeitet. Der Download erzeugt eine Textdatei auf Ihrem Gerät. Es findet keine Reservierung, Anfrageübermittlung oder Verfügbarkeitsprüfung statt. Es werden keine Namen, E-Mail-Adressen oder Zahlungsdaten abgefragt.</p><h2>Datenschutz und Technik</h2><p>Diese Website setzt keine Analyse-, Marketing- oder Tracking-Cookies ein. Schriften und Bilder werden lokal mit der Seite ausgeliefert. Beim Abruf verarbeitet der Hostinganbieter GitHub technisch erforderliche Verbindungsdaten. Informationen dazu bietet die <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">Datenschutzerklärung von GitHub</a>.</p><h2>Bildwelt</h2><p>Die Bilder sind eigens erzeugte Konzeptmotive und lizenzierte Inspirationsfotos. Sie dokumentieren kein gemeinsames, bestehendes Hotel. <a href="bildnachweise.html">Zu den Bildnachweisen</a>.</p><h2>Projekt</h2><p>Designkonzept von Chelonaki. <a href="https://github.com/o-some/wellnesshotell">Projekt und Quellcode auf GitHub</a>. Vor einer Nutzung als echte Hotelwebsite müssen Betreiberangaben, reale Angebote, Hotelbilder, Datenschutzinformationen und Buchungssystem anhand des tatsächlichen Betriebs ergänzt werden.</p>'''
(root/'public/hinweise.html').write_text(head.format(title='Konzept & Datenschutz')+legal+'</main></body></html>')
credits='<h1>Unsere <em>Bildwelt.</em></h1><p>Alle Bilder dienen der Illustration des Hotelkonzepts. Architekturvisionen zeigen keinen tatsächlichen Hotelbetrieb.</p><h2>Eigens erzeugte Motive</h2><p>Hero, See Suite, Innenpool, Ruheraum, Lesezimmer, Licht Refugium und saisonales Gericht: für STILL mit OpenAI Image Generation erzeugt und als WebP optimiert.</p><h2>Inspirationsfotografie</h2><p>Die folgenden Aufnahmen sind unter der <a href="https://unsplash.com/license">Unsplash-Lizenz</a> veröffentlicht. Die Originalseiten enthalten die jeweiligen Fotografenangaben.</p><ul>'
for row in sources:
 if 'source_page' in row:credits+=f'<li><a href="{row["source_page"]}">{row["id"]} — Originalaufnahme auf Unsplash</a></li>'
credits+='</ul><h2>Schriften</h2><p>Cormorant Garamond und Manrope, lokal eingebunden unter der SIL Open Font License. Lizenzdateien: <a href="assets/CormorantGaramond-OFL.txt">Cormorant Garamond</a> und <a href="assets/Manrope-OFL.txt">Manrope</a>.</p>'
(root/'public/bildnachweise.html').write_text(head.format(title='Bildnachweise')+credits+'</main></body></html>')
canvas=Image.new('RGB',(1250,3*240),'#f6f5f0');d=ImageDraw.Draw(canvas)
for i,row in enumerate(sources):
 im=Image.open(assets/row['file']);im=ImageOps.fit(im,(240,205));x=(i%5)*250;y=(i//5)*240;canvas.paste(im,(x,y));d.text((x+5,y+212),row['id'],fill='#24434b')
canvas.save(root/'docs/image-contact-sheet.jpg',quality=88)
logo=root.parent.parent/'[Logo]';shutil.copy2(assets/'favicon.svg',logo/'[Icons]'/'still-icon.svg')
(logo/'[Master]'/'still-wordmark.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="500" height="180" viewBox="0 0 500 180"><rect width="500" height="180" fill="#f6f5f0"/><text x="250" y="100" text-anchor="middle" font-family="Georgia,serif" font-size="80" letter-spacing="16" fill="#24434b">STILL</text><text x="250" y="138" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" letter-spacing="5" fill="#24434b">WELLNESSHOTEL</text></svg>')
print('packaged',len(sources),'distinct images')
