# BOSS FIGHT: Nearest Neighbor Search
# Vector Databases work by comparing a query vector to thousands of stored vectors 
# and returning the "closest" match.
#
# Your Task: Implement find_nearest(query: list[float], database: list[list[float]]) -> list[float]
# Use Euclidean distance to find and return the exact vector in `database` that is closest to `query`.
# If the database is empty, return an empty list.

def euclidean_distance(vec_a: list[float], vec_b: list[float]) -> float:
    diff_sum = 0.0
    for i in range(len(vec_a)):
        diff_sum += (vec_a[i] - vec_b[i]) ** 2
    return diff_sum ** 0.5

def find_nearest(query: list[float], database: list[list[float]]) -> list[float]:
    # STUDENT_IMPLEMENTATION: Implement a linear scan to find the vector with minimum distance
    pass
