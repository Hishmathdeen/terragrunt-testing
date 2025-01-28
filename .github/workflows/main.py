import requests

# Replace with your GitHub repository details
owner = 'hishmathdeen'  # GitHub username or organization
repo = 'demo-terra-atlantis'  # GitHub repository name
pr_number = 3  # PR number (e.g., 1 for PR #1)

# Personal access token (PAT) with necessary permissions
token = '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'

# The comment you want to post
# comment = 'This is a comment from the API.'

file_path = 'plan.txt'
with open(file_path, 'r') as file:
    file_data = file.read()

comment = f"""
### :memo: PR Summary

**Summary**: This PR improves the performance of the system by refactoring the data processing module.

---

### :rocket: Detailed View

**Changes made:**
- Refactored data processing logic in `data_processor.py`.
- Optimized the database queries for better performance.
- Added unit tests for the new functions.

**Performance improvements**:
- Data processing time reduced by 20%.
- CPU usage during peak times dropped by 15%.

---

:checkered_flag: Ready for review!

---

### :bulb: Notes:
Please test on the staging environment before merging. :warning:

---

<details>
  <summary>Click to see the detailed data</summary>

  Here is the data from the text file:

  ```txt
  {file_data}
  ```
</details> """


# GitHub API URL to post a comment on a PR
url = f'https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments'

# HTTP headers
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Payload with the comment body
payload = {
    'body': comment
}

# Send POST request to create the comment
response = requests.post(url, headers=headers, json=payload)

# Check the response
if response.status_code == 201:
    print('Comment posted successfully.')
else:
    print(f'Failed to post comment: {response.status_code} - {response.text}')
