import os,re,json,urllib.request,datetime
from pathlib import Path
R=Path(__file__).resolve().parents[1]; U="syedomer17"
H={"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28"}
if os.getenv("GITHUB_TOKEN"): H["Authorization"]="Bearer "+os.getenv("GITHUB_TOKEN")
def get(u):
    q=urllib.request.Request(u,headers=H)
    with urllib.request.urlopen(q,timeout=30) as x:return json.load(x)
u=get(f"https://api.github.com/users/{U}"); rs=get(f"https://api.github.com/users/{U}/repos?per_page=100&type=owner")
join_year = 2024
try:
    if "created_at" in u:
        join_year = datetime.datetime.strptime(u["created_at"], "%Y-%m-%dT%H:%M:%SZ").year
except:
    pass
current_year = datetime.date.today().year

total_contributions = 0
for yr in range(join_year, current_year + 1):
    try:
        c_req = urllib.request.Request(f"https://github.com/users/{U}/contributions?from={yr}-01-01&to={yr}-12-31", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(c_req, timeout=30) as x:
            c_html = x.read().decode("utf-8")
        c_match = re.search(r'(\d[\d,]*)\s+contributions', c_html)
        if c_match:
            total_contributions += int(c_match.group(1).replace(",", ""))
    except Exception as e:
        print(f"Warning: Failed to fetch contributions for {yr}: {e}")

contributions = f"{total_contributions:,}" if total_contributions > 0 else "0"

total_years = current_year - join_year + 1
if total_years == 1:
    lbl = "Contributions (1 Year)"
else:
    lbl = f"Contributions ({total_years} Years)"
dots = "." * max(0, 38 - len(lbl))
contributions_label = f"{lbl}<tspan class=\"text-dots\">{dots}</tspan>"

v={
    "repos": f"{u.get('public_repos',0):,}",
    "stars": f"{sum(x.get('stargazers_count',0) for x in rs):,}",
    "contributions_label": contributions_label,
    "contributions": contributions,
    "updated": datetime.date.today().isoformat()
}
for t in ("dark","light"):
 p=R/f"assets/profile-{t}.svg"; s=p.read_text()
 for k,n in v.items(): s=re.sub(rf'(<text id="{k}"[^>]*>).*?(</text>)',rf'\g<1>{n}\g<2>',s)
 p.write_text(s)
print(v)
