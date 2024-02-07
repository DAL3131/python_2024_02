mmovie = {
    'movie':[
        {'name': '액션 영화', 'price': 10000},
        {'name': '로맨틱 코미디', 'price': 8000},
        {'name': '공포 영화', 'price': 9000},
    ],
    'popcorn':[
        {'name': '치즈 팝콘', 'price':6000,},
        {'name': '카라멜 팝콘', 'price':5000},
        {'name': '일반 팝콘', 'price':5000,},
    ]
}

print(f"{mmovie['movie'],mmovie['popcorn']}")
num = int(input("영화를 고르세요"))
num2 = int(input("팝콘을 고르세요"))
print(f"구매한 영화는 {mmovie['movie'][num]['name']}고, 팝콘은 {mmovie['popcorn'][num2]['name']}입니다. "
      f"총 금액은 {mmovie['movie'][num]['price'] + mmovie['popcorn'][num2]['price']}에요.")












