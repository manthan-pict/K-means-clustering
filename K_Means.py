import numpy as np
import matplotlib.pyplot as plt
import scipy.io

# Input data extraction from MAt file
AllSamples = np.array(scipy.io.loadmat('C:/Users/magraw12/PycharmProjects/pythonProject/AllSamples.mat',
                                       variable_names='AllSamples').get('AllSamples'))


# Methos to plot graph on the given arrays on x and y axis
def plot_graph(x_axis_val, y_axis_val, name_of_graph):
    plt.plot(x_axis_val, y_axis_val)
    plt.xlabel('Number of Clusters --->')
    plt.ylabel('Objective Function val --->')
    plt.title(name_of_graph)
    plt.show()


# method to find Euclidean distance between two points
def euclidean_distance(point1, point2):
    return np.linalg.norm(point1 - point2)


# Method to implement the K means using strategy one which is choosing initial clusters randomly.
def k_means_strategy_1():
    avg_passes = 0
    distance_distribution_sum = []
    cluster_numbers = []
    cluster_number = 2
    while cluster_number < 11:
        center = np.array([[0 for x in range(2)] for y in range(cluster_number)], dtype=np.float64)
        center_new = np.array([[0 for x in range(2)] for y in range(cluster_number)], dtype=np.float64)
        numbers = np.random.choice(AllSamples.shape[0], cluster_number, replace=False)
        i = 0
        while i < cluster_number:
            center[i] = AllSamples[numbers[i]]
            i += 1

        z = 0
        while z < 2000:
            center_new = min_distance(center, AllSamples, cluster_number)
            if np.array_equal(center, center_new):
                break
            center = center_new
            z += 1

        avg_passes += z
        distance_distribution_sum.append(min_sqr_error_function(center_new, AllSamples, cluster_number))
        cluster_numbers.append(cluster_number)
        cluster_number += 1

    print("Average number of passes it took to converge for all the value of K", avg_passes / 9)
    plot_graph(cluster_numbers, distance_distribution_sum, 'K means plot Strategy 1')


# Method implement the logic to calculate the distance between input and given cluster centers.
# Finally return the new clusters with mean of the newly formed clusters.
def min_distance(center, samples, num_of_cluster):
    new_clust = [[0 for x in range(3)] for y in range(num_of_cluster)]
    new_clust_center = np.array(center)
    count = 0
    for x in samples:
        min_dis = 100000000
        clust_no = 0
        i = 0
        x_cor = 0
        y_cor = 0
        for y in center:
            dis = euclidean_distance(y, x)

            if dis < min_dis:
                min_dis = dis
                x_cor = x[0]
                y_cor = x[1]
                clust_no = i
            i += 1

        new_clust[clust_no][0] += x_cor
        new_clust[clust_no][1] += y_cor
        new_clust[clust_no][2] += 1

    z = 0
    for j in new_clust:
        new_clust_center[z][0] = j[0] / j[2]
        new_clust_center[z][1] = j[1] / j[2]
        z += 1

    return new_clust_center


# Calculation of objective function
def min_sqr_error_function(center, samples, num_of_clusters):
    new_clust = [0 for y in range(num_of_clusters)]
    mean_distance = 0
    for x in samples:
        min = 100000000
        clust_no = 0
        i = 0
        for y in center:

            dis = euclidean_distance(y, x)
            if dis < min:
                min = dis
                clust_no = i
            i += 1

        new_clust[clust_no] += np.power(min, 2)
    for j in new_clust:
        mean_distance += j

    return mean_distance


# Method impliments logic to find the cluster centers using strategy 2.
def identify_cluster_centers(num_centers, sample):
    sample = np.array(sample)
    cluster_centers = np.array([[0 for x in range(2)] for y in range(num_centers)], dtype=np.float64)
    cluster_centers[0] = sample[np.random.choice(sample.shape[0], 1)]
    i = 1
    while i < num_centers:
        max_val = 0
        x_cor = 0
        y_cor = 0
        for x in sample:
            sum = 0
            temp = 0
            while temp < i:
                sum += euclidean_distance(x, cluster_centers[temp])
                temp += 1
            sum /= i
            if sum > max_val:
                max_val = sum
                x_cor = x[0]
                y_cor = x[1]
        cluster_centers[i][0] = x_cor
        cluster_centers[i][1] = y_cor
        val_to_delete = np.where(sample == cluster_centers[i])
        sample = np.array(np.delete(sample, val_to_delete[0][0], 0))

        i += 1
    return cluster_centers


# Method impliment the logic to combine the identify_cluster_centers() with min_distance() for all the value of k.
def k_means_strategy_2():
    avg_of_passes = 0
    distance_distribution_sum = []
    cluster_numbers = []
    itr = 2
    while itr < 11:
        center = identify_cluster_centers(itr, AllSamples)
        z = 0
        while z < 2000:
            center_new = min_distance(center, AllSamples, itr)
            # print(center_new)
            if np.array_equal(center, center_new):
                break
            center = center_new
            z += 1

        avg_of_passes += z
        distance_distribution_sum.append(min_sqr_error_function(center, AllSamples, itr))
        cluster_numbers.append(itr)
        itr += 1
    print(avg_of_passes / 9)
    plot_graph(cluster_numbers, distance_distribution_sum, 'K means plot strategy 2')


# Final Calls to method
print("Strategy 1 pass 1")
k_means_strategy_1()
print("Strategy 2 pass 2")
k_means_strategy_1()
print("Strategy 2 pass 1")
k_means_strategy_2()
print("Strategy 2 pass 2")
k_means_strategy_2()
