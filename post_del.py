import vk_api
import sys

TELEPHONE=sys.argv[1]
PASSWORD=sys.argv[2]
OWNER_ID=sys.argv[3]
POST_ID=sys.argv[4]

vk_session = vk_api.VkApi(TELEPHONE, PASSWORD,scope='wall, groups')
vk_session.auth()
vk = vk_session.get_api()
print(vk.wall.delete(owner_id=OWNER_ID, post_id=[POST_ID]))

