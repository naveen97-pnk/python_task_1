from functools import reduce


class FilterModules:
    def mapInsideFilterUsage(self,l):
        if isinstance(l,list):
            def negative(num):
                return num >= 0
            a = list(filter(negative, list(map(lambda x: -x, l))))
            print(a)
        else:
            print("INVALID INPUT")
    def zipANdDictUsage(self,l1,l2):
        if len(l1) == len(l2) and isinstance(l1, list) and isinstance(l2, list):
            resDict=dict(zip(l1,l2))
            print(resDict)
        else:
            print("INVALID INPUT")
    def manipulationList(self,l):
        def multiple(a,b):
            return a*b
        print(reduce(multiple,l))
obj=FilterModules()
print("--------------------------task 1---------------------------------------")
l=[10,-1,2,3,-4,5,-6]
obj.mapInsideFilterUsage(l)
print("--------------------------task 2---------------------------------------")
ls=[1,2,3,4,5]
obj.manipulationList(ls)
print("--------------------------task 3---------------------------------------")
lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]
obj.zipANdDictUsage(lst1,lst2)
print("--------------------------END---------------------------------------")