from Logger.logHandler import create_log
from mapNameProb import MapNameProb
from oneEditApart import OneEditApart

logger = create_log()

map_name_prob = MapNameProb(logger)
map_name_prob.test()

one = OneEditApart(logger)
one.test()
