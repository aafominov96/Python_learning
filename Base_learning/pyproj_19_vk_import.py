import vk_api as vk

access_token = 'a722279dd7a7aa10e1519a628a7ae2c75d4bf09a77207432f157bcfb01545bab36327b1d01e542fbc886d'
vk_session = vk.VkApi(login='+79150600541', password='Fomaspas', api_version='5.101',
                      app_id=7076416, scope='wall,friends')
vk_session.auth()
VK = vk_session.get_api()

response = VK.wall.get(count=3)
print(response['items'])


response = VK.friends.get()
print(response)

response = VK.friends.getRecent(count=5)
print(response)

response = VK.friends.getOnline(user_id=155412220, count=5)
print(response)