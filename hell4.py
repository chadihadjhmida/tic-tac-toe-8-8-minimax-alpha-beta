import tkinter
import random
import json
import os


x_board = 0b0000000000000000000000000000000000000000000000000000000000000000
o_board = 0b0000000000000000000000000000000000000000000000000000000000000000


def set_bit(board, row, col):
    return board | (1 << (row * 8 + col))


def check_rows(bitboard):
    # Check all possible starting positions for four consecutive bits
    # Unroll the loops manually
    # Row 0
    if (bitboard & 0b1111) == 0b1111:
        return True
    if (bitboard & (0b1111 << 1)) == (0b1111 << 1):
        return True
    if (bitboard & (0b1111 << 2)) == (0b1111 << 2):
        return True
    if (bitboard & (0b1111 << 3)) == (0b1111 << 3):
        return True
    if (bitboard & (0b1111 << 4)) == (0b1111 << 4):
        return True

    # Row 1
    if (bitboard & (0b1111 << 8)) == (0b1111 << 8):
        return True
    if (bitboard & (0b1111 << 9)) == (0b1111 << 9):
        return True
    if (bitboard & (0b1111 << 10)) == (0b1111 << 10):
        return True
    if (bitboard & (0b1111 << 11)) == (0b1111 << 11):
        return True
    if (bitboard & (0b1111 << 12)) == (0b1111 << 12):
        return True

    # Row 2
    if (bitboard & (0b1111 << 16)) == (0b1111 << 16):
        return True
    if (bitboard & (0b1111 << 17)) == (0b1111 << 17):
        return True
    if (bitboard & (0b1111 << 18)) == (0b1111 << 18):
        return True
    if (bitboard & (0b1111 << 19)) == (0b1111 << 19):
        return True
    if (bitboard & (0b1111 << 20)) == (0b1111 << 20):
        return True

    # Row 3
    if (bitboard & (0b1111 << 24)) == (0b1111 << 24):
        return True
    if (bitboard & (0b1111 << 25)) == (0b1111 << 25):
        return True
    if (bitboard & (0b1111 << 26)) == (0b1111 << 26):
        return True
    if (bitboard & (0b1111 << 27)) == (0b1111 << 27):
        return True
    if (bitboard & (0b1111 << 28)) == (0b1111 << 28):
        return True

    # Row 4
    if (bitboard & (0b1111 << 32)) == (0b1111 << 32):
        return True
    if (bitboard & (0b1111 << 33)) == (0b1111 << 33):
        return True
    if (bitboard & (0b1111 << 34)) == (0b1111 << 34):
        return True
    if (bitboard & (0b1111 << 35)) == (0b1111 << 35):
        return True
    if (bitboard & (0b1111 << 36)) == (0b1111 << 36):
        return True

    # Row 5
    if (bitboard & (0b1111 << 40)) == (0b1111 << 40):
        return True
    if (bitboard & (0b1111 << 41)) == (0b1111 << 41):
        return True
    if (bitboard & (0b1111 << 42)) == (0b1111 << 42):
        return True
    if (bitboard & (0b1111 << 43)) == (0b1111 << 43):
        return True
    if (bitboard & (0b1111 << 44)) == (0b1111 << 44):
        return True

    # Row 6
    if (bitboard & (0b1111 << 48)) == (0b1111 << 48):
        return True
    if (bitboard & (0b1111 << 49)) == (0b1111 << 49):
        return True
    if (bitboard & (0b1111 << 50)) == (0b1111 << 50):
        return True
    if (bitboard & (0b1111 << 51)) == (0b1111 << 51):
        return True
    if (bitboard & (0b1111 << 52)) == (0b1111 << 52):
        return True

    # Row 7
    if (bitboard & (0b1111 << 56)) == (0b1111 << 56):
        return True
    if (bitboard & (0b1111 << 57)) == (0b1111 << 57):
        return True
    if (bitboard & (0b1111 << 58)) == (0b1111 << 58):
        return True
    if (bitboard & (0b1111 << 59)) == (0b1111 << 59):
        return True
    if (bitboard & (0b1111 << 60)) == (0b1111 << 60):
        return True

    return False


