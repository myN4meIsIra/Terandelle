# time
"""
functionality for pulling time and date
"""

import datetime

class TimeClass:
    def __init__(self):
        pass

    def getDateTime(self):
        now = datetime.datetime.now()
        dateTimeData = {"second": now.second,
                        "minute": now.minute,
                        "hour": now.hour,
                        "day": now.day,
                        "month": now.month,
                        "year": now.year,
                        }
        return dateTimeData


    def getDateTimeFormatted(self):
        dateTimeData = datetime.datetime.now()
        formattedTImeData = datetime.datetime.strftime(dateTimeData, "%I:%M %p, %A, %B %d, %Y")

        return formattedTImeData