# Посылка 35023983
import bisect


def max_photo_replica(datacenters_list):
    res = 0
    while len(datacenters_list) > 1:
        datacenters_list = sorted(datacenters_list, reverse=True)
        if datacenters_list[0] > 0 and datacenters_list[-1] > 0:
            datacenters_list[0] -= 1
            datacenters_list[-1] -= 1
            res += 1
        if datacenters_list[-1] == 0:
            datacenters_list.pop()
        if datacenters_list[0] == 0:
            datacenters_list.pop(0)
    return res


class Stack:
    def __init__(self):
        self.stack = []

    def __bool__(self):
        return bool(self.stack)

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def length(self):
        return len(self.stack)


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, elem):
        self.s1.push(elem)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def is_empty(self):
        return min(self.s1.is_empty(), self.s2.is_empty())

    def length(self):
        return self.s1.length() + self.s2.length()


def max_photo_replica_queue(capacities):
    capacities = sorted(capacities, reverse=True)
    dc_queue = Queue()
    global_max = -9999999999
    global_min = 9999999999
    for el in capacities:
        dc_queue.push(el)
        if el >= global_max:
            global_max = el
        if el <= global_min:
            global_min = el
    res = 0

    while dc_queue.length() > 1:
        first = dc_queue.pop()
        second = dc_queue.pop()
        if first > 0 and second > 0:
            res += min(first, second)
            to_be_pushed = max(first, second) - min(first, second)
            if to_be_pushed > 0:
                dc_queue.push(to_be_pushed)
    return res


def bisect_approach(capacities):
    capacities = sorted(capacities)
    res = 0
    while len(capacities) > 1:
        while len(capacities) >= 1 and capacities[0] == 0:
            capacities.pop(0)
        while len(capacities) >= 1 and capacities[-1] == 0:
            capacities.pop()
        if len(capacities) <= 1:
            return res
        res += 1
        capacities[0] -= 1
        to_be_inserted = capacities[-1] - 1
        capacities.pop()
        bisect.insort(capacities, to_be_inserted)
    return res


if __name__ == '__main__':
    n = input()
    datacenters_capacity = list(map(int, input().split()))
    #print(max_photo_replica_queue(datacenters_capacity))
    #print(max_photo_replica(datacenters_capacity))
    print(bisect_approach(datacenters_capacity))
