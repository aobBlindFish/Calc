import datetime
import time

date = str(datetime.date.today())
# date: "YYYY-MM-DD"


def date_check(custom_date):
    date_overlap = True
    for i in range(5, 10, 1):
        if custom_date[i] != date[i]:
            date_overlap = False
            return date_overlap
    return date_overlap


# custom delay
def custom_delay(sec):
    time.sleep(sec)


# delay presets
short_delay = 0.4
med_delay = 0.8
long_delay = 1.4
