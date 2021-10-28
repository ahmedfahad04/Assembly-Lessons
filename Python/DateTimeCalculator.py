# test case checking:
"""
Case 1: month same, date same, year same. (27/11/2021, 27/11/2021)
Case 2: month same, date same, year different. (27/11/2021, 27/11/2022)
Case 3: month different, date different, year same. (15/7/2021, 29/11/2021)
Case 4: month same, date different, year same. (27/11/2021, 29/11/2021)
Case 5: month different, date same, year same. (27/11/2021, 27/12/2021)
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

    return totalDayCount


# main
startDate = input("Enter starting date (DD/MM/YYYY): ").split("/")
endDate = input("Enter ending date (DD/MM/YYYY): ").split("/")

count = totalDays(startDate, endDate)
print("\nTotal Days: ", count, "days (Excluding End day)\n")
