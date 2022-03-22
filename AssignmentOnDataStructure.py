class DataStructureModules:
    def duplicateInfo(self,multiList):
        try:
            check=multiList[0][0]
            for singleList in multiList:
                if len(singleList)!=len(set(singleList)):
                    tempDict={i:singleList.count(i) for i in singleList}
                    c=0
                    for check in tempDict:
                        if str(tempDict[check])!="1":
                            c+=1
                    dup=0
                    for key in tempDict:
                        if str(tempDict[key])!="1":
                            dup+=1
                            if dup!=c:
                                 print(key,str("->"),tempDict[key],",",end=' ')
                            else:
                                print(key,"->",tempDict[key],end=" ")
                    print()
        except:
            print("Invalid Input: Please provide the Multi List")

    def mergeList(self,l1,l2):
        res=[]
        for i in l1:
            for j in l2:
                res.append(str(i)+" "+str(j))
        print(res)

    def insertInMiddleOfMultiList(self,list1,list2):
        list3 = list1[2]
        list4 = list3[1]
        list5 = list4[2]
        list5.extend(list2)
        print(list1)

    def mergeDictionary(self,dict1,dict2):
        dict1.update(dict2)
        print(dict1)

    def mapDictionary(self,keys,value):
        if len(keys)==len(value) and isinstance(keys,list) and isinstance(value,list):
            dictionary = {}
            for i in range(0, len(keys)):
                dictionary[keys[i]] = value[i]
            print(dictionary)
        else:
            print("INVALID INPUT(S)")



    def replaceKeyInDict(self,dict,oldKey,newKey):
        print("Input Dictionary:",dict)
        dict[newKey]=dict.pop(oldKey)
        print("Updated Dictionary:",dict)

    def dictToList(self,dict):
        list2 = []
        for i in dict.keys():
            list1 = []
            list1.append(i)
            for j in dict[i]:
                list1.append(j)
            list2.append(list1)
        print(list2)

obj1=DataStructureModules()

print("--------------------------task 1---------------------------------------")
input=[[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
obj1.duplicateInfo(input)
print("--------------------------task 2---------------------------------------")
obj1.mergeList(["Hello","Sir","Test"],["Hello","Google"])
print("--------------------------task 3---------------------------------------")
list1=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
list2=["h","i","j"]
obj1.insertInMiddleOfMultiList(list1,list2)
print("--------------------------task 4---------------------------------------")
keys = ["Ten","Twenty","Thirty"]
value = [10, 20, 30]
obj1.mapDictionary(keys,value)
print("--------------------------task 5---------------------------------------")
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
obj1.mergeDictionary(dict1,dict2)
print("--------------------------task 6---------------------------------------")
myDictionary={"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
obj1.replaceKeyInDict(myDictionary,"city","location")
print("--------------------------task 8---------------------------------------")
dict = {"HuEx":[1, 3, 4],"is":[7, 6],"best":[4,5]}
obj1.dictToList(dict)
print("--------------------------END---------------------------------------")