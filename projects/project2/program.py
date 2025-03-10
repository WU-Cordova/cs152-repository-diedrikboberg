from projects.project2.gamecontroller import Gamecontroller
from projects.project2.grid import Grid

def main():
    
    grid = Grid(10,10)

    game_controller = Gamecontroller(grid)
    game_controller.run(100)




if __name__ == '__main__':
    main()

    