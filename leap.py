def leap(year):
    return "闰年" if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else "平年"


def leap(year):
    if year % 400 == 0:
        return "闰年"
    elif year % 4 == 0 and year % 100 != 0:
        return "闰年"
    else:
        return "平年"


def leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return "闰年"
    else:
        return "平年"


if __name__ == "__main__":
    print(leap(2022))
