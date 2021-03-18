import re
from tqdm import tqdm
import os
from github import Github  # https://github.com/PyGithub/PyGithub

# get access token from github website
access_token = "4756748ebe2db17e6b56a05f******"
g = Github(access_token)
username = "username-of-repo"
password = "password-of-repo"
all_repos = g.get_user().get_repos()

# Then play with your Github objects:
# Clone all repo of the KSTN class (start with KSTN)
kstn_repos = [repo for repo in all_repos if repo.name.startswith("TKXDPM.KSTN.20201-")]
kstn_repos = [f"https://{username}:{password}@{re.search('github.com.*', repo.git_url).group()}" for repo in kstn_repos]

for repo in tqdm(kstn_repos):
    src = repo # repo url
    dest = "/home/nguyenlm/Desktop/TA-TKXDPM/KSTN" # clone to destination folder
    os.system(f"git clone {repo} {dest}/{repo.split('/')[-1][:-4]}")