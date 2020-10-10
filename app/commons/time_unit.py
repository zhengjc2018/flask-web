import time
import datetime


class TimesUnit:

    def get_now(Accuracy=10):
        # Accuracy为精确度
        if Accuracy == 13:
            return int(time.time() * 1000)
        return int(time.time())

    def get_first_day_of_month(year, month):
        return int(time.mktime(datetime.date(year, month, 1).timetuple()))

    def get_all_wanted_week_timestp(start, to, week=[0, 2]):
        result = []
        while start < to+864:
            _date = TimesUnit.timestp_to_date(start)
            if _date.tm_wday in week:
                result.append(start)
            start += 86400
        return result

    def timestp_to_date(timestp):
        if len(str(timestp)) > 10:
            timestp = int(timestp[:10])
        return time.localtime(timestp)


if __name__ == '__main__':
    a = TimesUnit.get_now()
    print(a)
    print(TimesUnit.get_first_day_of_month(2020, 9))
    now = TimesUnit.get_first_day_of_month(2020, 9)
    print(TimesUnit.get_all_wanted_week_timestp(now, time.time()))
