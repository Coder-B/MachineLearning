from bean import Sample
from bean import Node
import utils

samples = loadSamples()
attributes = initAttributes()

def TreeGenerate(samples,attributes):
    node = Node()
    if utils.samplesInOneCategory(samples) :
        node.selfCategory = samples[0].label
        return
    if attributes is None or 0 == len(attributes) or utils.samplesSameOnAttributes(samples,attributes) :
        # 将node标记为叶节点，其类别标记为samples中样本数最多的类
        node.selfCategory = 'most in samples'
        return
    # 选择最优划分属性
    bestAttribute = findBestAttribute(attributes)
    attributeVal = utils.extractValOnAttribute(samples,bestAttribute)
    