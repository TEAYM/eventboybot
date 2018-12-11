from datetime import datetime as dt
from intervaltree import Interval, IntervalTree

# SUCCESS CASES
###############

# input: no overlap
# expected: no common interval
interval_list = [
    Interval(dt(year=2018, month=1, day=1, hour=0), dt(year=2018, month=1, day=2, hour=0), "user_1"),
    Interval(dt(year=2018, month=1, day=2, hour=0), dt(year=2018, month=1, day=3, hour=0), "user_2"),
    Interval(dt(year=2018, month=1, day=3, hour=0), dt(year=2018, month=1, day=4, hour=0), "user_3")
]

find_all_common_intervals(interval_list)


# input: one overlap
# expected: one common interval at 2018,1,2,0 - 2018,1,3,0, for all users
interval_list = [
    Interval(dt(year=2018, month=1, day=1, hour=0), dt(year=2018, month=1, day=4, hour=0), "user_1"),
    Interval(dt(year=2018, month=1, day=2, hour=0), dt(year=2018, month=1, day=3, hour=0), "user_2"),
    Interval(dt(year=2018, month=1, day=2, hour=0), dt(year=2018, month=1, day=5, hour=0), "user_3")
]

find_all_common_intervals(interval_list)


# input: complete overlap
# expected: one common interval at 2018,1,1,0 - 2018,1,4,0, for all users
interval_list = [
    Interval(dt(year=2018, month=1, day=1, hour=0), dt(year=2018, month=1, day=4, hour=0), "user_1"),
    Interval(dt(year=2018, month=1, day=1, hour=0), dt(year=2018, month=1, day=4, hour=0), "user_2"),
    Interval(dt(year=2018, month=1, day=1, hour=0), dt(year=2018, month=1, day=4, hour=0), "user_3")
]

find_all_common_intervals(interval_list)

# input: user 1 has 2 different intervals
# expected: two common intervals at [2018,1,1,0 - 2018,1,2,0] and [2018,1,4,0 - 2018,1,5,0] 
interval_list = [
    Interval(dt(year=2018, month=1, day=1, hour=0), dt(year=2018, month=1, day=2, hour=0), "user_1"),
    Interval(dt(year=2018, month=1, day=4, hour=0), dt(year=2018, month=1, day=5, hour=0), "user_1"),
    Interval(dt(year=2018, month=1, day=1, hour=0), dt(year=2018, month=1, day=8, hour=0), "user_2"),
]

find_all_common_intervals(interval_list)


# input: many users with many intervals each
# expected: many common intervals 
interval_list = [
    Interval(dt(year=2018, month=1, day=1, hour=10), dt(year=2018, month=1, day=1, hour=12), "user_1"),
    Interval(dt(year=2018, month=1, day=3, hour=10), dt(year=2018, month=1, day=3, hour=12), "user_1"),
    Interval(dt(year=2018, month=1, day=1, hour=11), dt(year=2018, month=1, day=1, hour=13), "user_2"),
    Interval(dt(year=2018, month=1, day=3, hour=11), dt(year=2018, month=1, day=3, hour=13), "user_2"),
    Interval(dt(year=2018, month=1, day=1, hour=8), dt(year=2018, month=1, day=1, hour=18), "user_3"),
    Interval(dt(year=2018, month=1, day=2, hour=8), dt(year=2018, month=1, day=2, hour=18), "user_3"),
    Interval(dt(year=2019, month=1, day=1, hour=8), dt(year=2019, month=1, day=1, hour=18), "user_4"),
    Interval(dt(year=2019, month=1, day=5, hour=0), dt(year=2019, month=1, day=6, hour=0), "user_4"),
    Interval(dt(year=2019, month=1, day=5, hour=0), dt(year=2019, month=1, day=6, hour=0), "user_5"),
    Interval(dt(year=2019, month=1, day=5, hour=0), dt(year=2019, month=1, day=6, hour=0), "user_5"),
    Interval(dt(year=2019, month=1, day=5, hour=0), dt(year=2019, month=1, day=6, hour=0), "user_6")
]

find_all_common_intervals(interval_list)

# FAILURE CASES:
################

# input: one input interval does not have valid data
# expected: error
interval_list = [
    Interval(dt(year=2018, month=1, day=1, hour=0), dt(year=2018, month=1, day=2, hour=0)),
    Interval(dt(year=2018, month=1, day=4, hour=0), dt(year=2018, month=1, day=5, hour=0), "user_1"),
    Interval(dt(year=2018, month=1, day=1, hour=0), dt(year=2018, month=1, day=8, hour=0), "user_2"),
]

find_all_common_intervals(interval_list)


# input: invalid date (month = 0)
# expected: error
interval_list = [
    Interval(dt(year=2018, month=0, day=1, hour=0), dt(year=2018, month=1, day=2, hour=0), "user_1"),
    Interval(dt(year=2018, month=1, day=4, hour=0), dt(year=2018, month=1, day=5, hour=0), "user_1"),
    Interval(dt(year=2018, month=1, day=1, hour=0), dt(year=2018, month=1, day=8, hour=0), "user_2"),
]

find_all_common_intervals(interval_list)


# input: invalid date (non-leap year feb 29)
# expected: error
interval_list = [
    Interval(dt(year=2017, month=2, day=29, hour=0), dt(year=2017, month=3, day=2, hour=0), "user_1"),
    Interval(dt(year=2017, month=1, day=4, hour=0), dt(year=2017, month=1, day=5, hour=0), "user_1"),
    Interval(dt(year=2017, month=1, day=1, hour=0), dt(year=2017, month=1, day=8, hour=0), "user_2"),
]

find_all_common_intervals(interval_list)


# input: interval presented with larger element first and smaller element second (non-leap year feb 29)
# expected: not sure
interval_list = [
    Interval(dt(year=2017, month=3, day=2, hour=0), dt(year=2017, month=2, day=29, hour=0), "user_1"),
    Interval(dt(year=2017, month=1, day=4, hour=0), dt(year=2017, month=1, day=5, hour=0), "user_1"),
    Interval(dt(year=2017, month=1, day=1, hour=0), dt(year=2017, month=1, day=8, hour=0), "user_2"),
]

find_all_common_intervals(interval_list)


