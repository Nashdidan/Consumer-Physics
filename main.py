from Logger.logHandler import create_log
from mapNameProb import MapNameProb
from oneEditApart import OneEditApart

logger = create_log()

name_prob_map = {"Amit": 0.3, "Tamar": 0.2, "Yaron": 0.5}

map_name_prob = MapNameProb(logger)
map_name_prob.print_prob(100, name_prob_map)

ans_list = []
one = OneEditApart(logger)
ans_list.append(one.is_one_edit_apart("cat", "dog"))
ans_list.append(one.is_one_edit_apart("cat", "cats"))
ans_list.append(one.is_one_edit_apart("cat", "cut"))
ans_list.append(one.is_one_edit_apart("cat", "cast"))
ans_list.append(one.is_one_edit_apart("cat", "at"))
ans_list.append(one.is_one_edit_apart("cat", "act"))
ans_list.append(one.is_one_edit_apart("cat", "cat"))
ans_list.append(one.is_one_edit_apart("asdf", "jasdf"))
print(ans_list)