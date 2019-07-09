import turtle
import math
import os
import yaml
import random


class Drawings:

    def __init__(self):
        self.__configurate__()
        graphics = turtle.Turtle()
        graphics.radians()
        graphics.setheading(math.pi / 2)
        graphics.speed(10)
        graphics.setposition(0,-400)
        graphics.clear()
        self.graphics = graphics
        self.tree_draw(self.length)

    def __configurate__(self):
        configs = ConfigLoader().config
        self.divisor = configs.get('divisor')
        self.length = configs.get('length')
        self.cutoff = configs.get('cutoff')
        self.branches = configs.get('branches')
        self.randomize_divisor = configs.get('randomize_divisor')
        self.randomize_angle = configs.get('randomize_angle')

    def tree_draw(self, length):

        if length < self.cutoff:
            return
        self.graphics.forward(length)
        direction = self.graphics.heading()
        position = self.graphics.pos()
        af = 1
        if(self.randomize_angle):
            af = random.random()/2 + .75
        self.graphics.setheading(self.graphics.heading() + af * math.pi * 3/4)
        for i in range(1,self.branches+1):
            if(self.randomize_angle):
                af = random.random()/2 + .75
            divisor = self.divisor
            if(self.randomize_divisor):
                divisor = random.random()*3 + 2
            self.graphics.setheading(self.graphics.heading() - af * 1.5*math.pi/(self.branches+1))
            self.tree_draw(length / (divisor * 3.8))
            self.tree_draw(length / (divisor * 2.5))
            self.tree_draw(length/divisor)
            self.graphics.setposition(position)
            i = i + 1
        self.graphics.setheading(direction)
        self.graphics.setposition(position)


class ConfigLoader:

    def __init__(self):
        config_path = os.getcwd() + "/config.yml"
        self.config = yaml.load(open(config_path))

    def get_config(self):
        return self.config

drawings = Drawings()