def check_columns(bitboard):
    # Check all possible starting positions for four consecutive bits in columns
    # Unroll the loops manually

    # Column 0
    mask = 0b1 << 0
    mask |= 0b1 << 8
    mask |= 0b1 << 16
    mask |= 0b1 << 24
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 8
    mask |= 0b1 << 16
    mask |= 0b1 << 24
    mask |= 0b1 << 32
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 16
    mask |= 0b1 << 24
    mask |= 0b1 << 32
    mask |= 0b1 << 40
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 24
    mask |= 0b1 << 32
    mask |= 0b1 << 40
    mask |= 0b1 << 48
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 32
    mask |= 0b1 << 40
    mask |= 0b1 << 48
    mask |= 0b1 << 56
    if (bitboard & mask) == mask:
        return True

    # Column 1
    mask = 0b1 << 1
    mask |= 0b1 << 9
    mask |= 0b1 << 17
    mask |= 0b1 << 25
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 9
    mask |= 0b1 << 17
    mask |= 0b1 << 25
    mask |= 0b1 << 33
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 17
    mask |= 0b1 << 25
    mask |= 0b1 << 33
    mask |= 0b1 << 41
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 25
    mask |= 0b1 << 33
    mask |= 0b1 << 41
    mask |= 0b1 << 49
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 33
    mask |= 0b1 << 41
    mask |= 0b1 << 49
    mask |= 0b1 << 57
    if (bitboard & mask) == mask:
        return True

    # Column 2
    mask = 0b1 << 2
    mask |= 0b1 << 10
    mask |= 0b1 << 18
    mask |= 0b1 << 26
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 10
    mask |= 0b1 << 18
    mask |= 0b1 << 26
    mask |= 0b1 << 34
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 18
    mask |= 0b1 << 26
    mask |= 0b1 << 34
    mask |= 0b1 << 42
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 26
    mask |= 0b1 << 34
    mask |= 0b1 << 42
    mask |= 0b1 << 50
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 34
    mask |= 0b1 << 42
    mask |= 0b1 << 50
    mask |= 0b1 << 58
    if (bitboard & mask) == mask:
        return True

    # Column 3
    mask = 0b1 << 3
    mask |= 0b1 << 11
    mask |= 0b1 << 19
    mask |= 0b1 << 27
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 11
    mask |= 0b1 << 19
    mask |= 0b1 << 27
    mask |= 0b1 << 35
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 19
    mask |= 0b1 << 27
    mask |= 0b1 << 35
    mask |= 0b1 << 43
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 27
    mask |= 0b1 << 35
    mask |= 0b1 << 43
    mask |= 0b1 << 51
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 35
    mask |= 0b1 << 43
    mask |= 0b1 << 51
    mask |= 0b1 << 59
    if (bitboard & mask) == mask:
        return True

    # Column 4
    mask = 0b1 << 4
    mask |= 0b1 << 12
    mask |= 0b1 << 20
    mask |= 0b1 << 28
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 12
    mask |= 0b1 << 20
    mask |= 0b1 << 28
    mask |= 0b1 << 36
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 20
    mask |= 0b1 << 28
    mask |= 0b1 << 36
    mask |= 0b1 << 44
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 28
    mask |= 0b1 << 36
    mask |= 0b1 << 44
    mask |= 0b1 << 52
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 36
    mask |= 0b1 << 44
    mask |= 0b1 << 52
    mask |= 0b1 << 60
    if (bitboard & mask) == mask:
        return True

    # Column 5
    mask = 0b1 << 5
    mask |= 0b1 << 13
    mask |= 0b1 << 21
    mask |= 0b1 << 29
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 13
    mask |= 0b1 << 21
    mask |= 0b1 << 29
    mask |= 0b1 << 37
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 21
    mask |= 0b1 << 29
    mask |= 0b1 << 37
    mask |= 0b1 << 45
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 29
    mask |= 0b1 << 37
    mask |= 0b1 << 45
    mask |= 0b1 << 53
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 37
    mask |= 0b1 << 45
    mask |= 0b1 << 53
    mask |= 0b1 << 61
    if (bitboard & mask) == mask:
        return True

    # Column 6
    mask = 0b1 << 6
    mask |= 0b1 << 14
    mask |= 0b1 << 22
    mask |= 0b1 << 30
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 14
    mask |= 0b1 << 22
    mask |= 0b1 << 30
    mask |= 0b1 << 38
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 22
    mask |= 0b1 << 30
    mask |= 0b1 << 38
    mask |= 0b1 << 46
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 30
    mask |= 0b1 << 38
    mask |= 0b1 << 46
    mask |= 0b1 << 54
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 38
    mask |= 0b1 << 46
    mask |= 0b1 << 54
    mask |= 0b1 << 62
    if (bitboard & mask) == mask:
        return True

    # Column 7
    mask = 0b1 << 7
    mask |= 0b1 << 15
    mask |= 0b1 << 23
    mask |= 0b1 << 31
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 15
    mask |= 0b1 << 23
    mask |= 0b1 << 31
    mask |= 0b1 << 39
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 23
    mask |= 0b1 << 31
    mask |= 0b1 << 39
    mask |= 0b1 << 47
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 31
    mask |= 0b1 << 39
    mask |= 0b1 << 47
    mask |= 0b1 << 55
    if (bitboard & mask) == mask:
        return True

    mask = 0b1 << 39
    mask |= 0b1 << 47
    mask |= 0b1 << 55
    mask |= 0b1 << 63
    if (bitboard & mask) == mask:
        return True

    return False


