class SetList:
    class Node:
        def __init__(self, data, set_list, next_node=None, prev_node=None):
            self._data = data
            self._set_list = set_list
            self._next = next_node
            self._prev = prev_node

        def get_data(self):
            return self._data

        def get_next(self):
            return self._next

        def get_previous(self):
            return self._prev

        def get_set(self):
            return self._set_list

    def __init__(self):
        self._head = None
        self._tail = None

    def get_front(self):
        return self._head

    def get_back(self):
        return self._tail

    def make_set(self, data):
        if self.find_data(data) is not None:
            return None

        if self._head is None:
            new_node = self.Node(data, self)
            self._head = new_node
            self._tail = new_node
            return new_node

        return None

    def find_data(self, data):
        current_node = self._head
        while current_node is not None and current_node.get_data() != data:
            current_node = current_node.get_next()
        return current_node

    def representative_node(self):
        current_node = self._head
        while current_node is not None and current_node.get_set() != self:
            current_node = current_node.get_next()
        return current_node

    def representative(self):
        rep_node = self.representative_node()
        if rep_node is None:
            return None
        else:
            return rep_node.get_data()

    def union_set(self, other_set):
        if self is other_set:
            return
        other_head = other_set.get_front()
        if other_head is None:
            return
        other_tail = other_set.get_back()
        if self._tail is None:
            self._head = other_head
            self._tail = other_tail
        else:
            self._tail._next = other_head
            other_head._prev = self._tail
            self._tail = other_tail
        current_node = other_head
        while current_node is not None:
            current_node._set_list = self
            current_node = current_node.get_next()
        other_set._head = None
        other_set._tail = None

    def __len__(self):
        count = 0
        current_node = self._head
        while current_node is not None:
            count += 1
            current_node = current_node.get_next()
        return count
