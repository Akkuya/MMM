from collections import Counter


def calc():

    def calcType():
        print("Please enter what operation you would like to do. (mean/median/mode)")
        varCalcType = input()
        if varCalcType == ("1") or varCalcType == ("mean"):
            mean()
        elif varCalcType == ("3") or varCalcType == ("mode"):
            mode()
        elif varCalcType == ("2") or varCalcType == ("median"):
            median()
        else:
            print("Invalid input, please try again.")
            calcType()

    def mean():
        print("Please enter how many numbers you want to calculate the mean of.")
        numbers1 = input()
        try:
            mean.intInput = int(numbers1)
        except ValueError:
            print("Invalid input, please try again.")
            mean()
        sum1 = 0
        for i in range(int(numbers1)):
            print("Please enter number " + str(i + 1))
            meanCalc()
            sum1 = sum1+meanCalc.floatNum1
            average = sum1/int(numbers1)
        print("The mean of these numbers is " + str(average) + ".")

    def meanCalc():
        num1 = input()
        try:
            meanCalc.floatNum1 = float(num1)
        except ValueError:
            print("Invalid input, please try again.")
            meanCalc()

    def median():
        median.numList = []
        print("Please enter how many numbers you wish to find the median of.")
        medianNum = input()
        try:
            median.intMedianNum = int(medianNum)
        except ValueError:
            print("Invalid input, please try again.")
            median()
        medianCalc()
        median.numList.sort()
        medianIndex = int(medianNum)/2
        EOO = int(medianNum) % 2
        if EOO == (0):
            median.IMI = int(medianIndex) - 1
            median.IMI2 = median.IMI + 1
            MV1 = median.numList[median.IMI2]
            MV2 = median.numList[median.IMI]
            medianVar = ((MV1 + MV2)/2)
        else:
            MI1 = round(medianIndex)
            medianVar = median.numList[MI1]
        print(medianVar)
        calc()

    def medianCalc():
        for i in range(median.intMedianNum):
            print("Please enter number " + str(i + 1) + ".")

            def MC2():
                appendNum = input()
                try:
                    medianCalc.floatAppendNum = float(appendNum)
                except ValueError:
                    print("Invalid input, please try again.")
                    MC2()
            MC2()
            median.numList.append(medianCalc.floatAppendNum)

    def mode():
        mode.modeList = []
        print("Please enter how many numbers you wish to find the mode of.")
        modeNum = input()
        try:
            mode.intmodeNum = int(modeNum)
        except ValueError:
            print("Invalid input, please try again.")
            mode()
        modeCalc()
        data = Counter(mode.modeList)
        print("The mode of this set is the first value, which occurs the amount of times as the second value.")
        print(data.most_common(1))
        calc()

    def modeCalc():
        for i in range(mode.intmodeNum):
            print("Please enter number " + str(i + 1) + ".")
            appendmodeNum = input()
            try:
                modeCalc.floatAppendModeNum = float(appendmodeNum)
            except ValueError:
                print("Invalid input, please try again.")
                modeCalc()
            mode.modeList.append(modeCalc.floatAppendModeNum)

    calcType()


calc()
