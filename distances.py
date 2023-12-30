import numpy as np

class DistanceClass:
    @staticmethod
    def distancesCreate():
        np.random.seed(42)

        num_cities = 10

        distances = np.zeros((num_cities, num_cities), dtype=int)

        for i in range(num_cities):
            for j in range(i+1, num_cities): 
                if i != j:
                    distance = np.random.randint(1, 1001) 
                    distances[i, j] = distance
                    distances[j, i] = distance
        print(distances)
        return distances
