from xypath import DOWN, UP, LEFT, RIGHT
import bake
from hamcrest import *
OBS = -9
DATAMARKER = -8
STATUNIT = -7
MEASURETYPE = -6
UNITMULTIPLIER = -5
UNITOFMEASURE = -4
GEOG = -3
TIME = -2
TIMEUNIT = -1
STATPOP = 0

ABOVE = UP
BELOW = DOWN

DIRECTLY = True
CLOSEST = False

PARAMS = lambda: bake.Opt.params
