# 과제 1

def climb_stairs(n):
    # DP 테이블 생성
    table = [0] * (n + 1)

    # 초기값 설정
    table[0] = 1
    table[1] = 1

    # Bottom-up 방식으로 테이블 채우기
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]


# 사용자 입력
n = int(input("계단의 개수를 입력하시오: "))

# 결과 출력
result = climb_stairs(n)
print(f"{n}개의 계단을 오르는 방법의 수는 {result}가지입니다.")