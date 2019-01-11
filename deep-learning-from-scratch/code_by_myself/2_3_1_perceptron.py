def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta :
        return 1

ans1 = AND(0,0)
ans2 = AND(1,0)
ans3 = AND(0,1)
ans4 = AND(1,1)

print(ans1)
print(ans2)
print(ans3)
print(ans4)