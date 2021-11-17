import pygame
import numpy as np


class Box:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.clicked = False
        self.x = x
        self.y = y

    def check(self):
        action = False
        # Get mouse position
        mous = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(mous):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True
        return action


def gameboard_init():
    rect1 = Box(170, 40, 170, 130)
    rect2 = Box(360, 40, 170, 130)
    rect3 = Box(540, 40, 170, 130)
    rect4 = Box(170, 180, 170, 135)
    rect5 = Box(360, 180, 170, 135)
    rect6 = Box(540, 180, 170, 135)
    rect7 = Box(170, 335, 170, 150)
    rect8 = Box(360, 335, 170, 150)
    rect9 = Box(540, 335, 170, 150)

    return rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9


def gameboard_check(turn, rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, final_matrix):
    show_list = []
    if rect1.check():
        # print('Rect1 clicked')
        idx = 1
        turn, show = new_turn(turn)
        show1 = ((show, rect1), (rect1.x, rect1.y-12, idx))
        show_list.append(show1)
        if show == 1:
            final_matrix[0, 0] = 1
        else:
            final_matrix[0, 0] = -1
    if rect2.check():
        idx = 2
        # print('Rect2 clicked')
        turn, show = new_turn(turn)
        show2 = ((show, rect2), (rect2.x, rect2.y-12, idx))
        show_list.append(show2)
        if show == 1:
            final_matrix[0, 1] = 1
        else:
            final_matrix[0, 1] = -1
    if rect3.check():
        idx = 3
        # print('Rect3 clicked')
        turn, show = new_turn(turn)
        show3 = ((show, rect3), (rect3.x, rect3.y-12, idx))
        show_list.append(show3)
        if show == 1:
            final_matrix[0, 2] = 1
        else:
            final_matrix[0, 2] = -1
    if rect4.check():
        idx = 4
        # print('Rect4 clicked')
        turn, show = new_turn(turn)
        show4 = ((show, rect4), (rect4.x, rect4.y, idx))
        show_list.append(show4)
        if show == 1:
            final_matrix[1, 0] = 1
        else:
            final_matrix[1, 0] = -1
    if rect5.check():
        idx = 5
        # print('Rect5 clicked')
        turn, show = new_turn(turn)
        show5 = ((show, rect5), (rect5.x, rect5.y, idx))
        show_list.append(show5)
        if show == 1:
            final_matrix[1, 1] = 1
        else:
            final_matrix[1, 1] = -1
    if rect6.check():
        idx = 6
        # print('Rect6 clicked')
        turn, show = new_turn(turn)
        show6 = ((show, rect6), (rect6.x, rect6.y, idx))
        show_list.append(show6)
        if show == 1:
            final_matrix[1, 2] = 1
        else:
            final_matrix[1, 2] = -1
    if rect7.check():
        idx = 7
        # print('Rect7 clicked')
        turn, show = new_turn(turn)
        show7 = ((show, rect7), (rect7.x, rect7.y, idx))
        show_list.append(show7)
        if show == 1:
            final_matrix[2, 0] = 1
        else:
            final_matrix[2, 0] = -1
    if rect8.check():
        idx = 8
        # print('Rect8 clicked')
        turn, show = new_turn(turn)
        show8 = ((show, rect8), (rect8.x, rect8.y, idx))
        show_list.append(show8)
        if show == 1:
            final_matrix[2, 1] = 1
        else:
            final_matrix[2, 1] = -1
    if rect9.check():
        idx = 9
        # print('Rect9 clicked')
        turn, show = new_turn(turn)
        show9 = ((show, rect9), (rect9.x, rect9.y, idx))
        show_list.append(show9)
        if show == 1:
            final_matrix[2, 2] = 1
        else:
            final_matrix[2, 2] = -1

    return turn, show_list, final_matrix


def new_turn(turn):
    if turn == 1:
        # print("Circle")
        show = 1
    else:
        # print("Cross")
        show = 2

    next_turn = (0 if turn == 1 else 1)
    return next_turn, show


def undo_matrix(undo_idx):
    if undo_idx == 1:
        temp_idx = (0, 0)
    elif undo_idx == 2:
        temp_idx = (0, 1)
    elif undo_idx == 3:
        temp_idx = (0, 2)
    elif undo_idx == 4:
        temp_idx = (1, 0)
    elif undo_idx == 5:
        temp_idx = (1, 1)
    elif undo_idx == 6:
        temp_idx = (1, 2)
    elif undo_idx == 7:
        temp_idx = (2, 0)
    elif undo_idx == 8:
        temp_idx = (2, 1)
    else:
        temp_idx = (2, 2)
    return temp_idx
