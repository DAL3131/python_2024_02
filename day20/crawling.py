# from bs4 import BeautifulSoup
# import requests
#
# # url = "https://finance.naver.com/sise/"
# # # 위 url에서 정보 가져오기
# # response = requests.get(url)
# # # 인코딩하기
# # response.encoding = 'cp949'
# # # 텍스트화 하기
# # html = response.text
# # # 크롤링 시작하기
# # soup = BeautifulSoup(html,'html.parser')
# #
# # itemList = soup.find(id="popularItemList")
# # li_list = itemList.find_all('li')
# #
# # stockList = []
# # for i in li_list:
# #     stockList.append({'company':i.find('a').text,'price':i.find('span')})
# # print(stockList)
#
#
# url = "https://www.melon.com/index.htm"
# response = requests.get(url)
# response.encoding = 'cp949'
# html = response.text
