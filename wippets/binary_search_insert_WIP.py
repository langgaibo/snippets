# coding: utf8
# 朗盖博 2015

class ItemQueue(object):
    def __init__(self):
        self.bucket = []

    # main insert finds index and pushes there
    def insert(self, what, when):
        self.staged_tup = (what,when)
        self.get_index(self.bucket,when)
        self.bucket.insert(self.target_index,self.staged_tup)

'''
IMPORTANT
I have to maintain a count of how many loops have been pulled by the recursive
search, in order to translate the mini-list index into the final index.
And I guess even a count isn't enough, I need some kind of map to retrace
my steps.
'''

    def get_index(self, bucket, timestamp):
        # start with an empty list
        temp_bucket = []
        # fill it with the incoming list
        for i in range(len(bucket)):
            temp_bucket.append(bucket[i])
        # cleaver = midpoint index of current list
        cleaver = temp_bucket.index(temp_bucket[(len(temp_bucket) / 2)])
        # get the tuple at list[cleaver]
        apple = temp_bucket[cleaver]
        # get the timestamp from that tuple
        to_check = apple[1]
        # compare timestamp against the apple timestamp
        comp = timestamp >= to_check

        # Here's the magic. If the timestamp is SMALLER (older):
        if comp = False:
            # then repeat the check on the older neighbor index (i.e. right-hand)
            neighbor = cleaver + 1
            orange = temp_bucket[neighbor]
            next_check = orange[1]
            # and if the timestamp is still OLDER THAN THE NEIGHBOR:
            if comp >= next_check = False:
                # cut the working list in half:
                transfer_bucket = []
                for i in range(neighbor,len(temp_bucket)):
                    transfer_bucket.append(temp_bucket[i])
                # and run this whole thing again.
                # this recursively jumps to and checks the midpoint
                # value of each half-list.
                self.get_index(transfer_bucket, timestamp)
            # if the timestamp IS YOUNGER than the neighbor,
            # the tuple should be inserted at that index in the main list.
            else:
                ''' WRONG WRONG WRONG BAD BAD BAD '''
                self.target_index = neighbor


        elif comp = True:
            neighbor = cleaver - 1
            orange = temp_bucket[neighbor]
            next_check = orange[1]
            if comp >= next_check = True:
                transfer_bucket = []
                for i in range(0,(neighbor):
                    transfer_bucket.append(temp_bucket[i])
                self.get_index(transfer_bucket, timestamp)
            else:
                ''' WRONG WRONG WRONG BAD BAD BAD '''
                if neighbor <= 0:
                    self.target_index = -1
                else:
                    self.target_index = neighbor
