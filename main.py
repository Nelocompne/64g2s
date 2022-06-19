from requests_xml import XMLSession
import sys

session = XMLSession()
# URL e.g. https://steamcommunity.com/groups/myanimeclan

r = session.get(sys.argv[1]+'/memberslistxml/?xml=1')
g = r.xml.xpath('//groupID64', first=True)
print('ID:', int(g.text)-103582791429521408)

# 计算方法 https://forums.alliedmods.net/showthread.php?t=295678