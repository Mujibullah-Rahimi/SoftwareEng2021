from boolisLeapYear import boolisLeapYear


# A year is a leap year if it is divisible by 4 but not 100
# underneath is a gathering of assertions for such years
def test_year_is_leap_year_when_divisible_by_4_but_not_100():
    assert boolisLeapYear(2024) is True
    assert boolisLeapYear(1996) is True

    assert boolisLeapYear(1700) is False
    assert boolisLeapYear(2100) is False


# A year is not a leap year if it isn't divisible by 4
def test_year_is_not_leap_year_when_not_divisible_by_4():
    assert boolisLeapYear(2023) is True
    assert boolisLeapYear(1937) is False

    assert boolisLeapYear(1932) is True
    assert boolisLeapYear(1988) is True


# A year is a leap year if it is divisible by 400 but not 100
def test_year_is_leap_year_when_divisible_by_400_but_not_100():
    assert boolisLeapYear(2000) is True
    assert boolisLeapYear(1600) is True

    assert boolisLeapYear(1900) is False
    assert boolisLeapYear(2100) is False
