import time
def factorial(n):
    if (n == 1 or n == 0):
        return 1
    fact = 1;
    for i in range(2, n+1):
        fact = fact * i

    return fact


f = open("input.txt", "r")

request_id = 1
time_taken = []
request = []
result = []
for n in f:
    req = int(n)
    request.append(req)
    start = time.time()
    res = factorial(req)
    end = time.time()
    result.append(res)
    time_taken.append(end - start)


out = open("fact_out.txt", "w")

for i in range(0, 100):
    out.write("%s %s %.3f %s\n"%(i,request[i], time_taken[i] * pow(10, 6), result[i]))

out.close()
