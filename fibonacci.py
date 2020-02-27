import time
def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n ==1:
        return b
    else:
        for i in range(2, n+1):
            c = a+b
            a = b
            b = c
        return b


f = open("input.txt", "r")

request_id = 1
time_taken = []
request = []
result = []
for n in f:
    req = int(n)
    request.append(req)
    start = time.time()
    res = fibonacci(req)
    end = time.time()
    result.append(res)
    time_taken.append(end - start)

print(fibonacci(20))

out = open("fib_out.txt", "w")

for i in range(0, 100):
    out.write("%s %s %.3f %s\n"%(i,request[i], time_taken[i] * pow(10, 6), result[i]))

out.close()
