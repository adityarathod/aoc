import re


class Solution:
    def __init__(self, input_file='2020/day2.txt'):
        with open(input_file, 'r') as f:
            self.input = f.read().split('\n')
            mt = re.compile('^(\d+)-(\d+) (\w)\: (\w+)')
            self.input = [mt.search(line).groups() for line in self.input]

    def validate_p1(password_tuple):
        min_c, max_c, c, password = password_tuple
        min_c, max_c = int(min_c), int(max_c)
        c_count = password.count(c)
        return c_count >= min_c and c_count <= max_c

    def part_one(self):
        return len(list(filter(Solution.validate_p1, self.input)))

    def validate_p2(password_tuple):
        a, b, c, password = password_tuple
        a, b = int(a) - 1, int(b) - 1
        return bool(password[a] == c) ^ bool(password[b] == c)

    def part_two(self):
        return len(list(filter(Solution.validate_p2, self.input)))


if __name__ == "__main__":
    solution = Solution()
    print('Part 1: ', solution.part_one())
    print('Part 2: ', solution.part_two())
