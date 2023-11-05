import requests
import base64
import random
import time
import json

with open('config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    username = data['username']
    repository = data['repository']
    token = data['token']
    time_ = data['time']

url = f'https://api.github.com/repos/{username}/{repository}/contents/README.md'
headers = {
    'Authorization': f'token {token}'
}

def active():
    response = requests.get(url, headers=headers)
    response_data = response.json()
    current_content = base64.b64decode(response_data['content']).decode('utf-8')

    new_content = current_content + f"\n<!--- HASH: {random.randint(100000000000, 10000000000000)} --->"

    update_data = {
        'message': 'update README',
        'content': base64.b64encode(new_content.encode('utf-8')).decode('utf-8'),
        'sha': response_data['sha']
    }

    update_url = f'https://api.github.com/repos/{username}/{repository}/contents/README.md'
    response = requests.put(update_url, headers=headers, json=update_data)

    if response.status_code == 200:
        print('README successfully updated')
    else:
        print('An error occurred while updating the README:', response.status_code)
        print(response.text)

while True:
    active()
    time.sleep(time_)


# My GitHub - github.com/reques6e
# Pls, no abuse...
