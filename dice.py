# coding: utf8
# 朗盖博 2015

from random import randint

# inits gently
class Dice(object):
	def __init__(self):
		pass

	# expects num_sides, num_dice
	def roll(self, num_sides, num_dice):
		# wipe the slate
		self.num_sides = None
		self.num_dice = None
		self.rolls = None
		self.sum = None
		self.pack = []

		# box it to d6 if they're getting crazy
		if num_sides >= 1001:
			self.num_sides = 6
		elif num_sides <= 1:
			self.num_sides = 6
		else:
			self.num_sides = int(num_sides)

		# box it to 1 die if they're getting crazy
		if num_dice >= 1001:
			self.num_dice = 1
		elif num_dice <= 0:
			self.num_dice = 1
		else:
			self.num_dice = int(num_dice)

		# roll 'em
		self.rolls = [ randint(1,self.num_sides) for self.num_dice in range(0,self.num_dice)]

		# sum 'em
		self.sum = sum(self.rolls)

		# list instead of tuple for flexibility
		self.pack = [self.rolls, self.sum]
		return self.pack
