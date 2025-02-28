import pygame
import time
from maze import Maze
from collections import deque

def solve_maze(maze):
    stack = deque()
    visited = set()
    
    # defining the player positioning
    start_pos = maze.get_init_pos_player()
    stack.append(start_pos)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    
    running = True
    while stack and running:
        x, y = stack.pop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return False
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        if maze.find_prize((x, y)):
            print("Prêmio encontrado!")
            return True
        
        if maze.is_free((x, y)):
            maze.mov_player((x, y))
            maze.update_display()  # refresh the screen with the new player state
            time.sleep(0.1)  # delay aplied to better visualization of the path taken
        
        for dx, dy in directions:
            next_pos = (x + dx, y + dy)
            if next_pos not in visited and maze.is_free(next_pos):
                stack.append(next_pos)
    
    print("Prêmio não encontrado.")
    return False

# function to refresh the maze screen
def update_display(self):
    pygame.event.pump()  # keep the pygame window responsive
    pygame.display.flip()

Maze.update_display = update_display  # add the function to the maze class

# Execute the solution
txt_path = "labirinto1.txt"
maze = Maze()
maze.load_from_csv(txt_path)
maze.init_player()
maze.run()
solve_maze(maze)