def check_diagonals(bitboard):
    # Check diagonals with positive slope
    # Unroll the loops manually

    # Positive slope diagonals
    # Diagonal starting at (0, 0)
    mask = 0b1 << 0
    mask |= 0b1 << 9
    mask |= 0b1 << 18
    mask |= 0b1 << 27
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (0, 1)
    mask = 0b1 << 1
    mask |= 0b1 << 10
    mask |= 0b1 << 19
    mask |= 0b1 << 28
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (0, 2)
    mask = 0b1 << 2
    mask |= 0b1 << 11
    mask |= 0b1 << 20
    mask |= 0b1 << 29
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (0, 3)
    mask = 0b1 << 3
    mask |= 0b1 << 12
    mask |= 0b1 << 21
    mask |= 0b1 << 30
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (0, 4)
    mask = 0b1 << 4
    mask |= 0b1 << 13
    mask |= 0b1 << 22
    mask |= 0b1 << 31
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (1, 0)
    mask = 0b1 << 8
    mask |= 0b1 << 17
    mask |= 0b1 << 26
    mask |= 0b1 << 35
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (1, 1)
    mask = 0b1 << 9
    mask |= 0b1 << 18
    mask |= 0b1 << 27
    mask |= 0b1 << 36
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (1, 2)
    mask = 0b1 << 10
    mask |= 0b1 << 19
    mask |= 0b1 << 28
    mask |= 0b1 << 37
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (1, 3)
    mask = 0b1 << 11
    mask |= 0b1 << 20
    mask |= 0b1 << 29
    mask |= 0b1 << 38
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (1, 4)
    mask = 0b1 << 12
    mask |= 0b1 << 21
    mask |= 0b1 << 30
    mask |= 0b1 << 39
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (2, 0)
    mask = 0b1 << 16
    mask |= 0b1 << 25
    mask |= 0b1 << 34
    mask |= 0b1 << 43
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (2, 1)
    mask = 0b1 << 17
    mask |= 0b1 << 26
    mask |= 0b1 << 35
    mask |= 0b1 << 44
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (2, 2)
    mask = 0b1 << 18
    mask |= 0b1 << 27
    mask |= 0b1 << 36
    mask |= 0b1 << 45
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (2, 3)
    mask = 0b1 << 19
    mask |= 0b1 << 28
    mask |= 0b1 << 37
    mask |= 0b1 << 46
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (2, 4)
    mask = 0b1 << 20
    mask |= 0b1 << 29
    mask |= 0b1 << 38
    mask |= 0b1 << 47
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (3, 0)
    mask = 0b1 << 24
    mask |= 0b1 << 33
    mask |= 0b1 << 42
    mask |= 0b1 << 51
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (3, 1)
    mask = 0b1 << 25
    mask |= 0b1 << 34
    mask |= 0b1 << 43
    mask |= 0b1 << 52
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (3, 2)
    mask = 0b1 << 26
    mask |= 0b1 << 35
    mask |= 0b1 << 44
    mask |= 0b1 << 53
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (3, 3)
    mask = 0b1 << 27
    mask |= 0b1 << 36
    mask |= 0b1 << 45
    mask |= 0b1 << 54
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (3, 4)
    mask = 0b1 << 28
    mask |= 0b1 << 37
    mask |= 0b1 << 46
    mask |= 0b1 << 55
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (4, 0)
    mask = 0b1 << 32
    mask |= 0b1 << 41
    mask |= 0b1 << 50
    mask |= 0b1 << 59
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (4, 1)
    mask = 0b1 << 33
    mask |= 0b1 << 42
    mask |= 0b1 << 51
    mask |= 0b1 << 60
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (4, 2)
    mask = 0b1 << 34
    mask |= 0b1 << 43
    mask |= 0b1 << 52
    mask |= 0b1 << 61
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (4, 3)
    mask = 0b1 << 35
    mask |= 0b1 << 44
    mask |= 0b1 << 53
    mask |= 0b1 << 62
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (4, 4)
    mask = 0b1 << 36
    mask |= 0b1 << 45
    mask |= 0b1 << 54
    mask |= 0b1 << 63
    if (bitboard & mask) == mask:
        return True

    # Check diagonals with negative slope
    # Unroll the loops manually

    # Negative slope diagonals
    # Diagonal starting at (3, 0)
    mask = 0b1 << 24
    mask |= 0b1 << 17
    mask |= 0b1 << 10
    mask |= 0b1 << 3
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (4, 0)
    mask = 0b1 << 32
    mask |= 0b1 << 25
    mask |= 0b1 << 18
    mask |= 0b1 << 11
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (5, 0)
    mask = 0b1 << 40
    mask |= 0b1 << 33
    mask |= 0b1 << 26
    mask |= 0b1 << 19
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (6, 0)
    mask = 0b1 << 48
    mask |= 0b1 << 41
    mask |= 0b1 << 34
    mask |= 0b1 << 27
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (7, 0)
    mask = 0b1 << 56
    mask |= 0b1 << 49
    mask |= 0b1 << 42
    mask |= 0b1 << 35
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (3, 1)
    mask = 0b1 << 25
    mask |= 0b1 << 18
    mask |= 0b1 << 11
    mask |= 0b1 << 4
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (4, 1)
    mask = 0b1 << 33
    mask |= 0b1 << 26
    mask |= 0b1 << 19
    mask |= 0b1 << 12
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (5, 1)
    mask = 0b1 << 41
    mask |= 0b1 << 34
    mask |= 0b1 << 27
    mask |= 0b1 << 20
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (6, 1)
    mask = 0b1 << 49
    mask |= 0b1 << 42
    mask |= 0b1 << 35
    mask |= 0b1 << 28
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (7, 1)
    mask = 0b1 << 57
    mask |= 0b1 << 50
    mask |= 0b1 << 43
    mask |= 0b1 << 36
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (3, 2)
    mask = 0b1 << 26
    mask |= 0b1 << 19
    mask |= 0b1 << 12
    mask |= 0b1 << 5
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (4, 2)
    mask = 0b1 << 34
    mask |= 0b1 << 27
    mask |= 0b1 << 20
    mask |= 0b1 << 13
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (5, 2)
    mask = 0b1 << 42
    mask |= 0b1 << 35
    mask |= 0b1 << 28
    mask |= 0b1 << 21
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (6, 2)
    mask = 0b1 << 50
    mask |= 0b1 << 43
    mask |= 0b1 << 36
    mask |= 0b1 << 29
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (7, 2)
    mask = 0b1 << 58
    mask |= 0b1 << 51
    mask |= 0b1 << 44
    mask |= 0b1 << 37
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (3, 3)
    mask = 0b1 << 27
    mask |= 0b1 << 20
    mask |= 0b1 << 13
    mask |= 0b1 << 6
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (4, 3)
    mask = 0b1 << 35
    mask |= 0b1 << 28
    mask |= 0b1 << 21
    mask |= 0b1 << 14
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (5, 3)
    mask = 0b1 << 43
    mask |= 0b1 << 36
    mask |= 0b1 << 29
    mask |= 0b1 << 22
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (6, 3)
    mask = 0b1 << 51
    mask |= 0b1 << 44
    mask |= 0b1 << 37
    mask |= 0b1 << 30
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (7, 3)
    mask = 0b1 << 59
    mask |= 0b1 << 52
    mask |= 0b1 << 45
    mask |= 0b1 << 38
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (3, 4)
    mask = 0b1 << 28
    mask |= 0b1 << 21
    mask |= 0b1 << 14
    mask |= 0b1 << 7
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (4, 4)
    mask = 0b1 << 36
    mask |= 0b1 << 29
    mask |= 0b1 << 22
    mask |= 0b1 << 15
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (5, 4)
    mask = 0b1 << 44
    mask |= 0b1 << 37
    mask |= 0b1 << 30
    mask |= 0b1 << 23
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (6, 4)
    mask = 0b1 << 52
    mask |= 0b1 << 45
    mask |= 0b1 << 38
    mask |= 0b1 << 31
    if (bitboard & mask) == mask:
        return True

    # Diagonal starting at (7, 4)
    mask = 0b1 << 60
    mask |= 0b1 << 53
    mask |= 0b1 << 46
    mask |= 0b1 << 39
    if (bitboard & mask) == mask:
        return True

    return False


