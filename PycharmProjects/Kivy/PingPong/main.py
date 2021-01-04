from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongPaddle(Widget):
    pass


class PongBall(Widget):
    vel_x = NumericProperty(0)
    vel_y = NumericProperty(0)
    vel = ReferenceListProperty(vel_x, vel_y)

    def move(self):
        self.pos = Vector(*self.vel) + self.pos

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def on_touch_move(self, touch):
        if touch.x < self.width *1/4:
            self.player1.center_y = touch.y
        elif touch.x > self.width * 3/4:
            self.player2.center_y = touch.y
    def serve_ball(self):
        self.ball.vel = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        if self.ball.y < 0 or self.ball.y > self.height - 50:
            self.ball.vel_y *= -1

        if self.ball.x < 0 or self.ball.x > self.width - 50:
            self.ball.vel_x *= -1

        self.ball.move()

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

PongApp().run()