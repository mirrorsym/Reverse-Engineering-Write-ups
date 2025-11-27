def find_shortest_path(start_index, end_index, rows, cols, allowed):

    def shortest_path(index, visited):
        
        if index == end_index:
            return [end_index]
        if index not in allowed:
            return False
        
        curr_visited = visited
        curr_visited.add(index)
        
        prev_indices = False
        
        if index + 1 not in visited and (index + 1) % cols != 0:
            curr = shortest_path(index+1, curr_visited)
            if curr:
                prev_indices = curr
        if index - 1 not in visited and index % cols != 0:
            curr = shortest_path(index-1, curr_visited)
            if curr:
                if not prev_indices or (prev_indices and len(curr) < len(prev_indices)):
                    prev_indices = curr
        if index + cols not in visited:
            curr = shortest_path(index+cols, curr_visited)
            if curr:
                if not prev_indices or (prev_indices and len(curr) < len(prev_indices)):
                    prev_indices = curr
        if index - cols not in visited:
            curr = shortest_path(index-cols, curr_visited)
            if curr:
                if not prev_indices or (prev_indices and len(curr) < len(prev_indices)):
                    prev_indices = curr
        
        if prev_indices:
            prev_indices.append(index)
        
        return prev_indices
    
    shortest_path_from_start = shortest_path(start_index, set())
    
    if not shortest_path_from_start:
        return "No path exists between the inputted indices"
    
    shortest_path_from_start = shortest_path_from_start[::-1]
    
    # delete this block of code and return shortest_path_from start
    # if only the indices traversed are needed.
    
    moves = []
    
    for i in range(1,len(shortest_path_from_start)):
        diff = shortest_path_from_start[i]-shortest_path_from_start[i-1]
        if diff == 1:
            moves.append('R')
        elif diff == -1:
            moves.append('L')
        elif diff == cols:
            moves.append('D')
        else:
            moves.append('U')
            
    moves = "".join(moves)
    
    return moves

if __name__ == "__main__":

  allowed = {0, 1, 41, 42, 43, 44, 45, 46, 48, 58, 62, 67, 70, 74, 75, 76, 77, 78, 82, 85, 88, 89, 90, 91, 92, 94, 95, 96, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 114, 118, 122, 124, 125, 128, 134, 136, 138, 140, 143, 146, 149, 154, 155, 156, 161, 162, 165, 166, 167, 168, 169, 170, 171, 172, 174, 178, 186, 188, 189, 190, 191, 194, 198, 202, 204, 205, 208, 210, 212, 213, 214, 215, 216, 217, 218, 219, 221, 224, 229, 231, 232, 234, 236, 238, 241, 242, 250, 255, 261, 263, 264, 265, 267, 268, 269, 271, 274, 275, 276, 277, 278, 282, 284, 286, 288, 290, 291, 292, 293, 294, 295, 298, 301, 302, 303, 305, 306, 307, 313, 314, 316, 318, 321, 322, 323, 324, 326, 327, 328, 329, 330, 332, 335, 336, 338, 339, 340, 341, 343, 345, 347, 349, 350, 351, 353, 356, 358, 385}

  flag = find_shortest_path(1, 385, 10, 40, allowed)
  print(f"Flag: {flag}")
  print(f"Flag has {len(flag)} characters.")