def is_game_over(bitboard_X, bitboard_O):
    if (
        check_rows(bitboard_X)
        or check_columns(bitboard_X)
        or check_diagonals(bitboard_X)
    ):
        print("X wins")
        return True
    if (
        check_rows(bitboard_O)
        or check_columns(bitboard_O)
        or check_diagonals(bitboard_O)
    ):
        print("O wins")
        return True
    # Check for a draw (all cells filled)
    if (bitboard_X | bitboard_O) == 0xFFFFFFFFFFFFFFFF:
        print("Draw")
        return True
    return False


def evaluate_board(bitboard_X, bitboard_O):
    # Calculate scores for both players
    score_X = calculate_score(bitboard_X, bitboard_O, is_maximizing=True)
    score_O = calculate_score(bitboard_O, bitboard_X, is_maximizing=False)

    # Add center control bonus
    center_bonus_X = count_center_control(bitboard_X)
    center_bonus_O = count_center_control(bitboard_O)

    # Add flexibility bonus
    flexibility_bonus_X = count_flexibility(bitboard_X, bitboard_O)
    flexibility_bonus_O = count_flexibility(bitboard_O, bitboard_X)

    # Combine scores
    total_score = (score_X + center_bonus_X + flexibility_bonus_X) - (
        score_O + center_bonus_O + flexibility_bonus_O
    )
    return total_score


