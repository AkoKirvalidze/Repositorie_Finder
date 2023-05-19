import requests
from bs4 import BeautifulSoup
from RepositorieDatabase import RepoDatabase
from Repo import Repositorie

database = RepoDatabase("repobase")
coder = input("which developer? - ")

url = f'https://github.com/{coder}?tab=repositories'
content = requests.get(url).text
info = BeautifulSoup(content, "html.parser")

divs = info.find_all(class_="col-10 col-lg-9 d-inline-block")

for div in divs:
    name = div.find(itemprop="name codeRepository")
    desc = div.find(itemprop="description")
    lan = div.find(itemprop="programmingLanguage")

    if name and desc and lan:
        rep = Repositorie(name.string.strip(), desc.string.strip(), lan.string.strip())
        database.add_repos(rep)
    elif name and desc:
        rep = Repositorie(name.string.strip(), desc.string.strip(), None)
        database.add_repos(rep)
    elif name and lan:
        rep = Repositorie(name.string.strip(), None, lan.string.strip())
        database.add_repos(rep)
    elif name and lan is None and desc is None:
        rep = Repositorie(name.string.strip(), None, None)
        database.add_repos(rep)






