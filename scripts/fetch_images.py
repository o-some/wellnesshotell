from pathlib import Path
import urllib.request,re,html,json,concurrent.futures,subprocess
from PIL import Image
from io import BytesIO
root=Path.cwd();out=root/'public/assets';out.mkdir(parents=True,exist_ok=True)
photos=[('sauna','interior-of-a-wooden-sauna-with-a-heater-Z80uS2A-IFw'),('bath','wooden-sauna-room-with-a-bathtub-and-slippers-jlB0JgWlAns'),('massage','a-woman-getting-a-back-massage-at-a-spa--AakIaAPV0w'),('breakfast','breakfast-spread-with-waffles-eggs-and-juice-hrlvr2ZlUNk'),('tea','a-cup-of-herbal-tea-with-mint-leaves-WcVLb9HIMrk'),('forest','forest-pathway-GraajutbJHE'),('lake','a-floating-sauna-sits-in-a-stunning-mountain-lake-iffjBg4Rjk8'),('room','a-well-lit-hotel-room-with-seating-and-a-desk-xQbmc2FnK3Y'),('room-sea','elegant-hotel-room-with-a-view-of-the-sea-3gdMevwmb1U'),('room-studio','a-hotel-room-with-a-bed-desk-chairs-and-a-television-1EJXSLUfqU0')]
def get(x):
 name,slug=x;page='https://unsplash.com/photos/'+slug
 s=subprocess.check_output(['curl','-L','--silent','--fail',page],text=True);m=re.search(r'<meta property="og:image" content="([^"]+)',s);assert m,name
 url=html.unescape(m[1]).split('?')[0]+'?auto=format&fit=max&w=1800&q=85'
 data=subprocess.check_output(['curl','-L','--silent','--fail',url]);im=Image.open(BytesIO(data)).convert('RGB');im.thumbnail((1800,1800));im.save(out/(name+'.webp'),'WEBP',quality=86)
 for w in [640,1000]:
  small=im.copy();small.thumbnail((w,w));small.save(out/(name+f'-{w}.webp'),'WEBP',quality=82)
 return {'id':name,'file':name+'.webp','source_page':page,'source_image':url,'license':'https://unsplash.com/license','dimensions':im.size,'role':'illustrative concept imagery, not actual hotel','bytes':(out/(name+'.webp')).stat().st_size}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 results=[]
 for name,slug in photos:
  try:
   item=get((name,slug));results.append(item);print(name,'OK',flush=True)
  except Exception as e:print(name,str(e),flush=True)
(root/'docs/image-sources.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
