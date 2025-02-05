def make_set(data):
    if data is None:
        return []
    unique_elements = []
    for item in data:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements


def is_set(data):
    if data is None:
        return False
    return len(make_set(data)) == len(data)  


def union(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []
    return make_set(setA + setB)


def intersection(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []
    return [item for item in setA if item in setB]

if __name__ == "__main__":
    print(make_set([1, 2, 3, 4, 4, 5]))
    print(is_set([1, 2, 3, 4, 5]))  
    print(is_set([5, 5])) 
    print(is_set([])) 
    print(is_set(None))  
    print(union([1, 2], [2, 3]))  
    print(union([], [2, 3]))  
    print(union([1, 1, 1], [2, 3]))  
    print(intersection([1, 2], [2, 3]))  
    print(intersection([], [2, 3]))  
    print(intersection([1, 1, 1], [2])) 
