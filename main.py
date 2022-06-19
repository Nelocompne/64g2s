import requests
from lxml import etree

URL = 'https://steamcommunity.com/groups/cnl4d2rpg'
r = requests.get(URL+'/memberslistxml/?xml=1')
tree = etree.parse(r.content)
root = tree.getroot()