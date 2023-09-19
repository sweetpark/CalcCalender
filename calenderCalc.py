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
        "Usage: python3 calenderCalc.py [year/month/day] [day_count]\n",
        "EX:\n",
        "python3 calenderCalc.py 2023/09/12 10\n")


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
    try:
        #input
        if len(sys.argv) != 3:
            sys.exit()
        input=list(sys.argv[1].split('/'))
        #초기 변수
        date=datetime.date(int(input[0]),int(input[1]),int(input[2]))
        holiday_list = pytimekr.holidays()
        timeCalc=date
        weekDay=timeCalc.weekday()
        count =int(sys.argv[2])

        excludeWeekend(holiday_list,timeCalc,weekDay,count)

    except:
        printUsage()
        sys.exit()



main()

