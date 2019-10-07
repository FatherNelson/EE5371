import mean as m
import math

DEBUG = False

def jackknife(data):
    ret = []
    sum = 0
    length = len(data)-1
    if DEBUG:
        print("\n")
    for i in data:
        sum = 0
        for j in data:
            if i != j:
                # print(j)
                sum = sum + 1/j
                # print(length/sum)
            else:
                sum = sum + 0
                if DEBUG:
                    if sum != 0:
                        print(length/sum)
                    else:
                        print(0)
        ret.append(length/sum)
        if DEBUG:
            print("\n")
    mean = m.arithmetic(ret)
    sigma = jackknife_std_dev(ret, m.arithmetic(ret))
    # sigma = jackknife_std_dev(data, arithmetic(ret))
    return mean, sigma

def jackknife_std_dev(data, mean):
    sum = 0
    for x in data:
        sum = sum + (x-mean)**2
        # print(sum)
    prod = sum * (len(data)-1)
    return math.sqrt(prod);