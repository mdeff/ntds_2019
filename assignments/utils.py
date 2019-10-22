from mnist import MNIST
import numpy as np

def __subsample_mnist(images, labels, n):

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
    mndata = MNIST(path)
    images, labels = mndata.load_testing()

    classes = np.unique(labels)
    n_clusters_mnist = len(classes)
    keep_per_class = 300
    n = keep_per_class * len(classes)
    images = np.array(images)
    labels = np.array(labels)
    
    return __subsample_mnist(images, labels, n)