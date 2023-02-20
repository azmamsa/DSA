class DisjointSet:
    def __init__(self):
        self.data = {}
        self.num_sets = 0
        self.sizes = {}

    def make_set(self, x):
        if x in self.data:
            return False

        self.data[x] = x
        self.num_sets += 1
        self.sizes[x] = 1

        return True

    def find_set(self, x):
        if x not in self.data:
            return None

        if self.data[x] == x:
            return x

        self.data[x] = self.find_set(self.data[x])

        return self.data[x]

    def union_set(self, x, y):
        root_x = self.find_set(x)
        root_y = self.find_set(y)

        if root_x is None or root_y is None:
            return False

        if root_x == root_y:
            return False

        if self.sizes[root_x] >= self.sizes[root_y]:
            self.data[root_y] = root_x
            self.sizes[root_x] += self.sizes[root_y]
        else:
            self.data[root_x] = root_y
            self.sizes[root_y] += self.sizes[root_x]

        self.num_sets -= 1

        return True

    def get_num_sets(self):
        return self.num_sets

    def get_set_size(self, x):
        root = self.find_set(x)

        if root is None:
            return 0

        return self.sizes[root]

    def __len__(self):
        return len(self.data)
