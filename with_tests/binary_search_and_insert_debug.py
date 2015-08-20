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

# This version is the debugging monstrosity that I reached by the end of it.

class ItemQueue(object):
    def __init__(self):
        self.stack = []

    def insert(self, tup):
        self.staged_tup = tup
        print '\n\n\n'
        print '    NEW TUPLE = '
        print self.staged_tup
        self.timestamp = tup[1]
        self.temp_stack = []
        for i in range(len(self.stack)):
            chunk = self.stack[i]
            to_add = chunk[1]
            self.temp_stack.append(to_add)

        print 'len(temp_stack) = '
        print len(self.temp_stack)
        print 'len(stack) = '
        print len(self.stack)
        print 'and here\'s EXACTLY what the stack looks like:'
        print self.stack

        if len(self.temp_stack) == 0:
            self.stack.insert(0,self.staged_tup)
            print '    inserted tuple at index: '
            print self.staged_tup
            print 0

        elif len(self.temp_stack) == 1:
            comp = self.timestamp > self.temp_stack[0]
            if comp == True:
                print '    this timestamp was >:'
                print self.stack[0]
                self.stack.insert(0,self.staged_tup)
                print '    inserted tuple at index: '
                print self.staged_tup
                print 0
            else:
                print '    this timestamp was NOT > :'
                print self.stack[0]
                self.stack.append(self.staged_tup)
                print '    inserted tuple at index: '
                print self.staged_tup
                print 1

        elif len(self.temp_stack) == 2:
            comp = self.timestamp > self.temp_stack[0]
            if comp == True:
                print '    this timestamp was >:'
                print self.stack[0]
                self.stack.insert(0,self.staged_tup)
                print '    inserted tuple at index: '
                print self.staged_tup
                print 0
            else:
                comp = self.timestamp > self.temp_stack[1]
                if comp == True:
                    self.stack.insert(1,self.staged_tup)
                    print '    inserted tuple at index: '
                    print self.staged_tup
                    print 1
                else:
                    self.stack.append(self.staged_tup)
                    print '    appended tuple at index: '
                    print self.staged_tup
                    print len(self.stack)

        else:
            print '\n\n    Entering initial compare block.'
            print '    Since len(self.stack) > 2, let\'s cut and compare!'
            maximum = len(self.temp_stack)
            minimum = 0
            first_mid = ((maximum - minimum) // 2)
            print 'len(stack) ='
            print len(self.temp_stack)
            print 'initial midpoint = '
            print first_mid
            first_direction = self.timestamp > self.temp_stack[first_mid]
            print '    first direction = '
            print first_direction
            if first_direction == False:
                print 'Since first_direction = False, let\'s move up next_minimum.'
                minimum = first_mid
                print 'Heavy lifting! Next_midpoint should be to the right!'
                next_mid = (((maximum - minimum) // 2) + minimum)
                print 'Now min/max = '
                print minimum
                print maximum
                print 'And next_mid ='
                print next_mid

            else:
                print 'Since first_direction = True, let\'s make sure that'
                print 'our next min/max are correct'
                maximum = first_mid
                print 'Heavy lifting! Next_midpoint should be LEFT!'
                next_mid = ((maximum - minimum) // 2)
                print 'Now min/max = '
                print minimum
                print maximum
                print 'And next_mid = '
                print next_mid
            print '    entering the real recursion!\n\n'
            self.comp_check(maximum, minimum, next_mid)
            # Shoehorn the tuple
            self.stack.insert(self.target_index, self.staged_tup)
            print 'inserted tuple at index: '
            print self.staged_tup
            print self.target_index

    def comp_check(self, maximum, minimum, mid):
        print '\n    Top of comp_check!'
        if (maximum - minimum) >= 2:
            print '    Top of big_len block!\n'
            length = (maximum - minimum)
            print 'does current length make sense?'
            print length
            print 'range of this check is >= 2'
            print 'sanity check - current min/max are: '
            print minimum
            print maximum
            print 'and the incoming midpoint should make sense:'
            midpoint = mid
            print midpoint
            print 'now checking timestamp'
            print self.timestamp
            print 'against that midpoint\'s value'
            print self.temp_stack[midpoint]
            direction = self.timestamp > self.temp_stack[midpoint]
            print 'Next direction = '
            print direction
            if direction == False:
                print 'We\'re MOVING RIGHT!'
                next_minimum = midpoint
                print 'calibrating next_minimum as current mid:'
                print next_minimum
                # if length is even:
                if length % 2 == 0:
                    print 'this bracket LENGTH is EVEN'
                    next_maximum = next_minimum + (length // 2)
                    print 'so next maximum ='
                    print next_maximum
                # if not, the next one fucking well will be:
                elif length % 2 != 0:
                    print 'this bracket LENGTH is ODD'
                    next_maximum = next_minimum + ((length + 1) // 2)
                    print 'so we calibrate next_maximum as:'
                    print 'next min + ((length + 1) // 2), which is:'
                    print next_maximum
                if next_maximum > len(self.temp_stack):
                    print '...but that was too far in THIS case, so we dial it back:'
                    next_maximum = len(self.temp_stack)
                    print 'next max now ='
                    print next_maximum

                next_mid = (((next_maximum - next_minimum) // 2) + next_minimum)
                print 'And thus the next_mid ='
                print next_mid
            else:
                print 'We\'re moving LEFT!'
                next_maximum = midpoint
                print 'calibrating next_maximum as current mid:'
                print next_maximum
                # if length is even:
                if length % 2 == 0:
                    print 'This bracket length was EVEN'
                    next_minimum = next_maximum - (length // 2)
                    print 'so next minimum ='
                    print next_minimum
                # then it is now:
                elif length % 2 != 0:
                    print 'This bracket length was ODD'
                    next_minimum = next_maximum - ((length + 1) // 2)
                    print 'so we calibrate the next minimum as:'
                    print 'next max - ((length + 1) // 2), which is:'
                    print next_minimum
                if next_minimum < 0:
                    print '...but that was too far in THIS case, so we dial it back:'
                    next_minimum = 0
                    print 'next min now ='
                    print next_minimum

                next_mid = (((next_maximum - next_minimum) // 2) + next_minimum)
                print 'And thus the next_mid = '
                print next_mid

            print 'Entering the next recursion:'
            self.comp_check(next_maximum, next_minimum, next_mid)

        elif (maximum - minimum) == 1:

            print '    I\'m in comp_check, and we\'re down to range 1!'
            print 'right now, min/max are:'
            print minimum
            print maximum
            print 'current midpoint should make sense:'
            print 'in fact I think it should always == minimum?'
            midpoint = mid
            print midpoint
            print 'now I am comparing self.timestamp:'
            print self.timestamp
            print 'to current midpoint:'
            print self.temp_stack[midpoint]
            comp = self.timestamp > self.temp_stack[midpoint]
            # if the timestamp is SMALLER (older) than mid:
            if comp == False:
                print 'comp is False, so timestamp is OLDER, so now I\'m'
                # check the right-hand neighbor:
                n_index = midpoint + 1
                if n_index >= len(self.temp_stack):
                    n_index = midpoint
                n_value = self.temp_stack[n_index]
                print 're-calibrating comp with that guy...'
                comp = self.timestamp > n_value
                # if comp is somehow still smaller, stick it to the right!
                if comp == False:
                    print 'comp is STILL FALSE, so timestamp is YET OLDER...'
                    self.target_index = n_index + 1
                    print 'so I just set target_index beyond the neighbor: '
                    print self.target_index
                # if it's greater (younger), stick it to the left!
                else:
                    print 'after checking neighbor, timestamp was YOUNGER!'
                    self.target_index = n_index
                    print 'so I just set target_index to neighbor, bumping him: '
                    print self.target_index
            # if the timestamp is GREATER (younger) than min:
            else:
                print 'comp is True, so timestamp is YOUNGER (greater). Easy Left!'
                # just stick it to the left!
                self.target_index = minimum
                print 'I just set target_index to minimum: '
                print self.target_index

    def break_it_off(self):
        return self.stack.pop()


### TEST THE LIMITS ###
shtack = ItemQueue()

incoming_barrage = [
('magic',1),
('sneaky pete',0.9),
('beast_mode',33),
('gan bei',44),
('wang zi cheng long',55),
('R + L = J',66),
('swim horse',100),
('I say Geneva, you hear Helsinki',25),
('sneaky pete\'s brother, stealthy herbert',0.8),
('Oakland Bordello and Auto Shop, how may we service your parts?',1.000001),
('scrum-diddly-umptious',1.00001),
('infixes',1000),
('ship it!',999),
('PAIN_CHECK',3),
('more_hate',2),
('coup_de_grace',0.5)
]

for tup in range(len(incoming_barrage)):
    shtack.insert(incoming_barrage[tup])

from random import randint
additional_hell_list = []
for n in range(200):
    additional_hell_list.append(('extra',randint(1,200)))


last_kick = ('finish him!',0.001)
additional_hell_list.append(last_kick)

for tup in range(len(additional_hell_list)):
    shtack.insert(additional_hell_list[tup])
print '\n\n    Test Results:\n\n'
print shtack.stack
print '\n\n    Pop, lock and drop it:\n\n'
for cork in range(len(shtack.stack)):
    print shtack.break_it_off()
