cnt_three = 0
cnt_five = 0

for _ in range (10):
    num = int(input())
    if num % 3 == 0:
        cnt_three += 1
    if num % 5 == 0:
        cnt_five += 1
    
print(cnt_three, cnt_five)