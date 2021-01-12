import numpy as np

def detect_outliers_zscore(data):
    outliers = []

    threshold = 3
    mean = np.mean(data)
    sd = np.stddev(data)

    for i in data:
        zscore = (i - mean)/sd
        if np.abs(zscore) > threshold:
            outliers.append(i)
    return(outliers)

def outlier_detect_iqr(data):
    outliers = []
    data = sorted(data)
    q1, q3 = np.percentile(data, [25,75])
    iqr = q3 - q1

    lb = q1 - 1.5 * iqr
    ub = q3 + 1.5 * iqr

    for i in data:
        if (i < lb or i > ub):
            outliers.append(i)

    return(outliers)



    
