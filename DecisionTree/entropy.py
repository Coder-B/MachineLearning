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