def leapYear(year):
    if year % 100 != 0 and year % 4 == 0:
        return DateInfo(True)
    elif year % 100 == 0 and year % 400 == 0:
        return DateInfo(True)
    else:
        return DateInfo(False)
def dateAddZero(date):
    if date<10:
        strdate = '0'+str(date)
    else:
        strdate = str(date)
    return strdate
def DateInfo(leapFlag):
    allYear = {}
    month = [i for i in range(1,13)]
    for mon in month:
        if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
            allYear[dateAddZero(mon)] = [dateAddZero(i) for i in range(1,32)]

        elif mon == 2 and leapFlag == True:
            allYear[dateAddZero(mon)] = [dateAddZero(i) for i in range(1,30)]

        elif mon == 2 and leapFlag == False:
            allYear[dateAddZero(mon)] = [dateAddZero(i) for i in range(1, 29)]

        elif mon == 4 or mon == 6 or mon == 9 or mon == 11:
            allYear[dateAddZero(mon)] = [dateAddZero(i) for i in range(1, 31)]
    return allYear

def getMonth_Day(year):
    li = []
    for k,v in leapYear(year).items():
        for i in v :
            li.append(k+i)
    return li

checkCode = {'0': 1, '1': 0, '2': 10, '3': 9, '4': 8, '5': 7, '6': 6, '7': 5, '8': 4, '9': 3, 'X': 2}

def caculateIdNumber(idNum):
    res1 = int(idNum[0])*7+ \
          int(idNum[1])*9+ \
          int(idNum[2])*10+ \
          int(idNum[3])*5+ \
          int(idNum[4])*8+ \
          int(idNum[5])*4+ \
          int(idNum[6])*2+ \
          int(idNum[7])*1+ \
          int(idNum[8])*6+ \
          int(idNum[9])*3+ \
          int(idNum[14])*8+ \
          int(idNum[15])*4+\
          int(idNum[16])*2
              # int(idNum[10])*7+ \
              # int(idNum[11])*9+ \
              # int(idNum[12])*10+\
              # int(idNum[13])*5+ \
    year =int(idNum[6:10])
    for i in getMonth_Day(year):
        res2 = int(i[0])*7+ \
              int(i[1])*9+ \
              int(i[2])*10+\
              int(i[3])*5
        if (res1+res2)%11 == checkCode.get(idNum[-1]):
            print(idNum.replace('****',i))

if __name__ == '__main__':
    idNum = '4401171887****007X'
    caculateIdNumber(idNum)
