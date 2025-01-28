import requests
import os

owner = 'hishmathdeen'
repo = 'terragrunt-testing'
pr_number = os.getenv('PR_NUMBER')
token = os.getenv('GT_TOKEN')
dir_path = os.getenv('DIR')

file_path = '/home/runner/work/terragrunt-testing/terragrunt-testing/plans/plan.txt'
with open(file_path, 'r') as file:
    file_data = file.read()

comment = f"""
### :rocket: Infrasturece Change requtested
:memo: Terragrant File updated in `{dir_path}`

---

### :bulb: View the Plan

<details>
  <summary>Terragrunt Plan</summary>

  Here is the data from the text file:

  ```txt
  {file_data}
  ```
</details>

---

:checkered_flag: Review and Merge the PR

"""

url = f'https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments'

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

payload = {
    'body': comment
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 201:
    print('Comment posted')
else:
    print(f'Failed to post comment: {response.status_code} - {response.text}')
