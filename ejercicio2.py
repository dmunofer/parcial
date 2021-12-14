import math
import os
import random
import re
import sys

def verticalRooks(r1, r2):
    or_exclusivo = 0
    for x, y in zip(r1,r2):
        or_exclusivo^= (abs(x-y)-1)
    if or_exclusivo!=0:
        return 'player 2'
    else:
        return 'player 1'

