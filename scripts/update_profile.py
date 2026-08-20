import os,re,json,urllib.request,datetime
from pathlib import Path
R=Path(__file__).resolve().parents[1]; U="syedomer17"
H={"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28"}
if os.getenv("GITHUB_TOKEN"): H["Authorization"]="Bearer "+os.getenv("GITHUB_TOKEN")
def get(u):
    q=urllib.request.Request(u,headers=H)
    with urllib.request.urlopen(q,timeout=30) as x:return json.load(x)
u=get(f"https://api.github.com/users/{U}"); rs=get(f"https://api.github.com/users/{U}/repos?per_page=100&type=owner")
try:
    c_req=urllib.request.Request(f"https://github.com/users/{U}/contributions",headers={"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(c_req,timeout=30) as x:
        c_html=x.read().decode("utf-8")
    c_match=re.search(r'(\d[\d,]*)\s+contributions\s+in\s+the\s+last\s+year',c_html)
    contributions=c_match.group(1) if c_match else "0"
except:
    contributions="0"
v={
    "repos": f"{u.get('public_repos',0):,}",
    "stars": f"{sum(x.get('stargazers_count',0) for x in rs):,}",
    "contributions": contributions,
    "updated": datetime.date.today().isoformat()
}
for t in ("dark","light"):
 p=R/f"assets/profile-{t}.svg"; s=p.read_text()
 for k,n in v.items(): s=re.sub(rf'(<text id="{k}"[^>]*>).*?(</text>)',rf'\g<1>{n}\g<2>',s)
 p.write_text(s)
print(v)
