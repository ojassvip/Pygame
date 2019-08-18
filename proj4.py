import pygame, sys
 
class Director:
    """Represents the main object of the game.
 
    The Director object keeps the game on, and takes care of updating it,
    drawing it and propagate events.
 
    This object must be used with Scene objects that are defined later."""
 
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Game Name")
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()
 
    def loop(self):
        "Main game loop"
 
        while not self.quit_flag:
            time = self.clock.tick(60)
 
            # Exit events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
 
            # Detect events
            self.scene.on_event()
 
            # Update scene
            self.scene.on_update()
 
            # Draw the screen
            self.scene.on_draw(self.screen)
            pygame.display.flip()
 
    def change_scene(self, scene):
        "Changes the current scene."
        self.scene = scene
 
    def quit(self):
        self.quit_flag = Trues

class Scene:
     """Represents a scene of the game.
 
     Scenes must be created inheriting this class attributes
     in order to be used afterwards as menus, introduction screens,
     etc."""
 
     def __init__(self, director):
         self.director = director
 
     def on_update(self):
         "Called from the director and defined on the subclass."
 
         raise NotImplementedError("on_update abstract method must be defined in subclass.")
 
     def on_event(self, event):
         "Called when a specific event is detected in the loop."
 
         raise NotImplementedError("on_event abstract method must be defined in subclass.")
 
     def on_draw(self, screen):
         "Se llama cuando se quiere dibujar la pantalla."
 
         raise NotImplementedError("on_draw abstract method must be defined in subclass.")


class SceneHome(scene.Scene):
    """ Welcome screen of the game, the first one to be loaded."""
 
    def __init__(self, director):
        scene.Scene.__init__(self, director)
 
    def on_update(self):
        pass
 
    def on_event(self):
        pass
 
    def on_draw(self):
        pass
   

def main():
    dir = director.Director()
    scene = scene_home.SceneHome(dir)
    dir.change_scene(scene)
    dir.loop()
 
if __name__ == '__main__':
    pygame.init()
    main()
    
