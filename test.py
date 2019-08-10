def array_is_complete_cycle(array):
    if len(array) == 0:
        return False
    index_visited = [False for i in array]
    current_index = 0
    while True:
       index_visited[current_index] = True
       current_index = (current_index + array[current_index]) % len(array)
       if index_visited[current_index]:
            break
    return False if False in index_visited else True


A = [2,2,-1]
print(array_is_complete_cycle(A))