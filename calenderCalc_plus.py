import datetime
import sys
from pytimekr import pytimekr

#from datetime import datetime

##
# now = datetime.now()
# print(now) #2023-09-19 19:23:17.746442

##
# time=datetime.date(now)
# print(time) #2023-09-19

# ##
# stamp=datetime.timestamp(now)
# print(type(stamp))
# print("====>" + str(stamp)) #====>1695118997.746442

# ##
# ctime=datetime.ctime(now)
# print(ctime) #Tue Sep 19 19:23:17 2023

##
# timeCalc=date+datetime.timedelta(days=20)
# print(type(timeCalc))
# print(timeCalc)#2023-10-09

##
# whatDay=date.weekday()
# print(whatDay) #1 (Tuesday)

##
# date=datetime.date(2023,9,19)
# print(type(date))
# print(date) #2023-09-19


#example
def printUsage():
    print(
        "\n",
        "================================\n",
        "[Usage]\n",
        "Date (날짜) : [year/month/day]\n",
        "Period (소요기간) : [count]\n",
        "================================\n",
        "\n")


def excludeHoliday(holiday_list,time,weekDay,count):
    
    #공휴일 제외
    for i in holiday_list:
        if time == i:
            #주말 = 공휴일 중복 제외
            if weekDay > 4:
                break
            
            count=count+1
            break  
    return count



def excludeWeekend(holiday_list,timeCalc,weekDay,count):
    
    while True:
        #주말 제외
        if weekDay < 5:
            count = count - 1
            if count == 0:
                print(timeCalc)
                break
            timeCalc=timeCalc+datetime.timedelta(days=1)       
            weekDay=timeCalc.weekday()
        else:
            timeCalc=timeCalc+datetime.timedelta(days=1)
            weekDay=timeCalc.weekday()

        count=excludeHoliday(holiday_list,timeCalc,weekDay,count)


def main():
    while True:
        try:
            #input
            print(" ** if you want program exit : write \"shutdown\" ** ")
            date_tmp=input("Date (ex 2023/09/19): ")
            if (date_tmp=="shutdown"):
                break
            split_date=list(date_tmp.split('/'))
            if len(split_date) != 3:
                printUsage()
                continue
            #초기 변수
            date=datetime.date(int(split_date[0]),int(split_date[1]),int(split_date[2]))
            holiday_list = pytimekr.holidays()
            timeCalc=date
            weekDay=timeCalc.weekday()
            count =int(input("period (ex 10): "))

            excludeWeekend(holiday_list,timeCalc,weekDay,count)
        except:
            printUsage()




main()

