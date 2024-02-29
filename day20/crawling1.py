from bs4 import BeautifulSoup
import requests

url = "https://www.musinsa.com/ranking/best"
# 위 url에서 정보 가져오기
response = requests.get(url)
# 인코딩하기
response.encoding = 'utf-8'
# 텍스트화 하기
html = response.text
# 크롤링 시작하기
soup = BeautifulSoup(html, 'html.parser')

companies = soup.find_all("p", class_="item_title")
companyList = [i.text.strip() for i in companies]

infos = soup.find_all("p", class_="list_info")
infoList = [i.text.strip() for i in infos]

prices = soup.find_all("p", class_="price")
priceList = [i.text.strip().replace(" ", "").split("\n")[0] for i in prices]

print(companyList)
print(infoList)
print(priceList)