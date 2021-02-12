import datetime

date = str(datetime.date.today())
# date: "YYYY-MM-DD"


def date_check(custom_date):
    date_overlap = True
    for i in range(5, 10, 1):
        if custom_date[i] != date[i]:
            date_overlap = False
            return date_overlap
    return date_overlap