def calculate_score(bitboard_player, bitboard_opponent, is_maximizing):
    score = 0

    # Define patterns for 2, 3, and 4 in a row
    patterns = [
        (0b1111, 1000),  # 4-in-a-row (win)
        (0b0111, 100),  # 3-in-a-row
        (0b0011, 10),  # 2-in-a-row
    ]

    # Check rows, columns, and diagonals
    for i in range(8):
        for j in range(5):
            # Check rows
            mask = 0b1111 << (i * 8 + j)
            bits = (bitboard_player & mask) >> (i * 8 + j)
            for pattern, value in patterns:
                if (bits & pattern) == pattern:
                    score += value
            # Check columns
            mask = 0b1 << (i * 8 + j)
            mask |= 0b1 << ((i + 1) * 8 + j)
            mask |= 0b1 << ((i + 2) * 8 + j)
            mask |= 0b1 << ((i + 3) * 8 + j)
            bits = 0
            for k in range(4):
                bits |= (
                    (bitboard_player & (1 << ((i + k) * 8 + j))) >> ((i + k) * 8 + j)
                ) << k
            for pattern, value in patterns:
                if (bits & pattern) == pattern:
                    score += value
            # Check diagonals (positive slope)
            if i <= 4 and j <= 4:
                bits = 0
                for k in range(4):
                    bits |= (
                        (bitboard_player & (1 << ((i + k) * 8 + (j + k))))
                        >> ((i + k) * 8 + (j + k))
                        << k
                    )
                for pattern, value in patterns:
                    if (bits & pattern) == pattern:
                        score += value
            # Check diagonals (negative slope)
            if i >= 3 and j <= 4:
                bits = 0
                for k in range(4):
                    bits |= (
                        (bitboard_player & (1 << ((i - k) * 8 + (j + k))))
                        >> ((i - k) * 8 + (j + k))
                        << k
                    )
                for pattern, value in patterns:
                    if (bits & pattern) == pattern:
                        score += value

    # Block opponent's potential wins
    if is_maximizing:
        opponent_patterns = [
            (0b1111, 500),  # Block opponent's 4-in-a-row
            (0b0111, 50),  # Block opponent's 3-in-a-row
            (0b0011, 5),  # Block opponent's 2-in-a-row
        ]
        for i in range(8):
            for j in range(5):
                # Check rows
                mask = 0b1111 << (i * 8 + j)
                bits = (bitboard_opponent & mask) >> (i * 8 + j)
                for pattern, value in opponent_patterns:
                    if (bits & pattern) == pattern:
                        score += value
                # Check columns
                mask = 0b1 << (i * 8 + j)
                mask |= 0b1 << ((i + 1) * 8 + j)
                mask |= 0b1 << ((i + 2) * 8 + j)
                mask |= 0b1 << ((i + 3) * 8 + j)
                bits = 0
                for k in range(4):
                    bits |= (
                        (bitboard_opponent & (1 << ((i + k) * 8 + j)))
                        >> ((i + k) * 8 + j)
                    ) << k
                for pattern, value in opponent_patterns:
                    if (bits & pattern) == pattern:
                        score += value
                # Check diagonals (positive slope)
                if i <= 4 and j <= 4:
                    bits = 0
                    for k in range(4):
                        bits |= (
                            (bitboard_opponent & (1 << ((i + k) * 8 + (j + k))))
                            >> ((i + k) * 8 + (j + k))
                            << k
                        )
                    for pattern, value in opponent_patterns:
                        if (bits & pattern) == pattern:
                            score += value
                # Check diagonals (negative slope)
                if i >= 3 and j <= 4:
                    bits = 0
                    for k in range(4):
                        bits |= (
                            (bitboard_opponent & (1 << ((i - k) * 8 + (j + k))))
                            >> ((i - k) * 8 + (j + k))
                            << k
                        )
                    for pattern, value in opponent_patterns:
                        if (bits & pattern) == pattern:
                            score += value

    return score


