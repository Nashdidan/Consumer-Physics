from logging import Logger


class OneEditApart:
    def __init__(self, logger: Logger):
        self.logger = logger

    def test(self):
        expected_list = [False, True, True, True, True, False, False, True, False]
        ans_list = []
        ans_list.append(self.is_one_edit_apart("cat", "dog"))
        ans_list.append(self.is_one_edit_apart("cat", "cats"))
        ans_list.append(self.is_one_edit_apart("cat", "cut"))
        ans_list.append(self.is_one_edit_apart("cat", "cast"))
        ans_list.append(self.is_one_edit_apart("cat", "at"))
        ans_list.append(self.is_one_edit_apart("cat", "act"))
        ans_list.append(self.is_one_edit_apart("cat", "cat"))
        ans_list.append(self.is_one_edit_apart("asdf", "jasdf"))
        ans_list.append(self.is_one_edit_apart("", ""))

        if ans_list == expected_list:
            self.logger.info("Pass - One Edit Apart Test")
        else:
            self.logger.error("Failed - One Edit Apart Test")
    def is_one_edit_apart(self, first: str, second: str) -> bool:
        res_list = []
        if not first or not second:
            self.logger.warning("empty strings were given")
            return False

        min_length = min(len(first), len(second))
        max_length = max(len(first), len(second))
        if max_length - min_length > 1:
            return False

        #check first char
        if first[0] != second[0]:
            res_list.append(False)
            if max_length == min_length:
                first = first[1:]
                second = second[1:]
            elif len(first) == max_length:
                first = first[1:]
            else:
                second = second[1:]

        sum_list = sum(res_list + list(map(lambda x: first[x] == second[x], range(min(len(first), len(second))))))

        if sum_list < min_length - 1 or (min_length == max_length and sum_list == min_length):
            return False

        return True
