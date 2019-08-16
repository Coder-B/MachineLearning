# AdaBoost算法，内容来自《统计学习方法》8.1.2节
from typing import List
import math
class AdaBoostClassifier:
    # data[i] 格式
    # {x:3,y:-1,weight:0.25}
    def __init__(self, data:List) -> None:
        self.data = data
        self.basicClassifiers = []
    # def loadData():
    # 基本分类器的一种。经debug，发现书中的基本分类器不只一种。。。坑爹有点繁琐，大概知道啥意思了
    def predict(self, x:int, threshold: float) -> int:
        if x<threshold:
            return 1
        else:
            return -1
    # 使用当前的基本分类器
    def calculateErrRatio(self, threshold: float) -> float:
        errRatio = 0.0
        for item in self.data:
            if self.predict(item["x"],threshold) != item["y"]:
                item["isExpected"] = False
                errRatio += item["weight"]
                # if threshold == 5.5:
                #     print("x="+str(item["x"])+"; y="+str(item["y"])+"; predictVal="+str(self.predict(item["x"],threshold))+"; weight:"+str(item["weight"]))
            else:
                item["isExpected"] = True
        return errRatio

    # 找到本轮错误率最低的基本分类器，并计算分类器权重，更新样本权重
    def findBasicClassifier(self,round:int) -> None:
        threshold = self.data[0]["x"]
        delta = 0.5
        targetThreshold,targetErrRatio = threshold,1.0
        while threshold <= self.data[len(self.data)-1]["x"]:
            errRatio = self.calculateErrRatio(threshold)
            if errRatio < targetErrRatio:
                targetThreshold = threshold
                targetErrRatio = errRatio
            if round == 3:
                print("threshold: "+str(threshold)+"; errRatio:"+str(errRatio))
            threshold+=delta
        classifier = {"threshold":targetThreshold}
        print("TARGET  threshold: "+str(targetThreshold)+"; errRatio: "+str(targetErrRatio))
        # 用于更新最终状态下的 item["isExpected"]
        self.calculateErrRatio(targetThreshold)
        classifierRatio = self.calculateClassifierRatio(targetErrRatio)
        classifier["ratio"] = classifierRatio
        # print("alpha is "+str(classifierRatio))
        self.basicClassifiers.append(classifier)
        self.updateSampleRatio(classifierRatio)

    # 计算本轮基本分类器权重
    def calculateClassifierRatio(self,errRatio) -> float:
        return math.log(1.0/errRatio - 1)/2

    # 更新样本权重
    def updateSampleRatio(self,classifierRatio:float) -> None:
        totalWeight = 0.0
        for item in self.data:
            factor = 1.0
            if item["isExpected"]:
                factor = math.exp(-1*classifierRatio)
            else:
                factor = math.exp(classifierRatio)
            item["weight"] = factor * item["weight"]
            totalWeight += item["weight"]

        for item in self.data:
            item["weight"] = (item["weight"]/totalWeight)
            # print(item["weight"])

    # 投票分类器，集合各基本分类器，评估效果
    def calculateFinalClassifier(self) -> int:
        errPredict = 0
        for item in self.data:
            x,y=item["x"],item["y"]
            predictRes = 0
            for classifier in self.basicClassifiers:
                predictRes+=self.predict(x,classifier["threshold"])*classifier["ratio"]
            if predictRes*y < 0:
                errPredict+=1
        return errPredict



data = [{"x":0,"y":1},{"x":1,"y":1},{"x":2,"y":1},{"x":3,"y":-1},{"x":4,"y":-1},{"x":5,"y":-1}\
,{"x":6,"y":1},{"x":7,"y":1},{"x":8,"y":1},{"x":9,"y":-1}]
initWeight = 1/float(len(data))
for item in data:
    item["weight"] = initWeight
classifier = AdaBoostClassifier(data)
classifier.findBasicClassifier(1)
print(classifier.basicClassifiers)
print("err predict: "+str(classifier.calculateFinalClassifier()))
print("=======================")
classifier.findBasicClassifier(2)
print(classifier.basicClassifiers)
print("err predict: "+str(classifier.calculateFinalClassifier()))
print("=======================")
classifier.findBasicClassifier(3)
print(classifier.basicClassifiers)
print("err predict: "+str(classifier.calculateFinalClassifier()))
