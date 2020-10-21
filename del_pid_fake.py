

import vk_api

TELEPHONE=sys.argv[1]
PASSWORD=sys.argv[2]
GROUP_ID=sys.argv[3]
ID_DELL=sys.argv[4]


import vk_api 
vk_session = vk_api.VkApi(TELEPHONE, PASSWORD,scope='wall, groups') 
vk_session.auth() 
vk = vk_session.get_api()

if GROUP_ID >= 0:
  print(vk.account.ban(owner_id=ID_DELL))
else:
  print(vk.groups.ban(owner_id=ID_DELL, group_id=abs(GROUP_ID),reason=0,comment='ты же фейк'))

