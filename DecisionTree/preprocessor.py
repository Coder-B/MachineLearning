from bean import Sample

def loadSampleFromLine(line):
    array = line.split(",")
    attributeVals = list()
    index = 0
    while index < len(array)-1:
        attributeVals.append(array[index])
        index += 1
    return Sample(attributeVals,array[len(array)-1])


def loadSamples():
    attributeLine = True
    samples = list()
    for line in open("./watermelon.log",'r', encoding='UTF-8'):
        if attributeLine:
            attributeLine = False
            continue
        else:
            samples.append(loadSampleFromLine(line.rstrip('\n')))
    return samples

def initAttributes(sample):
    attributes = list()
    index = 0
    while index < len(sample.attributeVals):
        attributes.append(index)
        index+=1
    return attributes
