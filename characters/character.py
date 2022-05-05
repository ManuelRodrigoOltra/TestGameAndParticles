import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super.__init__()
        player = pygame.image.load('assets/characters/Characters/character_0001.png')
        player_rect = player.get_rect(center=(pos))
        player_rect = pygame.Rect(player_rect.center[0], player_rect.center[1], player_rect.width - 5,
                                  player_rect.height)
        player_movement = [0, 0]

    def move(self, rect, movement, tiles):
        collision_type = {'top': False, 'bottom': False, 'left': False, 'right': False}
        rect.x += movement[0]
        hit_list = self.collision_test(rect, tiles)

        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_type['right'] = True
            if movement[0] < 0:
                rect.left = tile.right
                collision_type['left'] = True
        rect.y += movement[1]
        hit_list = self.collision_test(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_type['bottom'] = True
            if movement[1] < 0:
                rect.top = tile.bottom
                collision_type['top'] = True

        return rect, collision_type

    def collision_test(self, rect, tiles):
        hit_list = []
        # newRec = pygame.Rect(rect.x, rect.y, rect.width, rect.height)
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list





