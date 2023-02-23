from github import Github
import helper
import subprocess
# using an access token
g = Github("4a7abb09d7fac7853eafbdfc687e8609021f8f7d")

# # Github Enterprise with custom hostname
# g = Github(base_url="ansible/ansible", login_or_token="4a7abb09d7fac7853eafbdfc687e8609021f8f7d")
repo = g.get_repo("ansible/ansible")
print(repo.collaborators_url)

result = subprocess.run(['https://api.github.com/repos/ansible/ansible/collaborators'], stdout=subprocess.PIPE)

