import time
import datetime


class TimesUnit:

    def get_now(Accuracy=13):
        # Accuracy为精确度
        if Accuracy == 13:
            return int(time.time() * 1000)
        return int(time.time())

    def get_first_day_of_month(year, month):
        return int(time.mktime(datetime.date(year, month, 1).timetuple()))


if __name__ == '__main__':
    a = TimesUnit.get_now()
    print(a)
    print(TimesUnit.get_first_day_of_month(2020, 9))