def count_center_control(bitboard):
    center_cells = [
        (3, 3),
        (3, 4),
        (4, 3),
        (4, 4),  # 4 central cells in an 8x8 grid
    ]
    bonus = 0
    for cell in center_cells:
        row, col = cell
        position = row * 8 + col
        if bitboard & (1 << position):
            bonus += 10  # Add 10 points for each controlled center cell
    return bonus


def count_flexibility(bitboard_player, bitboard_opponent):
    flexibility = 0
    # Count the number of open lines (rows, columns, diagonals) that the player can still use
    for i in range(8):
        for j in range(8):
            if not (bitboard_player & (1 << (i * 8 + j))) and not (
                bitboard_opponent & (1 << (i * 8 + j))
            ):
                # Check if the cell is part of a potential winning line
                if is_part_of_potential_line(i, j, bitboard_player, bitboard_opponent):
                    flexibility += 5  # Add 5 points for each flexible cell
    return flexibility


def is_part_of_potential_line(row, col, bitboard_player, bitboard_opponent):
    # Check if the cell is part of a potential winning line (row, column, or diagonal)
    # This is a simplified check; a full implementation would be more comprehensive
    for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
        count = 0
        for k in range(-3, 4):
            r = row + dr * k
            c = col + dc * k
            if 0 <= r < 8 and 0 <= c < 8:
                if bitboard_player & (1 << (r * 8 + c)):
                    count += 1
                elif bitboard_opponent & (1 << (r * 8 + c)):
                    break  # Opponent's cell blocks the line
        if count >= 2:  # At least 2 player cells in the line
            return True
    return False


