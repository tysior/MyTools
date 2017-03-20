import requests
import json
import sys

org_url = 'https://api.github.com/orgs/'+sys.argv[1]+'/repos'
r = requests.get(org_url)
repos = json.loads(r.text)

for repo in repos:
    repo_data = requests.get('https://api.github.com/repos/'+sys.argv[1]+'/'+repo['name']+'/git/trees/master?recursive=1')
    files = fl = json.loads(repo_data.text)
    for file in files:
        if '.md' in f['path']:
            md_file = requests.get('https://api.github.com/repos/'+sys.argv[1]+'/'+repo['name']+'/contents/'+f['path'])
            contents = md_file.text.split('\n')
            for line in contents:
                if '|' in line and '/intel' in line:
                    print(line)