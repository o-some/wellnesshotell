from pathlib import Path
import sys,yaml,json,hashlib,subprocess
root=Path.cwd(); base=Path('/Users/eleftheriossamouladas/Library/CloudStorage/Dropbox/[[MD Mastery]]');sys.path.insert(0,str(base/'factory/runtime'));sys.path.insert(0,str(base/'factory/kernel/runtime'))
from caf_customer_workspace import local_observation
from caf_runtime_r3 import host_identity
from caf_execution_contract import enroll
from caf_design_resolver import resolve
mb=root/'.masterbrain'; customer=root.parent.parent
if (mb/'enrollment-receipt.json').exists(): raise SystemExit('Already enrolled. Preparation is not a reset command.')
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
request={'brief':'Build a premium German wellness hotel concept website with at least 15 high quality images, conversion journey, slow motion, parallax and shading. Publish o-some/wellnesshotell on GitHub Pages.','product_type':'website','customer_name':'Wellnesshotel','resolved_customer_root':str(customer),'person_relevance':False,'brand_inventory':'absent','design_selection':{'number':'188'},'locales':['de'],'release_requested':True}
(mb/'request.yml').write_text(yaml.safe_dump(request,allow_unicode=True))
c=yaml.safe_load((base/'templates/execution-contract.template.yml').read_text());c.update(contract={'id':'wellnesshotel-20261006','revision':0,'status':'ACTIVE','owner':'Codex'},identity={'project_name':'Wellnesshotel','canonical_repository':'https://github.com/o-some/wellnesshotell','project_root':str(root),'branch':'main','head_sha':head,'base_sha':head},outcome={'goal':request['brief'],'must_do':['15 distinct quality images','Nordic Light Spa source','functional concept planner','responsive and reduced motion','GitHub Pages'],'must_preserve':['existing README history','global factory','design library'],'must_not_do':['Sites operations','invent real prices or testimonials','claim actual booking']},scope={'owned_paths':['**'],'allowed_supporting_paths':[str(customer)],'protected_paths':[str(base)],'external_systems':['o-some/wellnesshotell']},release={'requested':True,'active_target':'https://o-some.github.io/wellnesshotell/'},human_gates=[],rollback={'strategy':'git revert','reference':head})
(mb/'execution-contract.yml').write_text(yaml.safe_dump(c,allow_unicode=True));(mb/'workflow-state.yml').write_text('workflow:\n  current_state: PLANNED\n');(mb/'evidence-graph.yml').write_text('claims: []\n')
obs=local_observation(customer,['web_brand']);binding={'root':str(customer),'root_id':obs['root_id'],'host_id':host_identity(),'profiles':['web_brand'],'mode':'local_single_host'}
r=enroll(root,request,binding,'codex-wellnesshotel',hashlib.sha256((mb/'execution-contract.yml').read_bytes()).hexdigest(),apply=True)
(mb/'enrollment-receipt.json').write_text(json.dumps(r,indent=2));print(r)
sel=resolve({'number':'188'},request['brief'],base);(mb/'design-selection.json').write_text(json.dumps(sel,indent=2,ensure_ascii=False))
