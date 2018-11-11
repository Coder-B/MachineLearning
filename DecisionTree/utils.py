
def extractSampleValOnAttributes(sampleVals, attributeArray):
    targetList = list()
    for index in xrange(0,len(attributeArray)):
        attributeIndex = attributeArray[index]
        targetList.append(sampleVals[attributeIndex])
    return targetList

def samplesSameOnAttributes(samples, attributeArray):
    attributeVals = list()
    if len(samples) == 0 :
        return False
    else:
    	# 如果samples不为空，将第一个sample的feature取出来
        attributeVals = extractSampleValOnAttributes(samples[0].attributeVals,attributeArray)
    # 逐一比较所有samples
    for item in samples:
        isItemSame = True
        # 针对每个sample的每个feature值进行比对
        if extractSampleValOnAttributes(item.attributeVals,attributeArray) != attributeVals :
            return False
    return True

def samplesInOneCategory(samples):
    if len(samples) == 0 :
        return False
    else:
        for item in samples:
           if item.label != samples[0].label :
               return False
        return True

def extractValOnAttribute(samples, attribute):
    valSet = {}
    for item in samples:
        valSet.add(item.attributeVals[attribute])
    return valSet