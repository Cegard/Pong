from kivy.app import App
from kivy.clock import Clock
from PongGame import PongGame, randint

class PongApp(App):
    
    
    def build(self):
        game = PongGame()
        direction_x = 1 if randint(0, 1)%2 == 0 else -1
        game.serve_ball(vel=(direction_x*10, 0))
        Clock.schedule_interval(game.update, 1/60)
        return game