from logging import Logger

from mapNameProb import MapNameProb
from oneEditApart import OneEditApart


class Test:

    @staticmethod
    def run_all_tests(logger: Logger):

        one_edit_apart = OneEditApart(logger)
        map_name_prob = MapNameProb(logger)
        expected_list = [False, True, True, True, True, False, False, True, False]
        ans_list = [one_edit_apart.is_one_edit_apart("cat", "dog"), one_edit_apart.is_one_edit_apart("cat", "cats"),
                    one_edit_apart.is_one_edit_apart("cat", "cut"), one_edit_apart.is_one_edit_apart("cat", "cast"),
                    one_edit_apart.is_one_edit_apart("cat", "at"), one_edit_apart.is_one_edit_apart("cat", "act"),
                    one_edit_apart.is_one_edit_apart("cat", "cat"), one_edit_apart.is_one_edit_apart("asdf", "jasdf"),
                    one_edit_apart.is_one_edit_apart("", "")]

        if ans_list == expected_list:
            logger.info("Pass - One Edit Apart Test")
        else:
            logger.error("Failed - One Edit Apart Test")

        iterations = 100
        error_limit = 30
        name_prob = {"Amit": 0.3, "Tamar": 0.2, "Yaron": 0.5}
        counts = map_name_prob.print_prob(iterations, name_prob)
        error_percentage = map_name_prob.check_error(iterations, name_prob, counts)
        if all(i < error_limit for i in error_percentage.values()):
            logger.info("Pass - Map Name Prob Test {} is lower then {}"
                        .format(error_percentage, error_limit))
        else:
            logger.error("Failed - Map Name Prob Test - error percentage {} is greater then {}"
                         .format(error_percentage, error_limit))