transposition_table = {}


def generate_moves(occupied_bitboard):
    moves = []
    for i in range(8):
        for j in range(8):
            position = i * 8 + j
            if not (occupied_bitboard & (1 << position)):
                moves.append((i, j))
    return moves


def evaluate_move(bitboard_X, bitboard_O, move, maximizing_player):
    if maximizing_player:
        new_bitboard_X = set_bit(bitboard_X, move[0], move[1])
        return evaluate_board(new_bitboard_X, bitboard_O)
    else:
        new_bitboard_O = set_bit(bitboard_O, move[0], move[1])
        return evaluate_board(bitboard_X, new_bitboard_O)


# def minimax(
#    bitboard_X, bitboard_O, depth, alpha, beta, maximizing_player, transposition_table
# ):
#    # Check if the game is over or depth limit is reached
#    result = is_game_over(bitboard_X, bitboard_O)
#    if result is True or depth == 0:
#        return evaluate_board(bitboard_X, bitboard_O), (
#            0,
#            0,
#        )  # Return a default move (0, 0)
#
#    # Check transposition table for cached results
#    key = (bitboard_X, bitboard_O, depth, maximizing_player)
#    if key in transposition_table:
#        return transposition_table[key]
#
#    moves = generate_moves(bitboard_X | bitboard_O)
#    if not moves:  # No valid moves left (should not happen in a standard game)
#        return evaluate_board(bitboard_X, bitboard_O), (
#            0,
#            0,
#        )  # Return a default move (0, 0)
#
#    # Evaluate and sort moves by strength
#    move_scores = []
#    for move in moves:
#        if maximizing_player:
#            new_bitboard_X = set_bit(bitboard_X, move[0], move[1])
#            score = evaluate_move(bitboard_X, bitboard_O, move, True)
#        else:
#            new_bitboard_O = set_bit(bitboard_O, move[0], move[1])
#            score = evaluate_move(bitboard_X, bitboard_O, move, False)
#        move_scores.append((move, score))
#
#    # Sort moves by score (best moves first)
#    move_scores.sort(key=lambda x: x[1], reverse=maximizing_player)
#
#    best_move = move_scores[0][0]  # Initialize with the best move
#    if maximizing_player:
#        max_eval = -float("inf")
#        for move, score in move_scores:
#            # Reduce depth for weak moves
#            current_depth = depth if score > 50 else depth // 2  # Example threshold
#            new_bitboard_X = set_bit(bitboard_X, move[0], move[1])
#            eval, _ = minimax(
#                new_bitboard_X,
#                bitboard_O,
#                current_depth - 1,
#                alpha,
#                beta,
#                False,
#                transposition_table,
#            )
#
#            if eval > max_eval:
#                max_eval = eval
#                best_move = move  # Update the best move
#
#            alpha = max(alpha, eval)
#            if beta <= alpha:
#                break  # Beta cutoff
#
#        # Cache the result
#        transposition_table[key] = (max_eval, best_move)
#        return max_eval, best_move
#    else:
#        min_eval = float("inf")
#        for move, score in move_scores:
#            # Reduce depth for weak moves
#            current_depth = depth if score < -50 else depth // 2  # Example threshold
#            new_bitboard_O = set_bit(bitboard_O, move[0], move[1])
#            eval, _ = minimax(
#                bitboard_X,
#                new_bitboard_O,
#                current_depth - 1,
#                alpha,
#                beta,
#                True,
#                transposition_table,
#            )
#
#            if eval < min_eval:
#                min_eval = eval
#                best_move = move  # Update the best move
#
#            beta = min(beta, eval)
#            if beta <= alpha:
#                break  # Alpha cutoff
#
#        # Cache the result
#        transposition_table[key] = (min_eval, best_move)
#        return min_eval, best_move
#


