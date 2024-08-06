import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Create the dataset
x = [2, 15, 18, 56, 10, 82, 12, 9]
y = [100, 78, 3, 1, 16, 25, 24, 29, 21, 21]

data = list(zip(x, y))

# Perform hierarchical clustering
linkage_data = linkage(data, method='ward', metric='euclidean')

# Create the dendrogram
dendrogram(linkage_data)

# Display the dendrogram
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample index')
plt.ylabel('Distance')
plt.show()