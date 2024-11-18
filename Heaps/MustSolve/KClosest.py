import heapq

# method 1
# def kClosestPointsToOrigin(points, k):
#     heap = []
#     for point in points:
#         distance = point[0] ** 2 + point[1] ** 2
#         heapq.heappush(heap, (distance, point))
#     return [heapq.heappop(heap)[1] for _ in range(k)]

# method 2
# def kClosestPointsToOrigin(points, k):
#     return heapq.nsmallest(k, points, lambda x: x[0] ** 2 + x[1] ** 2)

# nlogn without inbuilt heap, without lambda function
def kClosestPointsToOrigin(points, k):
    points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
    return points[:k]



print(kClosestPointsToOrigin([[1, 3], [-2, 2]], 1)) # [[-2, 2]]S