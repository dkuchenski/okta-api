"""
Simple Okta API wrapper with Python3.6+
Requires two environment variables:
    OKTA_DOMAIN
    OKTA_API_TOKEN
"""

import requests
import json
import os


domain = os.environ.get('OKTA_DOMAIN')
api_token = os.environ.get('OKTA_API_TOKEN')
base_url = f'https://{domain}/api/v1'
headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'SSWS ' + api_token,
}


def _oktaBool(boolean):
    return str(boolean).lower()


# Example for adding "pretty print" option to function output
def getUser(user, pretty_print=False):
    url = f'{base_url}/users/{user}'
    response = requests.get(url, headers=headers)
    if pretty_print:
        return json.dumps(response.json(), indent=4)
    else:
        return response.json()


def getUsers():
    url = f'{base_url}/users'
    response = requests.get(url, headers=headers)
    response_data = response.json()
    while response.links.get('next'):
        url = response.links['next']['url']
        response = requests.get(url, headers=headers)
        response_data += response.json()
    return response_data


def getUserGroups(user):
    url = f'{base_url}/users/{user}/groups'
    response = requests.get(url, headers=headers)
    return response.json()


def getUserApps(user):
    url = f'{base_url}/users/{user}/appLinks'
    response = requests.get(url, headers=headers)
    return response.json()


def getGroup(group):
    url = f'{base_url}/groups/{group}'
    response = requests.get(url, headers=headers)
    return response.json()


def getGroupList():
    url = f'{base_url}/groups?filter=type+eq+"OKTA_GROUP"'
    response = requests.get(url, headers=headers)
    return response.json()


def getGroupMembers(group):
    url = f'{base_url}/groups/{group}/users'
    response = requests.get(url, headers=headers)
    return response.json()


def getApp(app):
    url = f'{base_url}/apps/{app}'
    response = requests.get(url, headers=headers)
    return response.json()


def getAppMembers(app):
    url = f'{base_url}/apps/{app}/users'
    response = requests.get(url, headers=headers)
    response_data = response.json()
    while response.links.get('next'):
        url = response.links['next']['url']
        response = requests.get(url, headers=headers)
        response_data += response.json()
    return response_data


def getAppList():
    url = f'{base_url}/apps?filter=status+eq+"ACTIVE"&limit=100'
    response = requests.get(url, headers=headers)
    response_data = response.json()
    while response.links.get('next'):
        url = response.links['next']['url']
        response = requests.get(url, headers=headers)
        response_data += response.json()
    return response_data


def updateGroupAddMember(group, user):
    url = f'{base_url}/groups/{group}/users/{user}'
    response = requests.put(url, headers=headers)
    return response.json()


def updateGroupRemoveMember(group, user):
    url = f'{base_url}/groups/{group}/users/{user}'
    response = requests.delete(url, headers=headers)
    return response.json()


def updateUserSecurityQuestion(user, question, answer):
    url = f'{base_url}/users/{user}'
    data = {
        'credentials': {
            'recovery_question': {
                'question': question,
                'answer': answer
            }
        }
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def updateUserSetPassword(user, password):
    url = f'{base_url}/users/{user}'
    data = {
        'credentials': {
            'password': {'value': password}
        }
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def updateUserResetFactors(user):
    url = f'{base_url}/users/{user}/lifecycle/reset_factors'
    response = requests.post(url, headers=headers)
    return response.json()


def updateUserResetPassword(user, send_email=True):
    url = f'{base_url}/users/{user}/lifecycle/reset_password?sendEmail={_oktaBool(send_email)}'
    response = requests.post(url, headers=headers)
    return response.json()


def updateUserExpirePassword(user, temp_password=False):
    url = f'{base_url}/users/{user}/lifecycle/expire_password?tempPassword={_oktaBool(temp_password)}'
    response = requests.post(url, headers=headers)
    return response.json()


def updateUserUnlock(user):
    url = f'{base_url}/users/{user}/lifecycle/unlock'
    response = requests.post(url, headers=headers)
    return response.json()


def updateUserActivate(user, send_email=True):
    url = f'{base_url}/users/{user}/lifecycle/activate?sendEmail={_oktaBool(send_email)}'
    response = requests.post(url, headers=headers)
    return response.json()


def updateUserReactivate(user, send_email=True):
    url = f'{base_url}/users/{user}/lifecycle/reactivate?sendEmail={_oktaBool(send_email)}'
    response = requests.post(url, headers=headers)
    return response.json()
