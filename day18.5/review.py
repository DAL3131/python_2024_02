# 1. 조건에 맞게 수열 변환하기
# 정수 배열 arr와 자연수 k가 주어집니다. 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고,
# k가 짝수라면 arr의 모든 원소에 k를 더합니다. 이러한 변환을 마친 후의 arr을 return 하는 solution 함수를 완성해 주세요.

# 2. A강조 하기
# 문자열 myString이 주어집니다. myString 에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고,
# "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하세요.

def solution1(arr, k):
    if k % 2 != 0:  # 홀수
        return [i * k for i in arr]
    else:
        return [i + k for i in arr]


def solution2(myString):
    my = myString.lower()
    return my.replace("a", "A")


print(solution2("abstract akgebra"))
print(solution2("PROGRaMMERS"))
print(solution1([1, 2, 3, 100, 99, 98], 3))
print(solution1([1, 2, 3, 100, 99, 98], 2))
