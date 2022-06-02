class Point:
    def __init__(self,coord_x=0,coord_y=0):
        self.x=coord_x
        self.y=coord_y
    def move_to(self,new_x,new_y):
        self.x=new_x
        self.y=new_y
    def go_home(self):
        self.x=0
        self.y=0
    def print_point(self):
        print(f'точка находится в координатах ({self.x},{self.y}')
