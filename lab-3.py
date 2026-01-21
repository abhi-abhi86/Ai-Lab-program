def depth_limited_search(nested_list, depth_limit, current_depth=1):
    if current_depth > depth_limit:
        return
    
    for element in nested_list:
        if isinstance(element, list):
            print(f"At depth {current_depth}: encountered nested list, diving deeper...")
            depth_limited_search(element, depth_limit, current_depth + 1)
        else:
            print(f"At depth {current_depth}: processing element: {element}")

if __name__ == "__main__":
    # Example nested structure
    nested_array = [1, [2, 3], [4, [5, 6]], 7, [8, 9]]
    limit = 2
    
    print(f"Starting Depth Limited Search with limit {limit}:")
    depth_limited_search(nested_array, limit)