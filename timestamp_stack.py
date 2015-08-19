# coding: utf8
# 朗盖博 2015

# This class acts as a stack.
# It expects incoming tuples in format (value,timestamp).
# It inserts each tuple into the existing stack in such a way
#  that the list order is preserved with list[0] being the oldest tuple,
#  and list[len(list)] being the most recent.

class ItemQueue(object):
    # inits with an empty list
    def __init__(self):
        self.stack = []

    # peels out the timestamp, uses that arg to find insertion point
    #  in the list, and jams the tuple where it hurts so good.
    def insert(self, tup):
        self.staged_tup = tup
        self.timestamp = tup[1]
        self.get_index(self.stack,self.timestamp)
        self.stack.insert(self.target_index,self.staged_tup)

    # bisect is made just for this sort of thing.
    # It tends to sort larger values to higher indices, so later,
    #  we pop from list[0] so we don't have to keep flipping the stack.
    def get_index(self, stack, timestamp):
        import bisect
        # we only care about the time stamps, so we build a new list of just those.
        temp_stack = []
        for i in range(len(stack)):
            chunk = stack[i]
            to_add = chunk[1]
            temp_stack.append(to_add)
        # search and return target insert index, which will be the same # in the real list.
        self.target_index = bisect.bisect_left(temp_stack, timestamp, lo=0, hi=len(temp_stack))

    # pop, lock and drop it
    def break_it_off(self):
        return self.stack.pop(0)
