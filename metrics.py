import requests, pathlib, sys

USER = "nedimperva"              # ← your username
OUT  = pathlib.Path("github-metrics.svg")

url = (
    f"https://github-readme-stats.vercel.app/api"
    f"?username={USER}&show_icons=true&theme=radical"
    f"&count_private=true&include_all_commits=true"
)
svg = requests.get(url, timeout=30).text
OUT.write_text(svg, encoding="utf-8")