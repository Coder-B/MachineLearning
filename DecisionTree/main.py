from bean import Sample
from bean import Node
import utils
import preprocessor
import entropy
import time

samples = preprocessor.loadSamples()
attributes = preprocessor.initAttributes(samples[0])
attributeValDict = utils.extractValOnAttributeArray(samples, attributes)

def TreeGenerate(samples,attributes):
    node=Node()
    if utils.samplesInOneCategory(samples) :
        node.selfCategory = samples[0].label
        return node
    if attributes is None or 0 == len(attributes) or utils.samplesSameOnAttributes(samples,attributes) :
        # 将node标记为叶节点，其类别标记为samples中样本数最多的类
        node.selfCategory = utils.determineCategoryInSamples(samples)
        return node

    # 选择最优划分属性
    bestAttribute,maxInfoGain = entropy.findBestAttribute(samples,attributes)
    for attributeVal in attributeValDict[bestAttribute] :
        sampleSubset = utils.filterSubsetOnAttributeVal(samples,bestAttribute,attributeVal)
        subNode = None
        if 0 == len(sampleSubset) :
            subNode = Node()
            subNode.selfCategory = utils.determineCategoryInSamples(samples)
            continue
        else:
            attributes_copy = attributes.copy()
            attributes_copy.remove(bestAttribute)
            attributes_copy.sort()
            subNode = TreeGenerate(sampleSubset,attributes_copy)
        subNode.selfJudge = {bestAttribute: attributeVal}
        node.addChild(subNode)
    return node

rootNode = TreeGenerate(samples,attributes)
rootNode.selfJudge = {}
utils.recursivePrintTree(rootNode,"")
