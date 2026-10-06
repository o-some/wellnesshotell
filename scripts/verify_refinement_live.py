import concurrent.futures,hashlib,json,subprocess,urllib.request
from pathlib import Path
base="https://o-some.github.io/wellnesshotell/"
paths=["index.html","styles.css","app.js","bildnachweise.html","assets/breakfast-v2.webp","assets/breakfast-v2-640.webp","assets/breakfast-v2-1000.webp"]
def check(p):
 data=urllib.request.urlopen(base+p+"?v=still-light-2",timeout=40).read()
 local=Path("public",p).read_bytes()
 return {"path":p,"matches":data==local,"sha256":hashlib.sha256(data).hexdigest()}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex: results=list(ex.map(check,paths))
report={"url":base,"revision":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"files":results}
Path("docs/qa/refinement/live.json").write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
assert all(r["matches"] for r in results)
