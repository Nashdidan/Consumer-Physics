from Logger.logHandler import create_log
from mapNameProb import MapNameProb
from oneEditApart import OneEditApart

logger = create_log()

name_prob_map = {"Amit": 0.3, "Tamar": 0.2, "Yaron": 0.5}

map_name_prob = MapNameProb(logger)
map_name_prob.print_prob(100, name_prob_map)

one = OneEditApart(logger)
print(one.is_one_edit_apart("asdf", "jasdfss"))