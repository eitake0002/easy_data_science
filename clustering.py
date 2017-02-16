"""
Cluster module.
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def cluster(data, n_clusters=10):
    """
    Clustering.

    Ex :
        df = np.ndarray([i for i in range(100)])
        cluster(data, 10)

    Parameters
    ----------
    data : nd.array
        np.ndarray
    n_cluster :
        Number of clustering.

    Returns
    -------
    Clustered data : DataFrame or Series.
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
    print(cluster(data, 3).sort(["labels"]))
