import time
import numpy as np
from distances import DistanceClass

def nearest_neighbor(distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    path = []
    path_length = 0
    
    current_city = np.random.randint(num_cities)
    path.append(current_city)
    visited[current_city] = True
    
    while False in visited:
        nearest_city = None
        min_distance = np.inf
        
        for city in range(num_cities):
            if not visited[city] and distances[current_city, city] < min_distance:
                nearest_city = city
                min_distance = distances[current_city, city]
        
        visited[nearest_city] = True
        path.append(nearest_city)
        path_length += min_distance
        current_city = nearest_city
    
    path_length += distances[path[-1], path[0]]
    
    return path, path_length


start_time = time.time()

path,path_length = nearest_neighbor(DistanceClass.distancesCreate())

end_time = time.time()

print("Best way:", path)
print("Best length:", path_length)
print("Time:  ",end_time - start_time)