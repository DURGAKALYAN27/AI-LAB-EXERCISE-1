from collections import deque

State = tuple[int, int, int, int, int, int]

def is_valid_state(M_s, C_s, M_g, C_g):
    if (0 <= M_s <= 3 and 0 <= C_s <= 3 and 0 <= M_g <= 3 and 0 <= C_g <= 3 and 
        (M_s == 0 or M_s >= C_s) and 
        (M_g == 0 or M_g >= C_g)):
        return True
    else:
        return False   
    
    
def get_possible_moves(M_s, C_s, B_s, M_g, C_g, B_g):
    moves = []
    if B_s == 1:
        new_positions = [
            (M_s - 2, C_s, 0, M_g + 2, C_g, 1),
            (M_s - 1, C_s, 0, M_g + 1, C_g, 1),
            (M_s, C_s - 2, 0, M_g, C_g + 2, 1),
            (M_s, C_s - 1, 0, M_g, C_g + 1, 1),
            (M_s - 1, C_s - 1, 0, M_g + 1, C_g + 1, 1)
        ] 
        
    else:
        new_positions = [
            (M_s + 2, C_s, 1, M_g - 2, C_g, 0),
            (M_s + 1, C_s, 1, M_g - 1, C_g, 0),
            (M_s, C_s + 2, 1, M_g, C_g - 2, 0),
            (M_s, C_s + 1, 1, M_g, C_g - 1, 0),
            (M_s + 1, C_s + 1, 1, M_g - 1, C_g - 1, 0)
        ]
        
    for state in new_positions:
        if is_valid_state(state[0], state[1], state[3], state[4]):
            moves.append(state)
            
    return moves


def missionaries_and_cannibals_bfs():
    initial_state: State = (3, 3, 1, 0, 0, 0)
    goal_state: State = (0, 0, 0, 3, 3, 1)
    
    queue = deque([(initial_state, [initial_state])])
    visited = set([initial_state])
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path
        
        M_s, C_s, B_s, M_g, C_g, B_g = current_state
        
        for move in get_possible_moves(M_s, C_s, B_s, M_g, C_g, B_g):
            if move not in visited:
                visited.add(move)
                queue.append((move, path + [move]))

    return []



def main():
    solution = missionaries_and_cannibals_bfs()
    if solution:
        for step in solution:
            M_s, C_s, B_s, M_g, C_g, B_g = step
            print(f"({M_s}, {C_s}, {B_s}, {M_g}, {C_g}, {B_g})")
        
    else:
        print("No solution found.")


if __name__  == "__main__":
    main()