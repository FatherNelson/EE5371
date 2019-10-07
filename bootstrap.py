import random
import mean


DEBUG = False

def bootstrap_selection(data, k):
    length = len(data);
    #An array to store all the mean values that are collected, it will be k-long
    means = []
    #We want to select an array of length data, k times
    for x in range(0,k):
        selections = []
        for y in range (0,length):
            num = random.randint(0, length-1)
            if DEBUG:
                print(num)
            selections.append(data[num])
        if DEBUG:
            print(selections)
            print(mean.harmonic(selections))
        means.append(mean.harmonic(selections))
    sort = sorted(means)
    if DEBUG:
        print(sort)
    if k == 100:
        conf_int_90 = [sort[4], sort[94]]
        conf_int_95 = [(sort[1]+sort[2])/2, (sort[98]+sort[97])/2]
        conf_int_99 = [(sort[0]+sort[1])/2, (sort[98]+sort[99])/2]
    elif k == 500:
        conf_int_90 = [sort[24], sort[474]]
        conf_int_95 = [(sort[11] + sort[12]) / 2, (sort[486] + sort[487]) / 2]
        conf_int_99 = [(sort[1] + sort[2]) / 2, (sort[496] + sort[497]) / 2]
    elif k == 1000:
        conf_int_90 = [sort[49], sort[949]]
        conf_int_95 = [sort[24], sort[974]]
        conf_int_99 = [sort[4], sort[994]]

    intervals = [conf_int_90, conf_int_95, conf_int_99]
    return intervals

