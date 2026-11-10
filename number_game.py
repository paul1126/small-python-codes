import random

n = int(input("시도 횟수:"))
rg = int(input("숫자 제한 범위:"))
random.seed()
rdn = random.randint(0, rg)

for i in range(n):
    print("\n")
    rdt = int(input(">>"))

    if rdt > rdn:
        print("더 작음")

    if rdt < rdn:
        print("더 큼")

    if rdt == rdn:
        print("정답")
        break
