class Sample:
    def  __init__(self, attributeVals, label):
        self.attributeVals = attributeVals
        self.label = label

class Node:
    def __init__(self, selfJudge = None, selfCategory = None):
        # attribute = val
        self.selfJudge = selfJudge
        # label
        self.selfCategory = selfCategory
        self.children = list()

    def addChild(self,child):
        self.children.append(child)