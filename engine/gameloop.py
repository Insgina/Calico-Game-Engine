from ast import Try
from .scene import Scene


class Gameloop:

    def __init__(self, limit_fps=60):
        self.limit_fps = limit_fps
    
    def __INIT__(self, canvas=None, window=None):
        self.__start_game_loop__()
    
    def _start_game_loop__(self):

        gameobjects = Scene.get_active_scene().get_game_objects()

        for go in gameobjects:
            go.start()

        # Game loop
        while True:
            
            gameobjects = Scene.get_active_scene().get_game_objects()

            for go in gameobjects:
                
                #start the game object
                if not item.started:
                    go.start()

                if go.destroyed:
                    Scene.get_active_scene().remove_game_objects(go)

                # handle input
                go.input()
                
                # handle update
                go.update()
                
                # handel render
                go.render()
                
