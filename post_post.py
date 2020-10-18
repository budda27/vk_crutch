import vk_api
import sys

TELEPHONE=sys.argv[1]
PASSWORD=sys.argv[2]
OWNER_ID=sys.argv[3]
PLAYLIST=sys.argv[4]

vk_session = vk_api.VkApi(TELEPHONE, PASSWORD, scope='wall, groups')
vk_session.auth()

vk = vk_session.get_api()

message='#RAP #РЭП #РУССКИЙ_РЭП #ХИП_ХОП #HIP_HOP #ТРЕК #МУЗЫКА #BOOM'

attachments=PLAYLIST

print(vk.wall.post(owner_id=OWNER_ID, message=message, attachments=attachments))

