from functools import reduce
class LambdaUsageRepo:
    def quadraticExpession(self,dataStream):
        a,b,c,x = [int(i) for i in dataStream.split(" ")]
        expression = lambda a,b,c,x: print(a*x**2+b*x+c)
        expression(a,b,c,x)

    def countOccurance(self,data):
        tempList=[]
        if isinstance(data,list):
            for i in data:
                tempList.append(list(map(lambda x: x=='A',i)).count(True))
            for i in data:
                tempList.append(list(map(lambda x: x=='a',i)).count(True))
            tempList=reduce(lambda a,b:a+b,tempList)
            print("Count of 'A' and 'a' of given list: ",tempList)

obj=LambdaUsageRepo()
print("--------------------------task 1---------------------------------------")
obj.quadraticExpession("2 3 2 4")
print("--------------------------task 2---------------------------------------")
l=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
obj.countOccurance(l)
print("--------------------------END---------------------------------------")
