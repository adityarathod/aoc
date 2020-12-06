from functools import reduce


class Solution:
    def __init__(self, input_file='2020/day6.txt'):
        with open(input_file, 'r') as f:
            self.input = f.read().split('\n\n')
            self.group_set = [set(x.replace('\n', '')) for x in self.input]

    def part_one(self):
        ypg = [len(x) for x in self.group_set]
        return sum(ypg)

    def part_two(self):
        def process_member(group):
            t = list(reduce(lambda a, b: a.intersection(b), [
                set(x) for x in group.split('\n')]))
            return len(t)
        return sum(map(process_member, self.input))


if __name__ == "__main__":
    solution = Solution()
    print('Part 1: ', solution.part_one())
    print('Part 2: ', solution.part_two())
