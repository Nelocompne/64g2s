from requests_html import HTMLSession
session = HTMLSession()

URL = 'https://steamcommunity.com/groups/cnl4d2rpg'
r = session.get(URL+'/memberslistxml/?xml=1')
g = r.html.find('groupID64', first=True)
print(int(g.text)-103582791429521408)
# 实现原因来自 https://forums.alliedmods.net/showthread.php?t=295678