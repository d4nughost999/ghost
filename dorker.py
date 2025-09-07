import requests
from bs4 import BeautifulSoup

print(r"""
   ____             _             
  |  _ \  _   _| | _ _ __ 
  | | | |/ _ \ / | |/ / _ \ '|
  | |_| | (_) | (|   <  / |   
  |__/ \_/ \_|_|\_\_|_|   
        Simple Dorker - d4nu-ghost
""")

query = input("[?] Masukkan dork query: ")
url = f"https://duckduckgo.com/html/?q={query}"

headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

results = []
for a in soup.select(".result__a"):
    results.append(a.get("href"))
    print("[+] " + a.get("href"))

save = input("\nSimpan hasil ke file? (y/n): ")
if save.lower() == "y":
    with open("hasil_dork.txt", "w") as f:
        for r in results:
            f.write(r + "\n")
    print("[✔] Disimpan di hasil_dork.txt")
