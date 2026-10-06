import concurrent.futures,hashlib,json,subprocess,urllib.request
from pathlib import Path
base="https://o-some.github.io/wellnesshotell/"
paths=["index.html","styles.css","cinematic.css","app.js","bildnachweise.html"]+["assets/"+x+suffix+".webp" for x in ["dawn","dusk"] for suffix in ["","-800","-1440"]]
def check(p):
 data=urllib.request.urlopen(base+p+"?v=still-cinema-3",timeout=40).read()
 local=Path("public",p).read_bytes()
 return {"path":p,"matches":data==local,"sha256":hashlib.sha256(data).hexdigest()}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: results=list(ex.map(check,paths))
report={"url":base,"revision":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"files":results}
Path("docs/cinematic-expansion/live.json").write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
assert all(r["matches"] for r in results)
