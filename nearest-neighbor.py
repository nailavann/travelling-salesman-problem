import time
import numpy as np
from distances import DistanceClass

def nearest_neighbor(distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    path = []
    path_length = 0
    
    # Başlangıç şehri seçimi
    current_city = np.random.randint(num_cities)
    path.append(current_city)
    visited[current_city] = True
    
    # Tüm şehirler ziyaret edilene kadar döngü
    while False in visited:
        nearest_city = None
        min_distance = np.inf
        
        # Şu anki şehirden en yakın ziyaret edilmemiş şehri bulma
        for city in range(num_cities):
            if not visited[city] and distances[current_city, city] < min_distance:
                nearest_city = city
                min_distance = distances[current_city, city]
        
        # En yakın şehri ziyaret edildi olarak işaretle, yola ekle ve toplam mesafeyi güncelle
        visited[nearest_city] = True
        path.append(nearest_city)
        path_length += min_distance
        current_city = nearest_city
    
    # Başlangıç şehrine geri dönüş
    path_length += distances[path[-1], path[0]]
    
    return path, path_length


start_time = time.time()

path,path_length = nearest_neighbor(DistanceClass.distancesCreate())

end_time = time.time()

print("En yakın komşu yol:", path)
print("En iyi yol uzunluğu:", path_length)
print("Gerçekleşme süresi: ",end_time - start_time)