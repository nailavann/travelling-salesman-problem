import numpy as np

class DistanceClass:
    @staticmethod
    def distancesCreate():
        np.random.seed(42)  # Sabit bir rastgelelik için seed belirlenir

        num_cities = 10

        distances = np.zeros((num_cities, num_cities), dtype=int)  # Mesafe matrisi oluşturulur, başlangıçta tüm değerler sıfır olarak atanır

        for i in range(num_cities):
            for j in range(i+1, num_cities):  # i'den sonraki şehirler arasındaki mesafeleri oluştur
                if i != j:
                    distance = np.random.randint(1, 1001)  # Rastgele mesafe oluştur
                    distances[i, j] = distance
                    distances[j, i] = distance  # Her iki yönde de mesafeyi atayarak tutarlılık sağla
        print(distances)
        return distances
