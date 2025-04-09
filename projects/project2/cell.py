class Cell:
    def __init__(self,is_alive: bool = False):
        self._is_alive = is_alive
        

    def is_alive(self) -> bool:
        return self._is_alive
    
    def set_alive(self, life_status):
        self._is_alive = life_status

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return False
        
        return self._is_alive == other._is_alive


    def __str__(self):
        if self._is_alive:
            return "🦠"
        
        else:
            return "💀"