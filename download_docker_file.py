import requests
import os
import sys
from github import Github

# Set your GitHub access token here or use an environment variable
access_token = os.environ.get("ACCESS_TOKEN")
if access_token is not None:
    access_token = access_token
else:
    print("Make sure to set and env ACCESS_TOKEN")
    sys.exit(0)

g = Github(access_token)

# for repo in g.get_user().get_repos():
repo = g.get_repo("elior7557/protfolio-DevOps-application")
# try:
repo_content = repo.get_contents("")
while repo_content:
    file_content = repo_content.pop(0)
    if file_content.type == "dir":
        repo_content.extend(repo.get_contents(file_content.path))
    else:
        file_name = file_content.name.lower()
        if "docker" in file_name and file_name != ".dockerignore":
            print(file_content.name)
            if file_content.encoding == "base64":
                # need to decode again from bytes to utf-8
                print(file_content.decoded_content.decode("utf-8"))    

# except:
#         print("Something else went wrong")






