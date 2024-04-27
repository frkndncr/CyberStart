points = [(2, 3), (5, 7), (8, 9), (10, 12)]

def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

min_distance = float('inf')
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        if distance < min_distance:
            min_distance = distance

print("Minimum Mesafe:", min_distance)
