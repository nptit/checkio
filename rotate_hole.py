# https://www.checkio.org/mission/rotate-hole/
__author__ = 'Vitalii K'

import collections


def rotate(state, pipe_numbers):
    result = []
    queue = collections.deque(state)
    for i in range(len(state)):
        if all(queue[i] for i in pipe_numbers):
            result.append(i)
        queue.rotate(1)
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"
