# test case checking:
"""
Case 1: date same, month same, year same. (27/11/2021, 27/11/2021)
Case 2: date same, month same, year different. (27/11/2021, 27/11/2022)
Case 3: date same, month different, year same. (29/11/2021, 29/12/2021)
Case 4: date different, month same, year same. (15/7/2021, 21/7/2021)
Case 5: date same, month different, year different. (27/11/2021, 27/12/2022)
Case 6: date different, month different, year same. (7/10/2021, 27/12/2021)
Case 7: date different, month same, year different. (7/10/2021, 27/10/2023)
Case 8: date different, month different, year different. (7/10/2020, 27/12/2021)
"""



months = {
    'Jan': 31,
    'Feb': 28,
    'Mar': 31,
    'Apr': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'Aug': 31,
    'Sep': 30,
    'Oct': 31,
    'Nov': 30,
    'Dec': 31
}


def dictToList(inputDict):

    val = inputDict.values()
    outputList = list(val)

    return outputList


def leapYear(year):

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def totalDays(start, end):

    monthList = dictToList(months)

    startingDate = int(start[0])
    endingDate = int(end[0])

    startingMonth = int(start[1])
    endingMonth = int(end[1])

    startingYear = int(start[2])
    endingYear = int(end[2])

    totalDayCount = 0
    currentYear = startingYear
    monthSerial = startingMonth
    monthCount = 0

    if startingMonth == endingMonth and startingYear == endingYear:

        # including both starting and ending dates
        totalDayCount += (endingDate - startingDate)

    else:

        # adding the first and last months' days
        totalDayCount += endingDate + (monthList[startingMonth-1]-startingDate)


        # counting days in between the starting and ending months
        while True:

            monthSerial = monthSerial % 12

            # check for new year
            if monthSerial == 0:
                currentYear += 1

            # check for leap year
            if monthSerial == 1 and leapYear(currentYear) == True:
                totalDayCount += 1

            # print("MONTH: ", monthSerial, "__YEAR__: ", currentYear)

            if monthSerial == endingMonth - 1 and currentYear == endingYear:
                break

            # extracting days from ith month
            days = monthList[monthSerial]
            totalDayCount += days

            # increment
            monthSerial += 1
            monthCount += 1

    return totalDayCount, monthCount



# main
startDate = input("Enter starting date (DD/MM/YYYY): ").split("/")
endDate = input("Enter ending date (DD/MM/YYYY): ").split("/")

daycount, monthcount = totalDays(startDate, endDate)
print("\nTotal Days: ", daycount, "days (Excluding End day)\n")


print(f"""
Additional Info-------
{daycount//365} years {daycount%365} days,
{monthcount//30} months {monthcount%30} days,
{daycount//7} weeks {daycount%7} days, 
""")

