import pygame

#width of game screen
WIDTH = 800
FPS = 30
PLAYER_SPEED = 4
#how big sprite box is
GAP = 30

#set colors
RED = (253, 255, 230)
GREEN = (253, 255, 231)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
LIGHTBLUE = (4, 157, 253)
PINK = (255,192,203)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

#lists for storing nodes


vec = pygame.math.Vector2

#tilemaps must be equal sides
tilemap1 = ['BBBBBBB',
           'BD.BQ.B',
           'B.....B',
           'BB.P..B',
           'B..BBBB',
           'B.....B',
           'BBBBBBB']

tilemap1 = ['BBBB',
           'BP.B',
           'BA.B',
           'BBBB']

tilemap1 = ['B.',
           'B.']


tilemap1 = [
    'BBBBBBBBBBBBBBBBBBBBBBB',
    'B.....................B',
    'B...........T.........B',
    'B.....................B',
    'B.....................B',
    'B.BBBBBBBBB...........B',
    'B.....................B',
    'B.......P.BBBBBBBBB...B',
    'B.....................B',
    'B.....................B',
    'B.....................B',
    'B.....................B',
    'BBB...................B',
    'B....Q..T.......B.....B',
    'B....T....S.....B.....B',
    'B.S.........T...B.....B',
    'B.......T.......B.....B',
    'B..T..................B',
    'B.......S...T.........B',
    'B............S........B',
    'B..T..................B',
    'B.........T...........B',
    'BBBBBBBBBBBBBBBBBBBBBBB'
]

tilemap = [
    'BBBBBBBBBBBBBBBBBBBBBBB',
    'B.....................B',
    'B.....................B',
    'B........D............B',
    'B.....................B',
    'B.BBBBBBBBB...........B',
    'B.....................B',
    'B.......P.BBBBBBBBB...B',
    'B.....................B',
    'B.....................B',
    'B.....................B',
    'B.....................B',
    'BBB...................B',
    'B....Q..B.......B.....B',
    'B....B..........B.....B',
    'B...........B...B.....B',
    'B.......B.......B.....B',
    'B..B..................B',
    'B...........B.........B',
    'B.....................B',
    'B..B..................B',
    'B.........B...........B',
    'BBBBBBBBBBBBBBBBBBBBBBB'
]



tilemap1 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B..........S...........................B',
    'B..........P............T..........T...B',
    'B..S....T...................S..........B',
    'B...D..........TT......................B',
    'B......BBBBBB...................S......B',
    'B......B....B...............T..........B',
    'B......B....B.T.............BBBBBBB.BBBB',
    'B......................................B',
    'B...............S......T...............B',
    'B......T......................T........B',
    'B......................................B',
    'B....S.................................B',
    'BBBBBBBBBBBBBBBBB....BBBBBBBBBBBBBBBBBBB',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'BBBBBBBBBBBBBBBBBB..BBBBBBBBBBBBBBBBBBBB',
    'B...................B......B...........B',
    'B...................B......B..B........B',
    'B....BBBBBBBBBBBB...B......B..B........B',
    'B.....B.............B.........B........B',
    'B.....B...BBB.......B.....BBBBBBBBBB...B',
    'B.....B....BB.......B..................B',
    'B.....B................................B',
    'B.....B........BBBBBBBBBBBBBBBBBBBBB...B',
    'B.........B..............B.............B',
    'B........................B..Q..........B',
    'BBBBBBBB.................B......T......B',
    'B...........B.....BBBB.BBB......S......B',
    'B...........B.....B......B.............B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'
]

tilemap1 = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B.......A..........B',
    'B..................B',
    'B.BBBBBBBBBBBBBB...B',
    'B..................B',
    'B.........BBBBBBBBBB',
    'B...A..............B',
    'B..................B',
    'B..................B',
    'B...........A......B',
    'BBBBBBBBBBBBBBBBBB.B',
    'B....Q..........B..B',
    'B...............B..B',
    'B........P......B..B',
    'B..t............B..B',
    'B..T...............B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB'
]