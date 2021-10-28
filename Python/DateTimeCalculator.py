months = {
	'Jan': 31, 
	'Feb': 28, 
	'Mar': 31, 
	'Apr': 30, 
	'May': 31, 
	'June':30, 
	'July':31, 
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
    
    if year % 400 == 0 or (year%4 == 0 and year%100 != 0 ):
        return True
    else:
        return False

def totalDays(start, end):

    startingDate = int(start[0])
    endingDate = int(end[0])
    
    startingMonth = int(start[1])
    endingMonth = int(end[1])

    startingYear = int(start[1])
    endingYear = int(end[1])










# main
startDate = input("Enter starting date (DD/MM/YYYY): ").split("/")
endDate = input("Enter ending date (DD/MM/YYYY): ").split("/")

print(startDate,endDate)

monthList = dictToList(months)
print(monthList[int(startDate[1])-1])    # be careful about indexing as it starts form 0
