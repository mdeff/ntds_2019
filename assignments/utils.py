from sklearn.datasets import fetch_openml
import numpy as np


def _subsample_mnist(images, labels, n):

    indices_to_keep = np.array([], dtype=np.int)
    classes = np.unique(labels)
    n_classes = len(classes)
    keep_by_class = int(n / n_classes)
    for i in range(10):
        if i in classes:
            belongs_to_class_i = np.where(labels==i)[0]
            indices_to_keep = np.append(indices_to_keep, belongs_to_class_i[:keep_by_class])

    X = images[indices_to_keep]
    Y = labels[indices_to_keep]
    return X, Y


def load_mnist(path='./data/mnist/'):
    # Load dataset

    mnist = fetch_openml('mnist_784')
    images =  mnist['data'][:10000]
    labels = np.array(list(map(int, mnist['target'][:10000])))

    classes = np.unique(labels)
    n_clusters_mnist = len(classes)
    keep_per_class = 300
    n = keep_per_class * len(classes)
    images = np.array(images)
    labels = np.array(labels)

    return _subsample_mnist(images, labels, n)
