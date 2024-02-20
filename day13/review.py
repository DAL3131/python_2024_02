def swap(x):
     b = list(str(x))
     b.reverse()
     return [int(i) for i in b]
print(swap(251531))
def solution(x):
    c = list(x)
    newNumber = ""
    for i,j in enumerate(c):
        if len(c) - i > 4:
            newNumber += "*"
        else:
            newNumber += j
    return newNumber

print(solution('01028372740'))







































