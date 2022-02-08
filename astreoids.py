
import pygame
import os

class Settings(object):
    window = {'width':800, 'height':500}
    fps = 60
    title = "Astroids"
    path = {}
    path['file'] = os.path.dirname(os.path.abspath(__file__))
    path['image'] = os.path.join(path['file'], "images")
    
    @staticmethod
    def dim():
        return (Settings.window['width'], Settings.window['height'])

    @staticmethod
    def filepath(name):
        return os.path.join(Settings.path['file'], name)

    @staticmethod
    def imagepath(name):
        return os.path.join(Settings.path['image'], name)

class Background(pygame.sprite.Sprite):
    def __init__(self, filename) -> None:
        super().__init__()
        self.image = pygame.image.load(Settings.imagepath(filename)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (Settings.window['width'], Settings.window['height']))
      
    def draw(self, screen):
        screen.blit(self.image,(0,0))

class pilot(pygame.sprite.Sprite):
    def __init__(self, filename) -> None:
        super().__init__()

        self.pilot = pygame.image.load(Settings.imagepath(filename)).convert()
        self.rect = self.pilot.get_rect()
        self.rect.center = (Settings.window['width'] // 2, Settings.window['height'] // 2)

    def draw(self, screen):
        screen.blit(self.pilot,(0,0))
    def update(self):
        pass

class Astroids(object):
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((Settings.window['width'], Settings.window['height']))
        self.background = Background("Background.jpg")
        self.pilot = pilot("3.png")
        self.clock = pygame.time.Clock()
        self.running = True
        self.pilot = pygame.sprite.GroupSingle(self.pilot)

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.watch_for_events()
            self.update()
            self.draw()
        pygame.quit()

    def watch_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.QUIT:
                self.running = False

    def update(self):

        self.pilot.sprite.update()

    def draw(self):
        self.background.draw(self.screen)
        self.pilot.sprite.draw(self.screen)
        pygame.display.flip

if __name__ == "__main__":

    game = Astroids()
    game.run()
