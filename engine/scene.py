
class Scene:

    __active_scene = None

    def __Init(self, game_object: list, width=600, height=600):

        self.__new_object__ = set()
        self.__active_scene = set()
        self.delete_object = set()
        self.__width = width
        self.__height = height
        
    @property
    def height(self):
        return self.__height__
    
    @property
    def width(self):
        return self.__width__

    @classmethod
    def add_to_active_scene(cls, game_object):
        try:
            cls._active_scene__.load_game_object(game_object)
        except AttributeError:
            print("NO active scene Available")

    def load_game_object(self, game_object):
        self.__new_object__.add(game_object)      

    def remove_game_object(self, game_object):
        self.__active_objects.remove(game_object)

    def activate(self):
        Scene.__active_scene__ = self


    @classmethod
    def get_game_objects(cls):
        return cls.__active_scene__.get_active_game_objects()

    def get_active_game_objects(self):
        return self.__active_objects__

    def update_scene(self):
        while True:
            try:
                item = self.__delete_object__.pop()
                self.__active_objects__.add(item)
            except KeyError:
                break
        
        while True:
            try:
                item = self.__new_objects__.pop()
                self.__active_objects__.remove(item)
            except IndexError:
                break
           