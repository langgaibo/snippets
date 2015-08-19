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


##### Let's Test It! #####

shtack = ItemQueue()

# The real purpose of the class is to handle "mostly in order" tuples,
#  but still maintaining sort order when random timestamps are not punctual.
incoming_barrage = [
('magic',1),
('beast_mode',33),
('gan bei',44),
('wang zi cheng long',55),
('R + L = J',66),
('swim horse',100),
('I say Geneva, you hear Helsinki',25),
('Oakland Bordello and Auto Shop, how may we service your parts?',1.000001),
('scrum-diddly-umptious',1.00001),
('infixes',1000),
('ship it!',999)
]

for tup in range(len(incoming_barrage)):
    shtack.insert(incoming_barrage[tup])

# How are things coming along here?
print shtack.stack

# Make it rain for a minute
for cork in range(5):
    dee_bug = shtack.break_it_off()
    print dee_bug

# How you like me now?
print shtack.stack
