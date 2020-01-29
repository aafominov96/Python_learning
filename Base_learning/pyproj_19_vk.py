from urllib.parse import urlencode
from urllib.parse import urlparse
import requests
import time

def our_friends(f_id, myf, at):
    print(len(myf))
    vers_1 = '5.101'
    base_1 = 'https://api.vk.com/method/'
    method_friends_1 = 'friends.get'
    auth_1 = '?' + 'user_id=' + str(f_id) + '&' + 'order=name&access_token=' + str(at) + '&v=' + vers_1
    tovk_1 = base_1 + method_friends_1 + auth_1
    answer_1 = requests.get(tovk_1)

    list_friend = set(answer_1.json()['response']['items'])
    print(len(list_friend))
    final_set = myf
    final_set.intersection_update(list_friend)
    print(len(final_set))
    return list(final_set)

auth_url = 'https://oauth.vk.com/authorize'
vers = '5.101'
app_id = 7076416

auth_data = {
    'client_id': app_id,
    'display': 'mobile',
    'response_type': 'token',
    'scope': 'friends',
    'v': vers
}
print('?'.join((auth_url, urlencode(auth_data))))

#token_url = input('Input token url: ')
token_url = 'https://oauth.vk.com/blank.html#access_token=359c2a2092c3e2cb93830823fdedc823ef0cfdf372c1f22710a5df160a49fbc5741e343a5770aea08f41f&expires_in=86400&user_id=48168640'
o = urlparse(token_url)
print(o)
fragments = dict((i.split('=') for i in o.fragment.split('&')))
access_token = fragments['access_token']
print(access_token)
#access_token = input()
parameters = {
    'access_token': access_token,
    'v': vers
}
#response = requests.get('https://api.vk.com/method/friends.get', parameters)
base = 'https://api.vk.com/method/'
method_friends ='friends.get'
method_users = 'users.get'
auth = '?'+'access_token='+str(access_token)+'&'+'v='+str(vers)
response = requests.get(base+method_friends+auth)
list_my = response.json()['response']['items']
'''answer = []
for user_id in response.json()['response']['items']:
    answer.append(requests.get(base+method_users, {'user_ids': user_id, 'access_token': access_token, 'v': vers}))
    time.sleep(0.2)
for i in range(0, len(answer)):
    try:
        print(answer[i].json()['response'][0]['id'])
    except:
        print('Error field')'''



answer = []
for user_id in our_friends(155412220, set(list_my), access_token):
    answer.append(requests.get(base+method_users, {'user_ids': user_id, 'access_token': access_token, 'v': vers}))
    time.sleep(0.2)
for i in range(0, len(answer)):
    try:
        print(answer[i].json()['response'][0])
    except:
        print('Error field')