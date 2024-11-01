import numpy as np
import time

def approx(f, a, b, n):
    return (np.array(list(map(lambda k: f( a + k * ( (b - a) / n) ), np.arange(1, n + 1)))).sum() 
            * ((b - a) / n))
    
if __name__=='__main__':
    start = time.time()
    f = lambda x: x**3 #함수 입력
    n_values=[2, 4, 6, 8, 10, 20, 40, 80]  #구간 개수 입력
    #n_values=range(1, 10**3)
    a=1.0  #적분 구간 아래 끝
    b=2.0  #적분 구간 위 끝
    Int=15.0/4  #미적분의 기본 정리로 계산한 참값

    results = np.array(list(map(lambda n: approx(f, a, b, n), n_values))) #결과 구하기
    errors = results-(np.ones(len(results))*Int)
    print(results)
    print(errors)

    end = time.time()
    print(end - start)