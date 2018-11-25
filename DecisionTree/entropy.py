import utils
import math
# 计算信息熵
def computeInfoEntropy(samples):
    samplePercentDict = utils.computeCategoryPercent(samples)
    infoEntropy = 0
    for lable in samplePercentDict:
        infoEntropy = infoEntropy - samplePercentDict[lable] * math.log(samplePercentDict[lable],2)
    return infoEntropy


# 计算信息增益
def computeInfoGain(samples,attribute):
    gainEntropy = computeInfoEntropy(samples)
    divideDict = utils.divideSamplesOnAttribute(samples,attribute)
    for attrVal in divideDict:
        gainEntropy = gainEntropy - computeInfoEntropy(divideDict[attrVal]) * len(divideDict[attrVal]) / len(samples)
    return gainEntropy

# 根据信息增益选择最佳分类
def findBestAttribute(samples,attributes):
    maxInfoGain = 0
    bestAttr = attributes[0]
    for item in attributes:
        infoGain = computeInfoGain(samples,item)
        if maxInfoGain < infoGain:
            maxInfoGain = infoGain
            bestAttr = item
    return bestAttr,maxInfoGain