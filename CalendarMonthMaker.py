import calendar

dayOfWeek = ["Monday", "Tuesday", "Wednesday", "Thurdsay", "Friday", "Saturday", "Sunday"]
monthName = ["January", "Feburary", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]

class CalendarBuilder(object):
    def __init__(self, month, year):
        self.month = month
        self.year = year

    def buildCalendar(self):
        print("\n\n======================")
        print("For %s %d" %(monthName[self.month-1], self.year))
        print("======================")
        startDayOfWeek = calendar.monthrange(self.year,self.month)[0]
        for i in range(calendar.monthrange(self.year,self.month)[1]):
            if (startDayOfWeek >= 7):
                startDayOfWeek = 0
            print("%s - %s %d" %(dayOfWeek[startDayOfWeek], monthName[self.month-1], i+1))
            startDayOfWeek += 1
            
def main():
    while True:
        month = input("Enter a month (1 to 12): ")
        if(month.isnumeric()):
            if(int(month) < 1 or int(month) > 12):
                print("That was not a valid entry.  Try again.")
                continue
            else:
                while True:
                    year = input("Enter a year: ")
                    if(year.isnumeric()):
                        reqC = CalendarBuilder(int(month),int(year))
                        reqC.buildCalendar()
                        break
                    else:
                        print("Invalid year.  Try again.")
                break
        else:
            print("Invalid month. Try again.")

if __name__ == '__main__':
    main()
