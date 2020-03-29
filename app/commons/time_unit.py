from time import time


class TimesUnit:

    def get_now(Accuracy=13):
        # Accuracy为精确度
        if Accuracy == 13:
            return int(time() * 1000)
        return int(time())


if __name__ == '__main__':
    a = TimesUnit.get_now()
    print(a)
