import vk_api
import sys
import simplejson as json
from vk_api.audio import VkAudio

TELEPHONE=sys.argv[1]
PASSWORD=sys.argv[2]
OWNER_ID=sys.argv[3]
#PLAYLIST="sys.argv[4]"

#print(TELEPHONE)
#print(PASSWORD)
#print(OWNER_ID)

vk_session = vk_api.VkApi(TELEPHONE, PASSWORD,scope='wall, groups, friends')
vk_session.auth()
vk = vk_session.get_api()

vkaudio = VkAudio(vk_session)

jsonData = json.dumps(vkaudio.get_albums(OWNER_ID))

sem = 0
while sem < 99999999:
    try:
        dictData = json.loads(jsonData)[sem]
        x = (dictData["url"])
        # А тут мы подрежем url
        y = (dictData["access_hash"])
        if y is not None:
            #try:
            s = x+"_"+y
            print(s.split('=')[1])
            #except:
        else:
            print(x.split('=')[1])
        sem = sem + 1
    except:
        break

