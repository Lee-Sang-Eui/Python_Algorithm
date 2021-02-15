A = int(input())
B = list(input())
A1= A * int(B[2])
A2= A * int(B[1])
A3= A * int(B[0])
result = (A1 + (A2*10) + (A3*100))
print(A1, A2, A3, result)

