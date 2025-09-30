import time

test_data = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

def factorial_iter(n):
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

def factorial_rec(n):
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)

def run_with_time(func, n):
    """함수를 실행하고 결과와 실행시간을 반환"""
    start = time.perf_counter()
    try:
        result = func(n)
    except RecursionError:
        result = "재귀 계산 실패 (RecursionError)"
    end = time.perf_counter()
    return result, end - start

def handle_single_case(n):
    iter_result, iter_time = run_with_time(factorial_iter, n)
    rec_result, rec_time = run_with_time(factorial_rec, n)
    
    print(f"\n=== n = {n} ===")
    print(f"[반복] 결과: {iter_result} (시간: {iter_time:.6f}초)")
    print(f"[재귀] 결과: {rec_result} (시간: {rec_time:.6f}초)")
    if isinstance(iter_result, int) and isinstance(rec_result, int):
        print(f"결과 일치 여부: {'일치' if iter_result == rec_result else '불일치'}")

if __name__ == "__main__":
    while True:
        print("\n=============== Factorial Tester ===============")
        print("1) 반복법으로 n! 계산")
        print("2) 재귀로 n! 계산")
        print("3) 두 방식 모두 계산 후 결과/시간 비교")
        print("4) 준비된 테스트 데이터 일괄 실행")
        print("q) 종료")
        print("------------------------------------------------")
        
        p = input("\n선택 : ").strip()
        
        if p == "1":
            n = int(input("\nn값을 입력하세요: ").strip())
            result, elapsed = run_with_time(factorial_iter, n)
            print(f"반복문 기반: {result} (시간: {elapsed:.6f}초)")

        elif p == "2":
            n = int(input("\nn값을 입력하세요: ").strip())
            result, elapsed = run_with_time(factorial_rec, n)
            print(f"재귀 기반: {result} (시간: {elapsed:.6f}초)")

        elif p == "3":
            n = int(input("\nn값을 입력하세요: ").strip())
            handle_single_case(n)

        elif p == "4":
            print("\n[테스트 데이터 일괄 실행 시작]")
            for n in test_data:
                handle_single_case(n)

        elif p == "q":
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("올바른 값을 입력해주세요.")