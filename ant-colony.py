import numpy as np
import time
from distances import DistanceClass

# Feromonların başlangıç değerlerini belirleme
def initialize_pheromones(n_points):
    return np.ones((n_points, n_points))

# Feromonların güncellenmesi
def update_pheromones(pheromone, paths, path_lengths, Q, evaporation_rate, n_points):
    pheromone *= evaporation_rate  # Feromon buharlaşması
    
    for path, path_length in zip(paths, path_lengths):
        for i in range(n_points-1):
            pheromone[path[i], path[i+1]] += Q/path_length
        pheromone[path[-1], path[0]] += Q/path_length
    
    return pheromone

# En iyi yolun bulunması
def find_best_path(distances, pheromone, n_ants, n_iterations, alpha, beta, evaporation_rate, Q):
    n_points = len(distances)
    best_path = None
    best_path_length = np.inf
    
    for iteration in range(n_iterations):
        paths = []
        path_lengths = []
        
        # Karınca döngüsü
        for ant in range(n_ants):
            visited = [False]*n_points
            current_point = np.random.randint(n_points)
            visited[current_point] = True
            path = [current_point]
            path_length = 0
            
            # Tüm şehirler ziyaret edilene kadar döngü
            while False in visited:
                unvisited = np.where(np.logical_not(visited))[0]
                probabilities = np.zeros(len(unvisited))
                
                # Her bir ziyaret edilmemiş şehir için olasılığın hesaplanması
                for i, unvisited_point in enumerate(unvisited):
                    probabilities[i] = pheromone[current_point, unvisited_point]**alpha / distances[current_point, unvisited_point]**beta
                
                probabilities /= np.sum(probabilities)
                next_point = np.random.choice(unvisited, p=probabilities)
                path.append(next_point)
                path_length += distances[current_point, next_point]
                visited[next_point] = True
                current_point = next_point

            paths.append(path)
            path_lengths.append(path_length)
            
            if path_length < best_path_length:
                best_path = path
                best_path_length = path_length
        
        pheromone = update_pheromones(pheromone, paths, path_lengths, Q, evaporation_rate, n_points)
    
    return best_path, best_path_length

def ant_colony_optimization(distances, n_ants, n_iterations, alpha, beta, evaporation_rate, Q):
    n_points = len(distances)
    pheromone = initialize_pheromones(n_points)
    
    best_path, best_path_length = find_best_path(distances, pheromone, n_ants, n_iterations, alpha, beta, evaporation_rate, Q)
    
    return best_path, best_path_length


start_time = time.time()

best_path, best_path_length = ant_colony_optimization( DistanceClass.distancesCreate(), n_ants=20, n_iterations=150, alpha=1, beta=2, evaporation_rate=0.1, Q=1)

end_time = time.time()
print("En iyi yol:", best_path)
print("En iyi yol uzunluğu:", best_path_length)
print("Gerçekleşme süresi: ",end_time - start_time)