class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    pass

class Mammals(Animals):
    pass

class Giraffes(Mammals):
    pass

reginald = Giraffes()

def this_is_a_normal_function():
    print('I am a normal function')
class ThisIsMySillyClass:
    def this_is_a_class_function():
        print('I am a class function')
    def this_is_also_a_class_function():
        print('I am also a class function. See?')
class Animals(Animate):
    def breathe(self):
        pass
    def move(self):
        pass
    def eat_food(self):
        pass

class Mammals(Animals):
    def feed_young_with_milk(self):
        pass

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        pass

reginald = Giraffes()

reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()

harold = Giraffes()
harold.move
class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves')
reginald = Giraffes()
harold = Giraffes()
reginald.move()
harold.eat_leaves_from_trees()

import turtle
andy = turtle.Pen()
emily = turtle.Pen()
andy.forward(50)
andy.right(90)
andy.forward(20)
emily.left(90)
emily.forward(100)
luke = turtle.Pen()
luke.left(180)
luke.forward(80)
kate = turtle.Pen()
for i in range(2):
    kate.left(90)
    kate.forward(100)
    kate.left(90)
    kate.forward(80)
reginald = Giraffes()
reginald.move()
reginald = Giraffes()
reginald.breathe()
reginald.eat_food()
reginald.feed_young_with_milk()
reginald.move()
class Giraffes(Mammals):
    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat_food()
    def eat_leaves_from_trees(self):
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()
reginald = Giraffes()
reginald.dance_a_jig()

class Giraffes:
    def __init__(self, spots):
        self.giraffe_spots = spots
ozwald = Giraffes(100)
gertrude = Giraffes(150)
print(ozwald.giraffe_spots)
print(gertrude.giraffe_spots)
class Animals:
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating_food')
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')
class Giraffes(Mammals):
    def left_foot_forward(self):
        print('left foot forward')
    def left_foot_back(self):
        print('left foot back')
    def right_foot_forward(self):
        print('right foot forward')
    def right_foot_back(self):
        print('right foot back')
    def left_foot_back(self):
        print('left foot back')
    def right_foot_back(self):
        print('right foot back')
    def right_foot_forward(self):
        print('right foot forward')
    def left_foot_forward(self):
        print('left foot forward')
    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.left_foot_forward()
reginald = Giraffes()
reginald.dance()
andy.reset()
emily.reset()
kate.reset()
luke.reset()
import turtle
andy = turtle.Pen()
emily = turtle.Pen()
luke = turtle.Pen()
katy = turtle.Pen()
andy.forward(150)
andy.left(90)
andy.forward(50)
andy.right(90)
andy.forward(25)
emily.forward(150)
emily.right(90)
emily.forward(50)
emily.left(90)
emily.forward(25)
luke.forward(125)
luke.left(90)
luke.forward(75)
luke.right(90)
luke.forward(60)
katy.forward(125)
katy.right(90)
katy.forward(75)
katy.left(90)
katy.forward(60)
