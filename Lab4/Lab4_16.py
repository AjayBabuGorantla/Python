import time
import datetime
def catlan(n):
    if(n==0):
        return 1
    else:
        term = (2*(2*n - 1))/(n+1)
        return term*catlan(n-1)

print(catlan(3))
target_1=time.time()
time.perf_counter()
print(catlan(20))
print("Time")
print(float(time.time()-target_1))
target_2=time.time()
print(catlan(30))
print("Time")
print(float(time.time()-target_2))
target_3=time.time()
print(catlan(50))
print("Time")
print(float(time.time()-target_3))