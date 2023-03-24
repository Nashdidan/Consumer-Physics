import random
from logging import Logger
from typing import Dict


class MapNameProb:
    def __init__(self, logger: Logger):
        self.logger = logger

    def _select_name(self, name_prob: Dict[str, int], total_prob: int):
        rand_num = random.uniform(0, total_prob)
        current_prob = 0
        for name, prob in name_prob.items():
            current_prob += prob
            if rand_num <= current_prob:
                return name

    def print_prob(self, iterations: int, name_prob: Dict[str, int]) -> Dict[str, int]:
        counts: Dict[str, int] = {key: 0 for key in name_prob.keys()}
        total_prob = sum(name_prob.values())
        if total_prob != 1:
            self.logger.warning("answer might be faulty because sum of all probabilities not equal to 1")
        for i in range(iterations):
            name = self._select_name(name_prob, total_prob)
            counts[name] += 1

        print(counts)
        return counts

    def check_error(self, iterations: int, name_prob: Dict[str, int], actual_counts: Dict[str, int]) -> Dict[str, int]:
        expected_counts = {name: int(iterations * prob) for name, prob in name_prob.items()}
        error_percentages = {name: abs((actual_counts[name] - expected_counts[name]) / expected_counts[name]) * 100 for
                             name in name_prob}
        # self.logger.info("expected result: {}".format(expected_counts))
        # self.logger.info("error percentage: {}".format(error_percentages))
        return error_percentages
