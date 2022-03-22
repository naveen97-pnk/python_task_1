class LoopsUsage:
    def getPascalTriangle(self,noOfRows):
        for i in range(noOfRows + 1):
            s = 1
            for j in range(1, i + 1):
                print(s, ' ', sep='', end='')
                s = s * (i - j) // j
            if i!=0:
                for m in range(i,noOfRows):
                    print('0',end=" ")
            print()
    def getPyramid_1(self,noOfRows):
        for i in range(1, noOfRows + 1):
            print(" " * (noOfRows - i), end=" ")
            print("*" * (2 * i - 1), end=" ")
            print()
        for i in reversed(range(0, noOfRows)):
            print(" " * (noOfRows - i), end=" ")
            print("*" * (2 * i - 1), end=" ")
            print()
    def getPyramid_2(self,noOfRows):
        for i in range(1, noOfRows + 1):
            for j in range(1, 2 * noOfRows):
                if i == noOfRows or i + j == noOfRows + 1 or j - i == noOfRows - 1:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()

    def getPyramid_3(self,noOfRows):
        for i in range(1,noOfRows + 1):
            for j in range(1,noOfRows+1):
                if i==1:
                    print('*', end=' ')
                elif (j < i) or ((j!=noOfRows) and (j > i)):
                    print(' ', end=' ')
                elif i==j or j==noOfRows:
                    print('*', end=' ')
            print()


obj=LoopsUsage()
print("_________________________PASCAL TRIANGLE_____________________________________")
obj.getPascalTriangle(4)
print("______________________________PATTERN 1___________________________________")
obj.getPyramid_1(5)
print("______________________________PATTERN 2___________________________________")
obj.getPyramid_2(5)
print("_______________________________PATTERN 3__________________________________")
obj.getPyramid_3(5)
print("_________________________________________________________________")

