import numpy as np
import time

def approx(f, a, b, n):
    h = (b - a) / n
    R = 0.0
    for k in range(1, n + 1):
        R += f(a + k * h)
    R = R * h
    return R

if __name__=='__main__':
    start = time.time()
    def f(x): return x**3  #함수 입력
    n_values=[2, 4, 6, 8, 10, 20, 40, 80]  #구간 개수 입력
    a=1.0  #적분 구간 아래 끝
    b=2.0  #적분 구간 위 끝
    Int=15.0/4  #미적분의 기본 정리로 계산한 참값
    for n in n_values:
        approx_result = approx(f, a, b, n)
        approx_error = abs(Int - approx_result)
        print(f'approx(f, {a}, {b}, {n}) = {approx_result}', f'Exact = {Int}', f'approx_error = {approx_error}', sep = '\n')
        print()
    end = time.time()
    print(end - start)