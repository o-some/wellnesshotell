from pathlib import Path
import json,re,subprocess,shutil
from PIL import Image,ImageDraw
root=Path.cwd();out=root/'public/assets';generated=Path('/Users/eleftheriossamouladas/.codex/generated_images/01a10ffc-7e0e-79c0-a433-6e6fc0bb2603')
files={'room':'exec-dc8ac199-17bc-4992-9be4-fd9ae3add97b.png','room-sea':'exec-176abfc0-5f4a-4aeb-aff9-5a55af1dd24e.png','hero':'exec-35d4866f-3471-46df-8944-e662b6f307c9.png','suite':'exec-9c03e265-118a-46d7-a7bd-8e3911ad8711.png','pool':'exec-2254b2c0-c3e8-418b-aef9-e3f8867dd0ec.png','lounge':'exec-1ed2c900-abbf-47a4-aaf6-16c18526e9fd.png','dinner':'exec-a922ebad-55ce-4e4c-a792-b509b5d13089.png'}
originals=root.parent.parent/'[User Input]'/'generated-originals';originals.mkdir(exist_ok=True)
for name,file in files.items():
 shutil.copy2(generated/file,originals/(name+'.png'));im=Image.open(generated/file).convert('RGB');im.save(out/(name+'.webp'),'WEBP',quality=88)
 for w in [640,1000]:
  small=im.copy();small.thumbnail((w,w));small.save(out/(name+f'-{w}.webp'),'WEBP',quality=83)
css=Path('/tmp/wellness-fonts.css').read_text();blocks=re.findall(r'/\* latin \*/\s*(@font-face\s*\{.*?\})',css,re.S)
for family,style,name in [('Cormorant Garamond','normal','display'),('Cormorant Garamond','italic','display-italic'),('Manrope','normal','body')]:
 block=next(b for b in blocks if family in b and 'font-style: '+style in b);url=re.search(r'url\(([^)]+)\)',block)[1];subprocess.run(['curl','--fail','-sL',url,'-o',str(out/(name+'.woff2'))],check=True)
s=(root/'public/styles.css').read_text();s="@font-face{font-family:Still Serif;src:url('assets/display-italic.woff2') format('woff2');font-style:italic;font-weight:400;font-display:swap}\n"+s;(root/'public/styles.css').write_text(s)
for name,folder in [('cormorantgaramond','CormorantGaramond'),('manrope','Manrope')]:
 subprocess.run(['curl','--fail','-sL',f'https://raw.githubusercontent.com/google/fonts/main/ofl/{name}/OFL.txt','-o',str(out/(folder+'-OFL.txt'))],check=True)
print('7 generated image concepts and local fonts prepared')
