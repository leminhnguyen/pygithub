# Clone the repos from github by `PyGithub`

## Installation
```bash
$ pip install -r requirements.txt
```

## Try with the code

```python
# get access token from github website
access_token = "4756748ebe2db17e6b56a05f******"
g = Github(access_token)
username = "username-of-repo"
password = "password-of-repo"
all_repos = g.get_user().get_repos()
for repo in all_repos:
    print(repo.name)
```