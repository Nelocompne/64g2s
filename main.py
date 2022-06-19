import requests
from lxml import html

URL = 'https://steamcommunity.com/groups/cnl4d2rpg'
r = requests.get(URL+'/memberslistxml/?xml=1')
tree = html.fromstring(r.content)
navareas = tree.xpath('//memberList/groupID64')
print(navareas)