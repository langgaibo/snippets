# coding: utf8
# 朗盖博 2015

# This Class builds and stores a list as a stack.
# It has 2 primary methods: Insert, and pop.
# For insertion, it expects tuples in the format ('value',timestamp).
# It does a binary search + insert for each tuple.
# The stack is oriented with most recent timestamp at index 0,
# and oldest at the end of the list.

# I wrote the binary search + insert by myself as a challenge.
# Not bad for a guy who didn't know how to print 'hello world'
# or even use a CLI 6 months ago!

class ItemQueue(object):
    def __init__(self):
        self.stack = []

    def insert(self, tup):
        self.staged_tup = tup
        self.timestamp = tup[1]

        # we build temp_stack with just timestamp values
        # this will be our index map for each binary search + insert run
        self.temp_stack = []
        for i in range(len(self.stack)):
            chunk = self.stack[i]
            to_add = chunk[1]
            self.temp_stack.append(to_add)

        # if stack is empty, congratulations, you're the first.
        if len(self.temp_stack) == 0:
            self.stack.insert(0,self.staged_tup)

        # if stack is single, just go left or right.
        elif len(self.temp_stack) == 1:
            comp = self.timestamp > self.temp_stack[0]
            if comp == True:
                self.stack.insert(0,self.staged_tup)
            else:
                self.stack.append(self.staged_tup)

        # here's the meat: from len(stack) >= 2 we do the real bisecting.
        else:
            maximum = len(self.temp_stack)
            minimum = 0
            first_mid = ((maximum - minimum) // 2)
            first_direction = self.timestamp > self.temp_stack[first_mid]
            # go right, set next bracket
            if first_direction == False:
                minimum = first_mid
                next_mid = (((maximum - minimum) // 2) + minimum)
            # go left, set next bracket
            else:
                maximum = first_mid
                next_mid = ((maximum - minimum) // 2)

            self.comp_check(maximum, minimum, next_mid)
            # Shoehorn the tuple at the target index
            self.stack.insert(self.target_index, self.staged_tup)

    def comp_check(self, maximum, minimum, mid):
        # if this bracket is >= 2, target and set up the next bracket
        if (maximum - minimum) >= 2:
            length = (maximum - minimum) # we'll need this later!
            midpoint = mid
            # check the direction of the next search
            direction = self.timestamp > self.temp_stack[midpoint]
            # moving right? then keep the left edge on current mid
            if direction == False:
                next_minimum = midpoint
                if length % 2 == 0:
                    next_maximum = next_minimum + (length // 2)
                # if length is not even, make it even.
                # We don't want the resulting bracket to fall short.
                elif length % 2 != 0:
                    next_maximum = next_minimum + ((length + 1) // 2)
                # but don't fall off the edge!
                if next_maximum > len(self.temp_stack):
                    next_maximum = len(self.temp_stack)
                # calibrate the next midpoint
                next_mid = (((next_maximum - next_minimum) // 2) + next_minimum)

            # moving left? then keep the right edge on current mid
            else:
                next_maximum = midpoint
                if length % 2 == 0:
                    next_minimum = midpoint - (length // 2)
                # again, make sure the next bracket doesn't fall short
                elif length % 2 != 0:
                    next_minimum = midpoint - ((length + 1) // 2)
                # or long...
                if next_minimum < 0:
                    next_minimum = 0
                # calibrate the next midpoint:
                next_mid = (((next_maximum - next_minimum) // 2) + next_minimum)

            self.comp_check(next_maximum, next_minimum, next_mid)

        elif (maximum - minimum) == 1:
            # down to the wire! Now we do some final comparisons and insert.
            # note: by this point, midpoint == minimum.
            midpoint = mid
            comp = self.timestamp > self.temp_stack[midpoint]
            # if the timestamp is SMALLER (older) than mid:
            if comp == False:
                # identify the right-hand neighbor's real position:
                n_index = midpoint + 1
                # cover the literal edge case :)
                if n_index >= len(self.temp_stack):
                    n_index = midpoint
                # compare the neighbor's value
                n_value = self.temp_stack[n_index]
                comp = self.timestamp > n_value
                # if comp is still smaller (older), stick it to the right!
                if comp == False:
                    self.target_index = n_index + 1
                # if it's greater (younger), stick it to the left!
                else:
                    self.target_index = n_index
            # if the timestamp is GREATER (younger) than mid:
            else:
                # just stick it to the left!
                self.target_index = minimum

    def break_it_off(self):
        return self.stack.pop()
