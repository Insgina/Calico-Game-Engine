
from typing import List
from abc import ABC

class Transform:

    def __init__(self, x=0, y=0, width=0, height=0, scale_x=1, scale_y=1):
        

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale_x = scale_x
        self.scale_y = scale_y

    @property    
    def center(self):
        x = self.x + (self.width / 2)
        y = self.y + (self.height / 2)

    def change_position(self, x, y):
        self.x = x
        self.y = y
    
    def change_dimensions(self, width, height):
        self.width = width or self.width
        self.height = height or self.height

    def change_scale(self, sx,sy):
        self.scale_x = sx or self.scale_x
        self.scale_y = sy or self.scale_y

# Gameobject

class AbstractGameObject(ABC):

    def __init__(self, transform: Transform, tags: List(str) = None, name: str = None):

        self.__transform__: Transform = transform or Transform()

        self.__tags__: str = tags
        self.__name__: str = name
    
    @property    
    def transform(self):
        return self.__transform__

    @property
    def tags(self):
        return self.__tags__

    @property
    def name(self):
        return self.__name__

    def input(self):
        pass

    def update(self):
        pass

    def fixed_update(self):
        pass

    def render(self):
        pass
    
class gameobject(AbstractGameObject): 
        
     def __init__(self, transform: Transform, tags: List(str) = None, name: str = None):
        super().__init__(transform=transform, tags=tags, name=name)
        # on screen
        self.started = False

        # removed on screen
        self.destroyed = False

        # Timeline

        # Start -> input -> update -> fixed_update* -> render -> destroy 