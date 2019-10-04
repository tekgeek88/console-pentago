import utils
import numpy as np


class Board:

    def __init__(self, tile_01=None, tile_02=None, tile_03=None, tile_04=None):

        if tile_01 is None:
            self._tile_01 = (('.', '.', '.'), ('.', '.', '.'), ('.', '.', '.'))
        else:
            self._tile_01 = tile_01
        if tile_02 is None:
            self._tile_02 = (('.', '.', '.'), ('.', '.', '.'), ('.', '.', '.'))
        else:
            self._tile_02 = tile_02
        if tile_03 is None:
            self._tile_03 = (('.', '.', '.'), ('.', '.', '.'), ('.', '.', '.'))
        else:
            self._tile_03 = tile_03
        if tile_04 is None:
            self._tile_04 = (('.', '.', '.'), ('.', '.', '.'), ('.', '.', '.'))
        else:
            self._tile_04 = tile_04

        self._board = (
            self._tile_01,
            self._tile_02,
            self._tile_03,
            self._tile_04,
        )

    @staticmethod
    def rotate_tile_right(board: tuple) -> tuple:
        rotated_list = list(np.rot90(np.array(board), 1, (1, 0)))
        return utils.convert_2d_array_to_2d_tuple(rotated_list)

    @staticmethod
    def rotate_tile_left(board):
        rotated_list = list(np.rot90(np.array(board), 1, (0, 1)))
        return utils.convert_2d_array_to_2d_tuple(rotated_list)

    def get_board_state(self):
        return self._board

    def get_tile(self, tile_num):
        if tile_num < 1 or tile_num > 4:
            return None
        else:
            return self._board[tile_num - 1]
1
