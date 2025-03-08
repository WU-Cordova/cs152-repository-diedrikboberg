from time import sleep
from projects.project2.grid import Grid
from projects.project2.khibit import KBHit


class Gamecontroller:
    def __init__(self, grid: Grid):
        print("From the constructor.")
        self.grid = Grid(80,60)
        self.hist = []

    def run(self, n):
        keyboard = KBHit()
        count_gen = 0
        while True:
            
            if keyboard.kbhit():
                c = keyboard.getch()

                if c == "q":
                    print("QUIT")
                    break

                if c == "c":
                    print("Moving onp")
                    continue
                
                if c == "p":
                    input("Pause:")
                    c = keyboard.getch()
                    if c == "p":
                        continue
            #sleep(0.5)
            
            self.hist.append(self.grid)
            count_gen += 1
            self.grid = self.grid.new_gen()

            print("---------------------")
            print("Generation:",count_gen)
            self.grid.display()
            #print("------------------")

            if self.grid == self.hist[-1]:
                print("No more evolution.", count_gen)
                break

            if len(self.hist) > 2:    
                if self.grid == self.hist[-2]:
                    print("No more evolution.", count_gen)
                    break
            
            if len(self.hist) > 3:
                self.hist.pop(0)