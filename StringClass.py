import itertools
class StringClass:
    def __init__(self,name):
        self.name=name
        print("Object has created with the string:", self.name)
    def getLength(self):
        print("Length of the String is:",len(self.name))
    def convertStringToChar(self,inputString):
        #print("String to Char result:",list(inputString))
        return list(inputString)
'''
obj1=StringClass("HashedIn Technologies")
obj1.getLength()
print(obj1.convertStringToChar("Test"))
'''

class PairsPossible(StringClass):
    def storeListOfData(self):
        self.bucket=list(itertools.permutations(self.name))
        l=[]
        for i in self.bucket:
            s=""
            for j in i:
                s+=str(j)
            l.append(s)
        removeDuplicates=set(l)
        self.bucket=list(removeDuplicates)
        #print("Data has been stored in the form of list as:",self.bucket)
        return self.bucket
    def getStoredData(self):
        temp=""
        for i in range(len(self.bucket)):
            if i<len(self.bucket)-1:
                temp+=str(self.bucket[i])+" "
            else:
                temp+=str(self.bucket[i])
        return temp

class SearchCommonElements(PairsPossible):
    pass

testObj1=PairsPossible("123")  #intialize the pairspossible with base constructor
testObj1.getLength()    #produce the length of the contructor string
print(testObj1.convertStringToChar("200"))  #Convert string to char in the form of Char List
print(testObj1.storeListOfData())  #Store data in the form of list
print(testObj1.getStoredData())  #produce the list of stored data with delemiter as space