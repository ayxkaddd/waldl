import os
import sys
import random
import string
import pathlib
import requests
import threading

DOWNLOAD_DIR = f"{str(pathlib.Path.home())}/pics/walls"

def generate_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))


def get_ext(url):
    ext = os.path.splitext(url)[1]
    return ext


def download_wallpaper(url):
    small_url = f"https://.../{url.split('/')[-1]}"
    print(f"[***] Downloading {small_url}")
    with requests.Session() as session:
        session.keep_alive = True
        res = session.get(url, allow_redirects=True)
        download_path = f"{DOWNLOAD_DIR}/{generate_id()}{get_ext(url)}"
        open(download_path, 'wb').write(res.content)
    print(f"[!!!] Downloading done of {small_url}")
    

def wallpaper_search_api(query):
    query_url = f"https://wallhaven.cc/api/v1/search?q={query}" 
    res = requests.get(query_url)
    response = res.json()
    dl_links = []
    for wallpaper in response["data"]:
        dl_links.append(wallpaper["path"])

    return dl_links


os.makedirs(DOWNLOAD_DIR, exist_ok=True)
if len(sys.argv) < 2:
    print("Usage waldl.py <search_query>")
    quit()


query = sys.argv[1].replace(' ', '+')
wallpapers = wallpaper_search_api(query)
threads = []

for wallpaper in wallpapers:
    t = threading.Thread(target=download_wallpaper, args=(wallpaper,))
    t.start()
    threads.append(t)


for t in threads:
    t.join()


print(f"Download complite!")
