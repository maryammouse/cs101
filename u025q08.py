###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
        """ Warning: this version incorrectly assumes
        all months have 30 days!"""
        if day < 30:
            day = day + 1
        elif day == 30 and month == 12:
            day = 1
            month = 1
            year = year + 1
        elif day == 30:
            day = 1
            month = month + 1

        return (year, month, day)
