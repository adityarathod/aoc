from functools import reduce


class Solution:
    def __init__(self, input_file='2020/day3.txt'):
        with open(input_file, 'r') as f:
            self.input = [list(x) for x in f.read().split('\n')]
            self.height = len(self.input)
            self.width = len(self.input[0])

    def stride_check(self, col_stride=3, row_stride=1):
        # Stride checking function. Returns trees hit in a run starting from top left and moving
        # col_stride units right and row_stride units down.
        # Generate indices to check
        ri = list(range(0, self.height, row_stride))
        ci = list(map(
            lambda x: x if x < self.width else (x % self.width),
            range(0, col_stride * self.height, col_stride)
        ))
        # Check indices, filter out non-tree cells
        tree_spots = list(filter(
            lambda z: self.input[z[0]][z[1]] == '#',
            zip(ri, ci)
        ))
        # Return number of non-tree cells
        return len(tree_spots)

    def part_one(self):
        return self.stride_check()

    def part_two(self):
        # Try all specified strides
        strides = [
            self.stride_check(1, 1),
            self.stride_check(3, 1),
            self.stride_check(5, 1),
            self.stride_check(7, 1),
            self.stride_check(1, 2),
        ]
        # Return product of trees hit of all strides
        return reduce(lambda x, y: x * y, strides)


if __name__ == "__main__":
    solution = Solution()
    print('Part 1: ', solution.part_one())
    print('Part 2: ', solution.part_two())
