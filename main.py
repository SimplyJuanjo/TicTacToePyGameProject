import pygame
import button
import numpy as np
import win_conditions as wc
import gameboard as gb

# Initializing the pygame

pygame.init()

# Create the screen
scrHeight = 539
scrWeight = 910
screen = pygame.display.set_mode((scrWeight, scrHeight))
clock = pygame.time.Clock()

# Title and icon
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load('ttt.png').convert_alpha()
# <div>Iconos diseñados por <a href="https://www.freepik.com" title="Freepik">Freepik</a>
# from <a href="https://www.flaticon.es/" title="Flaticon">www.flaticon.es</a></div>
pygame.display.set_icon(icon)

# Background
backgroundImg = pygame.image.load('background.jpg').convert_alpha()

# Cursor
pygame.mouse.set_visible(False)
cursor = pygame.image.load('cursor.png').convert_alpha()
# <div>Iconos diseñados por <a href="https://www.freepik.com" title="Freepik">Freepik</a>
# from <a href="https://www.flaticon.es/" title="Flaticon">www.flaticon.es</a></div>

# Menu images
soloImg = pygame.image.load('soloplayer.png').convert_alpha()
# <div>Icons made by <a href="https://www.flaticon.com/authors/eucalyp" title="Eucalyp">Eucalyp</a>
# from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
for1v1Img = pygame.image.load('vs.png').convert_alpha()
# <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a>
# from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
exitImg = pygame.image.load('exit.png').convert_alpha()
# <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a>
# from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
restartImg = pygame.image.load('reload.png').convert_alpha()
# <div>Icons made by <a href="https://www.flaticon.com/authors/gregor-cresnar" title="Gregor Cresnar">Gregor Cresnar</a>
# from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
undoImg = pygame.image.load('undo.png').convert_alpha()
# <div>Icons made by <a href="https://www.flaticon.com/authors/google" title="Google">Google</a>
# from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>


# Initializing buttons
soloButton = button.Button(240, 225, soloImg, 1)
for1v1Button = button.Button(420, 225, for1v1Img, 1)
exitButton = button.Button(605, 225, exitImg, 1)
restartButton = button.Button(800, 50, restartImg, 1)
undoButton = button.Button(800, 130, undoImg, 1)

# Initializing clickable areas
rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9 = gb.gameboard_init()

# Game images
circle = pygame.image.load('circle.png').convert_alpha()
# <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a>
# from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
cross = pygame.image.load('x.png').convert_alpha()
# <div>Icons made by <a href="https://www.flaticon.com/authors/stockio" title="Stockio">Stockio</a>
# from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
winRed = pygame.image.load('winRed.png').convert_alpha()
winBlue = pygame.image.load('winBlue.png').convert_alpha()

# Game Loop
rects = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9]
running = 1
turn = 1
gamemode = 0
final_list = []
move_order = [1]
idx_list = [0]
final_matrix = np.zeros((3, 3))
while running:

    # Display background and main menu
    screen.blit(backgroundImg, (0, 0))
    soloButton.draw(screen)
    for1v1Button.draw(screen)
    exitButton.draw(screen)

    # Basic buttons functionality
    if soloButton.check():
        soloButton.clear()
        for1v1Button.clear()
        exitButton.move(800, 450)
        gamemode = 1
        exitButton.draw(screen)
    if for1v1Button.check():
        soloButton.clear()
        for1v1Button.clear()
        exitButton.move(800, 450)
        gamemode = 2
    if exitButton.check():
        running = 0
    if restartButton.check():
        final_list = []
        final_matrix = np.zeros((3, 3))
        move_order = [1]
        idx_list = [0]
        turn = 1
        for i, val in enumerate(rects):
            val.clicked = False
    if undoButton.check():
        # print(move_order) QUE MALDITO
        try:
            undo_rect = move_order[-2]
            undo_rect.clicked = False
            undo_idx = idx_list[-2]
            temp_idx = gb.undo_matrix(undo_idx)
            final_matrix[temp_idx] = 0
            print(final_matrix)
            move_order.pop(-2)
            idx_list.pop(-2)
            # print(move_order) DOLOR
            final_list.pop(-1)
            # print(final_list) DE CABEZA
            turn = (0 if turn == 1 else 1)
        except:
            pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

    # Screen updates (RGB)
    # screen.fill((0, 0, 0))        I won't be filling the color by now

    # Gamemodes loop cycle
    if gamemode == 1:
        restartButton.draw(screen)
        undoButton.draw(screen)
        turn = gb.gameboard_check(turn, rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, final_matrix)

    elif gamemode == 2:
        restartButton.draw(screen)
        undoButton.draw(screen)
        turn, show_list, final_matrix = gb.gameboard_check(turn, rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, final_matrix)
        for i in range(len(show_list)):
            show = show_list[i]
            final_list.append(show)
            print(final_list)
            print(final_matrix)

    # Represent moves
    for i in range(len(final_list)):
        tuple_1 = final_list[i]
        if move_order[i] != tuple_1[0][1]:
            move_order.append(tuple_1[0][1])
            move_order.remove(1)
            move_order.append(1)
        figure = tuple_1[0][0]
        pos_x = tuple_1[1][0]
        pos_y = tuple_1[1][1]
        if idx_list[i] != tuple_1[1][2]:
            idx_list.append(tuple_1[1][2])
            idx_list.remove(0)
            idx_list.append(0)
        if figure == 1:
            screen.blit(circle, (pos_x + 25, pos_y + 10))
        else:
            screen.blit(cross, (pos_x + 25, pos_y + 10))

    # Checking win conditions
    result = wc.win_checker(final_matrix)
    if result == 1:
        screen.blit(winRed, (194, 20))
    elif result == -1:
        screen.blit(winBlue, (194, 20))

    # Cursor style
    pos = pygame.mouse.get_pos()
    screen.blit(cursor, (pos[0], pos[1]))

    pygame.display.update()

    clock.tick(40)
