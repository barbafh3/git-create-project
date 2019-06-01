import sys
import os
import requests
import mechanicalsoup
from bs4 import BeautifulSoup

base_url = "https://www.github.com"
repo = sys.argv[1]
path = sys.argv[2]
cmd = "pass github"

username = "barbafh3"
password = os.popen(cmd).read().strip()
# print(f'$${password}$$')

os.system('echo Logging into Github...')
browser = mechanicalsoup.StatefulBrowser()
browser.open(f'{base_url}/new')
browser.select_form('#login form')
browser['login'] = username
browser['password'] = password
resp = browser.submit_selected()
if resp.ok:
    os.system('echo Successfully logged into Github.')
    os.system(f'echo Creating repository {repo}...')
    browser.select_form(browser.get_current_page().find_all('form')[3])
    browser.get_current_page() \
           .find('input', id='repository_name')['value'] = repo
    repo_resp = browser.submit_selected()
    if repo_resp.ok:
        os.system(f'echo Repository {repo} successfully created.')
        os.system(f'echo Adding remote git for repository {repo}...')
        command = browser.get_current_page() \
            .find_all('span', class_='user-select-contain')[4].text
        command2 = browser.get_current_page() \
            .find_all('span', class_='user-select-contain')[5].text
        os.chdir(path)
        os.system(command)
        os.system('touch README.md && echo buba >> README.md')
        os.system('git add README.md && git commit -am "Initial commit"')
        os.system(command2)
        os.system('echo Project successfully created.')
    else:
        os.system('echo Failed to create repository')
        exit()

else:
    os.system("echo Login failed")
    exit()