def minimax(
    bitboard_X, bitboard_O, depth, alpha, beta, maximizing_player, transposition_table
):
    # Check if the game is over or depth limit is reached
    result = is_game_over(bitboard_X, bitboard_O)
    if result is True or depth == 0:
        return evaluate_board(bitboard_X, bitboard_O), None

    # Check transposition table for cached results
    key = (bitboard_X, bitboard_O, depth, maximizing_player)
    if key in transposition_table:
        return transposition_table[key]

    if maximizing_player:
        max_eval = -float("inf")
        best_move = None
        moves = generate_moves(bitboard_X | bitboard_O)

        # Sort moves by evaluation (best moves first)
        moves.sort(
            key=lambda move: evaluate_move(bitboard_X, bitboard_O, move, True),
            reverse=True,
        )

        for move in moves:
            new_bitboard_X = set_bit(bitboard_X, move[0], move[1])
            eval, _ = minimax(
                new_bitboard_X,
                bitboard_O,
                depth - 1,
                alpha,
                beta,
                False,
                transposition_table,
            )

            if eval > max_eval:
                max_eval = eval
                best_move = move

            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff

        # Cache the result
        transposition_table[key] = (max_eval, best_move)
        return max_eval, best_move
    else:
        min_eval = float("inf")
        best_move = None
        moves = generate_moves(bitboard_X | bitboard_O)

        # Sort moves by evaluation (worst moves for the opponent first)
        moves.sort(key=lambda move: evaluate_move(bitboard_X, bitboard_O, move, False))

        for move in moves:
            new_bitboard_O = set_bit(bitboard_O, move[0], move[1])
            eval, _ = minimax(
                bitboard_X,
                new_bitboard_O,
                depth - 1,
                alpha,
                beta,
                True,
                transposition_table,
            )

            if eval < min_eval:
                min_eval = eval
                best_move = move

            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff

        # Cache the result
        transposition_table[key] = (min_eval, best_move)
        return min_eval, best_move


def find_best_move(bitboard_X, bitboard_O, max_depth, maximizing_player):
    transposition_table = {}
    best_move = []
    for depth in range(1, max_depth + 1):
        _, best_move = minimax(
            bitboard_X,
            bitboard_O,
            depth,
            -float("inf"),
            float("inf"),
            maximizing_player,
            transposition_table,
        )
    return best_move


def next(r, c):
    global player, x_board, o_board, players
    print(is_game_over(x_board, o_board))
    if button[r][c]["text"] == "" and is_game_over(x_board, o_board) is False:
        if player == players[0]:
            button[r][c]["text"] = player
            x_board = set_bit(x_board, r, c)
            print(x_board)
            t = is_game_over(x_board, o_board)
            if t is False:
                besty = find_best_move(
                    x_board, o_board, max_depth=4, maximizing_player=False
                )
                if besty:
                    button[besty[0]][besty[1]]["text"] = players[1]
                o_board = set_bit(o_board, besty[0], besty[1])
                # player = players[1]
            elif t is True:
                pass
            elif t == "tie":
                pass
        elif player == players[1]:
            button[r][c]["text"] = player
            o_board = set_bit(o_board, r, c)
            t = is_game_over(x_board, o_board)
            print(o_board)
            if t is False:
                player = players[0]
            if t is True:
                pass
            if t == "tie":
                pass


window = tkinter.Tk()
players = ["x", "o"]
player = "x"

button = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

frame = tkinter.Frame(window)
frame.pack()

for r in range(8):
    for c in range(8):
        button[r][c] = tkinter.Button(
            frame,
            text="",
            font=("consolas"),
            width=5,
            height=2,
            command=lambda r=r, c=c: next(r, c),
        )
        button[r][c].grid(row=r, column=c)

window.mainloop()
