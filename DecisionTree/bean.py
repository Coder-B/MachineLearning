class Sample:
    def  __init__(self, attributeVals, label):
        self.attributeVals = attributeVals
        self.label = label

class Node:
    children = list()
    def __init__(self, parent = None, selfJudge = None, selfCategory = None):
        self.parent = parent
        self.selfJudge = selfJudge
        self.selfCategory = selfCategory

    def addChild(child):
        self.children.append(child)