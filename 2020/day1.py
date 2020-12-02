from functools import reduce


class Solution:
    def __init__(self, input_file='2020/day1.txt'):
        with open(input_file, 'r') as f:
            self.input = list(map(int, f.read().split('\n')))
            self.input_set = set(self.input)

    def part_one(self):
        nums = list(filter(lambda x: 2020 - x in self.input_set, self.input))
        return reduce(lambda x, y: x * y, nums)

    def part_two(self):
        # yes, this is O(n^3) but I'm lazy
        for i in range(len(self.input)):
            for j in range(i, len(self.input)):
                for k in range(j, len(self.input)):
                    if self.input[i] + self.input[j] + self.input[k] == 2020:
                        return self.input[i] * self.input[j] * self.input[k]


if __name__ == "__main__":
    solution = Solution()
    print('Part 1: ', solution.part_one())
    print('Part 2: ', solution.part_two())
