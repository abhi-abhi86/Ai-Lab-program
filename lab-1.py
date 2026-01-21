import random

# Distance matrix representing the cost between cities
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def total_distance(path):
    total = 0
    # Calculate distance from city i to i+1
    for i in range(len(path) - 1):
        total += distance_matrix[path[i]][path[i+1]]
    # Add distance from last city back to the first city
    total += distance_matrix[path[-1]][path[0]]
    return total

def hill_climber_tsp(num_cities, max_iterations=10000):
    # Start with a random path
    current_path = list(range(num_cities))
    random.shuffle(current_path)
    
    current_distance = total_distance(current_path)
    
    for _ in range(max_iterations):
        # Create a neighbor by swapping two random cities
        neighbor_path = current_path.copy()
        i, j = random.sample(range(num_cities), 2)
        neighbor_path[i], neighbor_path[j] = neighbor_path[j], neighbor_path[i]
        
        neighbor_distance = total_distance(neighbor_path)
        
        # If neighbor is better, move to that state
        if neighbor_distance < current_distance:
            current_path = neighbor_path
            current_distance = neighbor_distance
            
    return current_path, current_distance

if __name__ == "__main__":
    num_cities = 4
    solution_path, solution_dist = hill_climber_tsp(num_cities)
    print("Optimal Path:", solution_path)
    print("Total Distance:", solution_dist)