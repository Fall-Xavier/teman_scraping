import re,requests,bs4
from bs4 import BeautifulSoup as parser
ses=requests.Session()

class Teman:
	
	def __init__(self):
		#self.token = "EAAGNO4a7r2wBAOqcyiJ8IfIsSP8SvW5bHaThiSFh7tFj4QSeeZA2cu1t38nuK4PrkX1CtqZCT7LxqAcV5Y4K2rWw4u0X2EVZAusPhvQOhf8uX5s9s777R3HBRaxyOxht2mHIfpOjRWfmrqEMKZCxSWZAX4mvB4YO1uHQS5dzaJZALtWwUy0KZBk"
		self.cookie = {"cookie": "sb=1_PWYhiPTCnLeVH6ykLR8F-E; datr=WIv3YmfN-i9hJj123mTEvNdJ; dpr=2; locale=id_ID; fr=0iC5h0oLPOw9GMeqM.AWUm4RmNr-bWH1HJddNtIGzadJc.BjfWME.0W.AAA.0.0.Bjl99t.AWWPnGzbve8; c_user=100088297642887; xs=15:uWOJOnaXLOVCug:2:1670897517:-1:-1; m_page_voice=100088297642887; m_pixel_ratio=2; wd=360x646"}
		link = input(" masukan link target : ")
		id= "".join(bs4.re.findall("://(.*?)/",link))
		self.main(bs4.re.sub(id,"m.facebook.com",link).replace("profile.php?id=","")+"?v=friends")
		
	def main(self,url):
		url = parser(ses.get(url,cookies=self.cookie).text,"html.parser")
		for z in url.find_all("a",href=True):
			if "fref" in z.get("href"):
				if "/profile.php?id=" in z.get("href"):
					uid = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",z.get("href")))
					nama = z.text
					print(uid+"<=>"+nama)
				else:
					uid = "".join(bs4.re.findall("/(.*?)\?",z.get("href")))
					nama = z.text
					print(uid+"<=>"+nama)
		for x in url.find_all("a",href=True):
			if "Lihat Teman Lain" in x.text:
				self.main("https://mbasic.facebook.com/"+x.get("href"))
		
Teman()