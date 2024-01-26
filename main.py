#ulysse doyon

import arcade
import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

#classe objet balle
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = random.randint(-7,7)
        self.change_y = random.randint(-7,7)
        self.size = random.randint(15,30)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

#mur balle
    def update(self):
            ball.x += ball.change_x
            ball.y += ball.change_y
            if ball.x < ball.size:
                ball.change_x *= -1
            if ball.y < ball.size:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - ball.size:
                ball.change_x *= -1
            if ball.y > SCREEN_HEIGHT - ball.size:
                ball.change_y *= -1

#faire balle
    def draw(self):
        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.color)


#classe objet rectangle
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = random.randint(15,30)
        self.height = random.randint(30,60)
        self.angle = 0
        self.change_x = random.randint(-7,7)
        self.change_y = random.randint(-7,7)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

#mur rectangle
    def update(self):
        for rectangle in self.rectangle_list:
            rectangle.x += rectangle.change_x
            rectangle.y += rectangle.change_y
            if rectangle.x < rectangle.width:
                rectangle.change_x *= -1
            if rectangle.y < rectangle.height:
                rectangle.change_y *= -1
            if rectangle.x > SCREEN_WIDTH - rectangle.width:
                rectangle.change_x *= -1
            if rectangle.y > SCREEN_HEIGHT - rectangle.height:
                rectangle.change_y *= -1
#faire rectangle
    def draw(self):
        for rectangle in self.rectangle_list:
            arcade.draw_rectangle_filled(rectangle.x, rectangle.y, rectangle.width, rectangle.height, rectangle.color, rectangle.angle)


#classe window
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1",)
        self.ball_list = []

        self.rectangle_list = []

#fond d'écran
    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

#faire les objets
    def on_draw(self):
        arcade.start_render()
        for i in self.ball_list:
            i.draw()
        for i in self.rectangle_list:
            i.draw()

#changement de direction "mur"
    def on_update(self, delta_time):
        for i in self.ball_list:
            i.update()
        for i in self.rectangle_list:
            i.update()

# faire les objets sur la souris
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            ball = Ball(x,y)
            self.ball_list.append(ball)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle = Rectangle(x,y)
            self.rectangle_list.append(rectangle)

def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()

if __name__ == "__main__":
   main()