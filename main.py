import requests
import pprint
import re
import json

APIKEY = 'b22736caea19ab796652bf68c6b1af6c'
ENDPOINT = 'https://api.chatwork.com/v2'
path = '/root/chatwork_invite_test/idlist.txt'
headers = { 'X-ChatWorkToken': APIKEY }

post_message_url = '{}/rooms'.format(ENDPOINT)
resp = requests.get(post_message_url,headers=headers)
data = resp.json()

for line in data:
    post_message_url = '{}/rooms/{}/link'.format(ENDPOINT, line["room_id"])
    resp = requests.get(post_message_url,headers=headers)
    data = resp.json()
    if data["public"]:
        print(line["name"] + "," + data["url"])
    else:
        print(line["name"] + "," + "false")
