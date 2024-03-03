class Tile:
    def __init__(self, image, source):
        self.image = image
        self.source = source

    def blit(self, target, destination):
        target.blit(self.image, destination, self.source)
