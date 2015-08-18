# coding: utf8
# 朗盖博 2015
from random import randint

# This class provides a clean way to generate and use a D&D statblock.
# For flexibility, the class has methods for changing its initial stats,
# or rolling alternates as needed.

# Class inits with a list of rolled stats
class Stats(object):
    def __init__(self):
        self.rolls = [self.basestat() for i in range(6)]

    # roll 4 d20, discard lowest, and return sum
    def basestat(self):
        baseroll = [randint(1,6) for i in range(4)]
        delroll = min(baseroll)
        baseroll.remove(delroll)
        basestat = sum(baseroll)
        return basestat

    # give up the goods
    def get(self):
        return self.rolls

    # for flexibility depending on how class is called,
    # there are 2 methods for rerolling.
    # if the instance's initial rolls need to be changed:
    def reroll_base(self):
        self.rolls = [self.basestat() for i in range(6)]

    # if the initial rolls need to be preserved:
    def alt_roll(self):
        self.alt_roll = [self.basestat() for i in range(6)]
        return self.alt_roll

derp = Stats()
print 'Dynamic rolls at first:'
print derp.rolls

print 'Rolls instanced: '
attempt = derp.get()
print attempt

print 'Dynamic rolls unchanged by alt_roll(): '
print derp.rolls
alt = derp.alt_roll()
print alt
print derp.rolls

print 'Dynamic rolls changed by reroll_base(): '
print derp.rolls
derp.reroll_base()
print derp.rolls

print 'Original instance of rolls was preserved: '
print attempt
