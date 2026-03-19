for k in range(3):
    print(k,end=" ")

print()

for i in range(1, 4):          # i는 1, 2, 3 (각 줄의 시작 숫자)
    for j in range(i, i + 3):  # j는 i부터 i+2까지 3개의 숫자
        if j == i + 2:         # 줄의 마지막 숫자라면 쉼표 없이 출력
            print(j)           
        else:                  # 마지막 숫자가 아니라면 쉼표 포함
            print(j, end=",")