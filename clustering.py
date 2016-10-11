"""
Clusterings.
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def num_cluster(data, n_clusters=10):
    """
    Clustering into DataFrame or nd.array.

    Ex :
        df = np.ndarray([i for i in range(100)])
        num_cluster(data, 10)

    Return sample
    -------------
       labels  values
    0       1      31
    1       2    6453
    2       1    1053
    3       1    1614
    4       2    5119
    5       1     542
    ...

    Parameters
    ----------
    data : nd.array
        Array data to clustering
    n_cluster :
        Number of clustering.
    """
    k_model = KMeans(n_clusters=n_clusters).fit(data)

    labels = []
    vals = []
    for label, v in zip(k_model.labels_, data):
        labels.append(label)
        vals.append(v[0])

    return pd.DataFrame({"labels": labels, "values": vals})

if __name__ == '__main__':
    import random_data as rd
    data = rd.random_int(10, 9999, "np")
    print(num_cluster(data, 10))
