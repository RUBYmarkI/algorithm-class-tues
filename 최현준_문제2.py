# 과제 2

def knapSack_dp(W, wt, val, n):
    # 1. DP 테이블 초기화 : (n+1) X (W+1)
    A = []
    for i in range(n + 1):
        row = []
        for w in range(W + 1):
            row.append(0)
        A.append(row)

    # 2. DP 테이블 채우기 (Bottom-up)
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if w < wt[i-1]:
                A[i][w] = A[i-1][w]
            else:
                valWith = val[i-1] + A[i-1][w - wt[i-1]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)

    return A[n][W], A


items = [
    ("노트북", 3, 12),
    ("카메라", 1, 10),
    ("책", 2, 6),
    ("옷", 2, 7),
    ("휴대용 충전기", 1, 4)
]


names = [item[0] for item in items]
wt = [item[1] for item in items]
val = [item[2] for item in items]
n = len(items)

W = int(input("배낭 용량을 입력 하세요 : "))


max_value, A = knapSack_dp(W, wt, val, n)

print("\n최대 만족도:", max_value)


selected = []
w = W

for i in range(n, 0, -1):
    if A[i][w] != A[i-1][w]:
        selected.append(names[i-1])
        w -= wt[i-1]

selected.reverse()

print("선택된 물건:", selected)