m1 = [list(map(int, input().split())) for _ in range((3))]
input()
m2 = [list(map(int, input().split())) for _ in range((3))]

for i in range(3):
    for j in range(3):
        print(m1[i][j]*m2[i][j], end=' ')
    print()