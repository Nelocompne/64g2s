from requests_xml import XMLSession
import argparse

parser = argparse.ArgumentParser(description='help')
parser.add_argument('-u', dest='url', type=str, help='steam 组主页链接 e.g. https://steamcommunity.com/groups/myanimeclan')
args = parser.parse_args()

session = XMLSession()

r = session.get(args.url+'/memberslistxml/?xml=1')
g = r.xml.xpath('//groupID64', first=True)
print('ID:', int(g.text)-103582791429521408)

# 计算方法 https://forums.alliedmods.net/showthread.php?t=295678