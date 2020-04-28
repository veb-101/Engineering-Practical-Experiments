import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


def euclideanDistance(centroid, datapoint):
    '''
    Description:{
        Calculates the Euclidean distance between a centroid and 
        a data point
    }

    inputs: {
        centroid: centroid position
        datapoint: a single datapoint whose distance from
            centroid is to be calculated
    }
    return: {
        [scalar] Distance between centroid and data
    }
    '''

    distance = np.sum(np.power(centroid - datapoint, 2))
    return np.sqrt(distance)


def calculateDistances(data, centroid):
    '''
    Description: {
        This function calculates distances between a 
        centroid and the dataset.
        Uses the euclideanDistance function
    }

    inputs: {
        centroid: centroid position
        data: dataset whose distance from a 
            centroid is to be calculated
    }

    return: {
        [list] distance of each datapoint from the centroid
    }
    '''

    dist = []
    for i in range(len(data)):
        point_dist_to_centroid = euclideanDistance(centroid, data[i])
        dist.append(point_dist_to_centroid)
    return dist


def distanceToCentroids(data, centroids):
    '''
    Description: {
        This function calculates distance of between all datapoints
        and the specified number of centroids.
        Uses calculateDistances function
    }

    inputs: {
        data: dataset
        centroids: list of list of initial or intermediary 
            centroids positions.
    }

    return: {
        [list of list] each row contains distance between the 
            datapoint and all centroids
    }
    '''

    data_dist_from_centroid = [[] for i in range(len(data))]

    for k in centroids:
        dist = calculateDistances(data, k)
        for x, y in enumerate(dist):
            data_dist_from_centroid[x].append(y)

    return data_dist_from_centroid


def getNewCentroid(data, distances, numOfCentroids, assigned_centroids=None):
    '''
    Description: {
        This functions assigns datapoints to each of
            the centroids and calculates new position for 
            all the centroids
    }

    inputs: {
        data: dataset
        distances: calculated distances between datapoints and centroids
        numOfCentroids: number of centroids initialized
    }

    return: {
        [list of list] new poistions of each centroid
    }
    '''

    assigned_centroids = [[] for _ in range(numOfCentroids)]

    # assignnig data point to centroids
    for i in range(data.shape[0]):
        min_index = np.argmin(distances[i])
        assigned_centroids[min_index].append(data[i])

    new_k = [np.array(i).mean(axis=0) for i in assigned_centroids]

    return new_k, assigned_centroids


# generating dataset

X = -2 * np.random.rand(150, 2)
X1 = 1 + 2 * np.random.rand(50, 2)
X2 = 3 + 2 * np.random.rand(50, 2)

X[50:100, :] = X1
X[100:150, :] = X2
print(X.shape)

plt.scatter(X[:, 0], X[:, 1], s=50, c="b")
plt.title("2-dimensional data")
plt.xlabel("X1")
plt.ylabel("X2")
plt.show()


# num_centroids = int(input("Number of centroids: "))
num_centroids = 2
centroids = []

# Initial centroids
num_dim = X.shape[1]

# dynamic
for i in range(num_centroids):
    k = [np.random.choice(X[:, z] + 1 * 2 * np.random.rand(X.shape[0]))
         for z in range(num_dim)]
    centroids.append(k)

print(centroids)

num_iterations = 4

# centroids = np.array([[-2, 3],
#                       [3, -2]])

colors = ["red", "green"]

for idx, centroid in enumerate(centroids, 1):
    plt.plot(centroid[0], centroid[1], marker="^",
             c=colors[idx - 1], markersize=12, label=f'k{idx}')


plt.scatter(X[:, 0], X[:, 1], c="k")

plt.title("$Initial$", fontsize=18)
plt.xlabel("X1", fontsize=15)
plt.ylabel("X2", fontsize=15, rotation=0)
plt.show()


distances = distanceToCentroids(X, centroids)
centroids, centroid_points = getNewCentroid(X, distances, num_centroids)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 9))

for i in range(num_iterations):
    plt.sca(axes[i // 2, i % 2])

    for idx, centroid in enumerate(centroids, 1):
        x1, x2 = [], []

        for a, b in centroid_points[idx - 1]:
            x1.append(a)
            x2.append(b)

        plt.plot(centroid[0], centroid[1], marker="^",
                 c=colors[idx - 1], markersize=12, label=f'k{idx}')
        plt.scatter(x1, x2, s=15, c=colors[idx - 1], label=f'Centroid: {idx}')

        plt.title(f"$Iteration: {i + 1}$", fontsize=15)

        if i in (0, 1):
            plt.xlabel("")
        else:
            plt.xlabel("X1", fontsize=15)

        if i in (1, 3):
            plt.ylabel("")
        else:
            plt.ylabel("X2", fontsize=15, rotation=0)
    plt.legend()

    distances = distanceToCentroids(X, centroids)
    centroids, centroid_points = getNewCentroid(X, distances, num_centroids)
plt.show()
