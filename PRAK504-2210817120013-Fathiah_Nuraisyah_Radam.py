def reverse(a):
    x = 0
    while (int(a) != 0):
        b = int(a) % 10
        x = x * 10 + b
        a = int(a) / 10
    return x
A, B =input().split()
A = reverse(A)
B = reverse(B)
C = A + B
print(reverse(C))