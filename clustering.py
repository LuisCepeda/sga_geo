import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


def perform_clustering(data, eps=0.01, min_samples=2):

    coords = np.array(data)
    
    coords = StandardScaler().fit_transform(coords)

    db = DBSCAN(eps=eps, min_samples=min_samples).fit(coords)

    labels = db.labels_

    return labels.tolist()
