for i in range(63,6,-7):
    print(i)

# 1부터 100까지 (101은 포함 안 됨) + 99부터 1까지 (-1씩 감소, 0은 포함 안 됨)
up_down = tuple(range(1, 101)) + tuple(range(99, 0, -1))

print(up_down)