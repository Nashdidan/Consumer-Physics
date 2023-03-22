import logging

from mapNameProb import MapNameProb

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('logfile.log')

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

name_prob_map = {"Amit": 0.3, "Tamar": 0.2, "Yaron": 0.5}

map_name_prob = MapNameProb(logger)
map_name_prob.print_prob(100, name_prob_map)