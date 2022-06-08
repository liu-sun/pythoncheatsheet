stem = "甲乙丙丁戊己庚辛壬癸"
branch = "子丑寅卯辰巳午未申酉戌亥"
__zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"


def stembranch(year):
    """干支纪年"""
    return stem[(year-4) % 10]+branch[(year-4) % 12]


def zodiac(year):
    return __zodiac[(year-4) % 12]


class StemBranch:
    stem = "甲乙丙丁戊己庚辛壬癸"
    branch = "子丑寅卯辰巳午未申酉戌亥"
    __zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"

    def __init__(self):
        self.stem = "甲乙丙丁戊己庚辛壬癸"
        self.branch = "子丑寅卯辰巳午未申酉戌亥"
        self.__zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"

    def stembranch(self, year):
        """干支纪年"""
        return self.stem[(year-4) % 10]+self.branch[(year-4) % 12]

    @classmethod
    def zodiac(cls, year):
        return cls.__zodiac[(year-4) % 12]

    @staticmethod
    def leap(year):
        """平年闰年"""
        return "闰年" if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else "平年"


class Zodiac(StemBranch):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    print(StemBranch._StemBranch__zodiac)
    print(StemBranch()._StemBranch__zodiac)
    print(StemBranch.zodiac(2022))
    print(Zodiac.leap(2022))
    print(stembranch(2022))
