# dict
# key-value, key(고유, only-one)
# key: int,str
# value: 내맘임

issac = {
    'ham':2500,
    'cheese':3000,
    'bacon':3000,
}
print(f"{issac['cheese']}")

bong = {
    'eggham':3800,
    'soya':3200,
    'original':3000,
}

cgv = {
    'popcorn':['소금', '카라멜', '어니언'],
    'becerage':{
        'sprite':2000,
        'zero_coke':1500

    }

}

#print(f"{cgv['popcorn'[0]]}")
#print(f"{cgv['becerage']['zero_coke']}")

mbti = {
    'e':'외향적',
    'i':'내향적',
    's':'현실적',
    'n':'미래지향적',
    'f':'감성적',
    't':'발',
    'p':'즉흥적',
    'j':'계획적',

}
q = input("당신의 mbti는 무엇인가요?")
print(f"당신은 {mbti[q[0]]}이고 {mbti[q[1]]}이며 {mbti[q[2]]}이고 {mbti[q[3]]}군요")








