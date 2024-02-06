# set: 중복 허용안됨, 집합개념
# a = {1,2,3,1,2,3,1,2,3}
# a.add(4) # 추가
# a.discard(3) # 삭제
# print(a)
# # set() - 세트화
# b = set([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])
#
# print(b)

# 영어 신문기사 스크랩 후, 단어들 리스트하기

news = """Tuesday's UK front pages are of course dominated by news of the King's health.

The headline on The Sun is stark - "King: I have cancer". The Mirror calls it a "shock" and notes that it was his recent prostate operation which led to the diagnosis.

The Times reports that the Palace says Charles is "wholly positive". The i says that the announcement "abandons royal protocol" regarding comment on the monarch's health and The Express says Prince Harry will see his father in coming days.

The Guardian chose not to put a picture of King Charles next to its front-page article, opting for Taylor Swift at the Grammys instead. The Telegraph goes the other way - devoting its entire front to the story, while the Daily Mail headline reports the King is "so grateful they caught it early"."""


words = news.split(" ")
word = list(set(words))
print(word.sort)











