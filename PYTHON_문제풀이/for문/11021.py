T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print("Case #%d: %d"%(i+1, A+B))

    # %d(정수), %s(문자열), %f(실수)
    # 변수를 문자열과 함께 출력할 때 사용