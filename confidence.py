import numpy as np
import scipy.stats
import statistics
import mean
import math
import bootstrap
import jackknife as jk

# Z scores are at -1.645->1.645, -1.96->1.96, -2.756->2.576
def confidence_numpy(data, confidence):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

def confidence_arithmetic(data, confidence):
    a_mean = mean.arithmetic(data)
    std_dev = statistics.stdev(data, a_mean)/ math.sqrt(len(data))
    low_val_90= (std_dev*-1.645 + a_mean)
    hi_val_90 = (std_dev*1.645  + a_mean)
    low_val_95 = (std_dev * -1.96 + a_mean)
    hi_val_95 = (std_dev * 1.96 + a_mean)
    low_val_99 = (std_dev * -2.576 + a_mean)
    hi_val_99 = (std_dev * 2.576 + a_mean)
    return a_mean, std_dev, [low_val_90, hi_val_90], [low_val_95, hi_val_95],[low_val_99, hi_val_99]

def confidence_harmonic(data, confidence):
    h_mean = mean.harmonic(data)
    std_dev = statistics.stdev(data, h_mean) / math.sqrt(len(data))
    low_val_90 = (std_dev * -1.645 + h_mean)
    hi_val_90 = (std_dev * 1.645 + h_mean)
    low_val_95 = (std_dev * -1.96 + h_mean)
    hi_val_95 = (std_dev * 1.96 + h_mean)
    low_val_99 = (std_dev * -2.576 + h_mean)
    hi_val_99 = (std_dev * 2.576 + h_mean)
    return h_mean, std_dev, [low_val_90, hi_val_90], [low_val_95, hi_val_95], [low_val_99, hi_val_99]

def confidence_jackknife(data, confidence):

    #These are the precomputed values of the mean and standard deviation, can derive them using the below function
    # calls for any dataset.
    # j_mean = 162.52337292327385
    # std_dev = 385.8849347861505 / math.sqrt(len(data))

    #Generic
    description = jk.jackknife(data)
    j_mean = description[0]
    std_dev = description[1] / math.sqrt(len(data)) #It should be noted the function returns sigma, NOT the

    # normalization and that is done here
    low_val_90 = (std_dev * -1.645 + j_mean)
    hi_val_90 = (std_dev * 1.645 + j_mean)
    low_val_95 = (std_dev * -1.96 + j_mean)
    hi_val_95 = (std_dev * 1.96 + j_mean)
    low_val_99 = (std_dev * -2.576 + j_mean)
    hi_val_99 = (std_dev * 2.576 + j_mean)
    return j_mean, std_dev, [low_val_90, hi_val_90], [low_val_95, hi_val_95], [low_val_99, hi_val_99]

def confidence_bootstrap(data,confidence):
    return bootstrap.bootstrap_selection(data, confidence);