# 获取单一sample在attributeArray上的投影
def extractSampleValOnAttributes(sample, attributeArray):
    targetList = list()
    for index in xrange(0,len(attributeArray)):
        attributeIndex = attributeArray[index]
        targetList.append(sample.attributeVals[attributeIndex])
    return targetList

# samples在attributeArray上的投影是否相同
def samplesSameOnAttributes(samples, attributeArray):
    attributeVals = list()
    if len(samples) == 0 :
        return False
    else:
    	# 如果samples不为空，将第一个sample的feature取出来
        attributeVals = extractSampleValOnAttributes(samples[0],attributeArray)
    # 逐一比较所有samples
    for item in samples:
        isItemSame = True
        # 针对每个sample的每个feature值进行比对
        if extractSampleValOnAttributes(item,attributeArray) != attributeVals :
            return False
    return True

# samples的label是否相同，是否属于一个类别
def samplesInOneCategory(samples):
    if len(samples) == 0 :
        return False
    else:
        for item in samples:
           if item.label != samples[0].label :
               return False
        return True

# 获取samples在attribute上的值，去重
def extractValOnAttribute(samples, attribute):
    valSet = set()
    for item in samples:
        valSet.add(item.attributeVals[attribute])
    return valSet

# 获取samples中在attributeArray上的值，去重
def extractValOnAttributeArray(samples, attributeArray):
    attributeValDict = dict()
    for attribute in attributeArray:
        attributeValDict[attribute] = extractValOnAttribute(samples, attribute)
    return attributeValDict

# 获取samples 的子集，其中attribute值为attributeVal
def filterSubsetOnAttributeVal(samples, attribute, attributeVal):
    subset = list()
    for item in samples:
        if item.attributeVals[attribute] == attributeVal :
            subset.add(item)
    return subset

# 基于attribute值对samples进行划分
def divideSamplesOnAttribute(samples,attribute):
    divideDict = dict()
    for item in samples:
        val = item.attributeVals[attribute]
        if val not in divideDict:
            divideDict[val] = list()
        divideDict[val].add(item)
    return divideDict


# 统计samples 中样本数最多的label
def determineCategoryInSamples(samples):
    categoryDict = dict()
    for item in samples:
        label = item.label 
        if label in categoryDict:
            categoryDict[label]+=1
        else :
            categoryDict[label] = 1
    max_label = 'init'
    for label in categoryDict:
        if categoryDict[label] > categoryDict[max_label] :
            max_label = label
    return max_label

# 计算不同类别及各自占比
def computeCategoryPercent(samples):
    categoryDict = dict()
    for item in samples:
        label = item.label 
        if label in categoryDict :
            categoryDict[label]+=1
        else :
            categoryDict[label] = 1
    for label in categoryDict:
       categoryDict[label] = categoryDict[label]/len(samples)
    return categoryDict