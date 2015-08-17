# coding: utf8
# 朗盖博 2015

# expects zippable lists
class Zip_Print(object):
    def __init__(self, *args):
        self.receipt = zip(*args)

    # prints the zipped block, line by line
    def paper(self):
        for line in self.receipt:
            temp = []
            for chunk in line:
                temp.append(str(chunk))
            print temp

    # returns the zipped block within a list
    def holodisk(self):
        self.block = []
        for line in self.receipt:
            temp = []
            for chunk in line:
                temp.append(str(chunk))
            self.block.append(temp)
        return self.block
