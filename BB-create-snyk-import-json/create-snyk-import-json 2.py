import requests
from requests.auth import HTTPBasicAuth
import json
import os
from datetime import datetime

##Bitbucket login credentials
username = os.environ["BITBUCKET_USERNAME"] #CHANGEME
password = os.environ["BITBUCKET_KEY"] #CHANGEME

full_repo_list = [] # to store every piece of information from bitbucket
targets_list = [] # to store snyk related fields

next_page_url = 'https://api.bitbucket.org/2.0/repositories/{YOUR_BITBUCKET_REPO}' #CHANGEME


# Keep fetching pages while there's a page to fetch
while next_page_url is not None:
  response = requests.get(next_page_url, auth=HTTPBasicAuth(username, password))
  page_json = response.json()

  # Parse repositories from the JSON
  for repo in page_json['values']:
    reponame=repo['slug']
    full_repo_list.append(response.text)
    target_item = {}
    target_item['orgId']='{YOUR_SNYK_ORG_ID}' #CHANGEME
    target_item['integrationId']='{YOUR_SNYK_INTEGRATION_ID}' #CHANGEME
    target_item['target']={}
    target_item['target']['owner']=repo['owner']['display_name']
    target_item['target']['name']=repo['slug']
    target_item['target']['branch']=repo['mainbranch']['name']
    targets_list.append(target_item)
    print(target_item)

  next_page_url = page_json.get('next', None)

with open("repos-"+datetime.now().strftime("%Y%m%d-%H%M%S")+".txt","w") as outfile:
    for item in full_repo_list:
        outfile.write(json.dumps(json.loads(item), sort_keys=True, indent=4, separators=(",", ": ")))

targets_dict = {'targets':targets_list}
with open("snyk-targets-"+datetime.now().strftime("%Y%m%d-%H%M%S")+".json", 'w', encoding='utf-8') as f:
    json.dump(targets_dict, f, ensure_ascii=True, indent=4)
