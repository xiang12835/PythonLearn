# coding=utf-8

import datetime
def dayofyear():
    year = input("请输入年份:")
    month = input("请输入月份:")
    day = input("请输入天:")
    date1 = datetime.date(year=int(year),month=int(month),day=int(day))
    date2 = datetime.date(year=int(year),month=1,day=1)

    return (date1 - date2 + datetime.timedelta(1)).days


if __name__ == "__main__":
    print dayofyear()
