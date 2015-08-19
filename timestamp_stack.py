# coding: utf8
# 朗盖博 2015

# Class stores a list of items
# each item will have 2 things:
# 1. item1
# 2. timestamp
# Every time user of class calls get method on the class,
# it should give out item1 with the oldest timestamp.
# Class should also have method to put item into the class

class ItemQueue(object):
    def __init__(self):
        self.bucket = []

    # main insert finds index and pushes there
    def insert(self, pack):
        self.staged_tup = pack
        self.when = pack[1]
        self.get_index(self.bucket,self.when)
        self.bucket.insert(self.target_index,self.staged_tup)

# note: import time
# note: when will be in mk time

    def get_index(self, bucket, timestamp):
        import bisect
        temp_bucket = []
        for i in range(len(bucket)):
            chunk = bucket[i]
            to_add = chunk[1]
            temp_bucket.append(to_add)
        self.target_index = bisect.bisect_left(temp_bucket, timestamp, lo=0, hi=len(temp_bucket))

    def bust_a_nut(self):
        return self.bucket.pop(0)


##### Let's Test It! #####

dingus = ItemQueue()

tup1 = ('a_fart',1)
tup2 = ('fucking_asshole',33)
tup3 = ('cunt',44)
tup4 = ('prick',55)
tup5 = ('dog_shit',66)
tup6 = ('taint_whiff',100)
tup7 = ('delayed_queef',25)
tup8 = ('some_new_shit',1.000001)
tup9 = ('a_dick',1.00001)
tup10 = ('big_shit',1000)
tup11 = ('slightly_less_big_shit',999)

dingus.insert(tup1)
dingus.insert(tup2)
dingus.insert(tup3)
dingus.insert(tup4)
dingus.insert(tup5)
dingus.insert(tup6)
dingus.insert(tup7)
dingus.insert(tup8)
dingus.insert(tup9)
dingus.insert(tup10)
dingus.insert(tup11)

print dingus.bucket

check1 = dingus.bust_a_nut()
check2 = dingus.bust_a_nut()
check3 = dingus.bust_a_nut()
check4 = dingus.bust_a_nut()
check5 = dingus.bust_a_nut()


print check1
print check2
print check3
print check4
print check5

print dingus.bucket
