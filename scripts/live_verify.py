from pathlib import Path
import subprocess,json,hashlib,concurrent.futures,datetime
r=Path.cwd();base='https://o-some.github.io/wellnesshotell/';files=['index.html','styles.css','app.js','hinweise.html','bildnachweise.html']+['assets/'+x['file'] for x in json.loads((r/'docs/image-manifest.json').read_text())]
def check(path):
 data=subprocess.check_output(['curl','--silent','--location','--fail',base+path]);local=(r/'public'/path).read_bytes();return {'path':path,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'matches_local':data==local}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(check,files))
report={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':base,'site_revision':'65a9a1863658092f8b64eca73eefdfe82e5a2e16','checks':results,'pass':all(x['matches_local'] for x in results)}
(r/'docs/qa/live-files.json').write_text(json.dumps(report,indent=2));print('Live file hashes match:',report['pass'],'files:',len(results))
assert report['pass']
