from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.vector import Vector
from random import randint
from PongBall import PongBall
from PongPaddle import PongPaddle


class PongGame(Widget):
    
    ball = ObjectProperty(None)
    player_1 = ObjectProperty(None)
    player_2 = ObjectProperty(None)
    
    
    def serve_ball(self, vel):
        self.ball.center = self.center
        angle = randint(0, 45)
        angle *= 1 if randint(0,1)%2 == 0 else -1
        self.ball.velocity = Vector(*vel).rotate(angle)
    
    
    def on_touch_move(self, touch):
        
        
        def update_position(position, player):
            
            if position >= player.size[1]/2 \
                    and position <= self.top-player.size[1]/2:
                player.center_y = position
        
        
        if touch.x < self.width/3:
            update_position(touch.y, self.player_1)
        
        elif touch.x > (self.width*2)/3:
            update_position(touch.y, self.player_2)
    
    
    def update(self, dt):
        self.ball.move()
        self.player_1.bounce_ball(self.ball)
        self.player_2.bounce_ball(self.ball)
        
        
        def update_states(player, velocity):
            player.score += 1
            self.serve_ball(velocity)
        
        
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        
        if self.ball.x > self.width:
            update_states(self.player_1, (-10, 0))
        
        elif self.ball.x < self.x:
            update_states(self.player_2, (10, 0))