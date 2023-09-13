import matplotlib.pyplot as plt
import numpy as np

def plot_heatmap(data):
    plt.imshow(data, cmap='hot', interpolation='nearest')
    plt.colorbar(label='Temperature')
    plt.title('Temperature Distribution')
    plt.xlabel('X(m)')
    plt.ylabel('Y(m)')
    plt.show()

def calculate_temperature(N, M, sensors):
    # 결과를 담을 2D 리스트 초기화
    result = [[0 for _ in range(M)] for _ in range(N)]
    
    # 각 격자의 온도 계산
    for i in range(N):
        for j in range(M):
            total_weight = 0
            total_temp = 0
            for sensor in sensors:
                x, y, temp = sensor
                # 유클리드 거리 계산
                distance = ((x - i)**2 + (y - j)**2)**0.5
                # 거리의 역수를 가중치로 사용
                weight = 1 / distance if distance != 0 else float('inf')
                total_temp += temp * weight
                total_weight += weight
            
            # 가중 평균 온도 계산
            result[i][j] = total_temp / total_weight
    
    # 센서의 온도 값을 직접 할당
    for sensor in sensors:
        x, y, temp = sensor
        result[x][y] = temp
    
    return result

N, M = 15, 15  # 예시
sensors = [(3, 2, 30), (5, 14, 22), (5, 2, 20), (14, 13, 20), (14, 2, 25)]  # 위치 (x, y)와 온도

grid_temperature = calculate_temperature(N, M, sensors)
for row in grid_temperature:
    print(row)



# Plotting the heatmap
plot_heatmap(grid_temperature)



