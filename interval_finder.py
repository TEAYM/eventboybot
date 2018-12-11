from datetime import datetime as dt
from intervaltree import Interval, IntervalTree

# Input: An list of Intervals
# Output: A dictionary (key: overlap, value: set of user_ids which share the overlap)
def find_all_common_intervals(interval_list):
    overlap_dict = dict()
    interval_tree = IntervalTree(interval_list)
    for interval in interval_tree.items(): # create a copy of the tree to iterate over
        other_intervals_that_overlap = find_other_intervals_which_overlap(interval_tree, interval)
        for other_interval in other_intervals_that_overlap:
            add_overlap_to_dict(interval, other_interval, overlap_dict)
    return overlap_dict


# Input: An IntervalTree and an Interval in the IntervalTree
# Output: A set containing all other Intervals in the IntervalTree that intersect with the given
#  Interval
def find_other_intervals_which_overlap(tree, interval):
    tree.remove(interval)
    result = tree.search(interval.begin, interval.end) # returns a set
    return result

# Input: Two intervals and a dictionary (key: tuple)
# Output: None
def add_overlap_to_dict(interval_a, interval_b, dict):
    overlap = find_overlap(interval_a.begin, interval_a.end, interval_b.begin, interval_b.end)
    # if it is already recorded that other existing intervals already overlap over this exact
    # period, add intervals a and b to the set of existing intervals
    if overlap in dict:
        existing_intervals_that_overlap = dict[overlap]
        existing_intervals_that_overlap |= {interval_a.data, interval_b.data}
        dict[overlap] = existing_intervals_that_overlap
    else:
        dict[overlap] = {interval_a.data, interval_b.data}


# Pre-condition: all arguments are integers, a and b are comparable
def find_overlap(a1, a2, b1, b2):
    a_begin = min(a1, a2)
    a_end = max(a1, a2)
    b_begin = min(b1, b2)
    b_end = max(b1, b2)

    if b_end < a_begin or a_end < b_begin:
        return None
    common_begin = max(a_begin, b_begin)
    common_end = min(a_end, b_end)
    return common_begin, common_end


def print_common_intervals(tup_set_dict):
    print("available common datetime intervals:\n")
    # tup is the tuple representing the common interval, userid_set is set of the user data
    for tup, userid_set in tup_set_dict.items():
        print(tup[0].strftime('%Y-%b-%d %H%M') + " - " + tup[1].strftime('%Y-%b-%d %H%M') + ": ")
        print("\tuserids: " + str(userid_set))
    print()

#-----------------------------------------------------------------------------------------------------------------------
# the following section is for the funtionality of finding common times from block out times

blockedtime_intervals = [
    Interval(dt(year=2018, month=6, day=10, hour=0), dt(year=2018, month=7, day=2, hour=10), 20008),
]

def extract_freetime_from_blockedtime(initial_interval, interval_set):
    tree = IntervalTree()
    tree.add(initial_interval)

    for interval in interval_set:
        tree.chop(interval.begin, interval.end)

    return tree

'''
#determine the min and max datetime to look at and provide the user data:
initial_interval = Interval(datetime_tree.begin(), datetime_tree.end(), 20008)
#get a tree representing the "free" intervals:
nonblockedtime_tree = extract_freetime_from_blockedtime(initial_interval, blockedtime_intervals)
#update the main tree with the new information:
datetime_tree.update(nonblockedtime_tree)
'''

# ----------------------------------------------------------------------------------------------------------------------
# plotting given datetime intervals on a Gantt Chart (timeline plot) for easy visualization
# tmp_list = list()
# for interval in datetime_tree:
#     tmp_dict = dict(Task=interval.data, Start=interval.begin.strftime('%Y-%m-%d %H:%M:%S'),
#                     Finish=interval.end.strftime('%Y-%m-%d %H:%M:%S'))
#     tmp_list.append(tmp_dict)
#
# fig = ff.create_gantt(tmp_list, bar_width=0.3, showgrid_x=True, showgrid_y=True)
# offline.plot(fig, filename='gantt-hours-minutes.html')

'''
#example code for plotting gantt charts (timeline plot)
df = [
    dict(Task='Morning Sleep', Start='2016-01-01', Finish='2016-01-01 6:00:00', Resource='Sleep'),
    dict(Task='Breakfast', Start='2016-01-01 7:00:00', Finish='2016-01-01 7:30:00', Resource='Food'),
    dict(Task='Work', Start='2016-01-01 9:00:00', Finish='2016-01-01 11:25:00', Resource='Brain'),
    dict(Task='Break', Start='2016-01-01 11:30:00', Finish='2016-01-01 12:00:00', Resource='Rest'),
    dict(Task='Lunch', Start='2016-01-01 12:00:00', Finish='2016-01-01 13:00:00', Resource='Food'),
    dict(Task='Work', Start='2016-01-01 13:00:00', Finish='2016-01-01 17:00:00', Resource='Brain'),
    dict(Task='Exercise', Start='2016-01-01 17:30:00', Finish='2016-01-01 18:30:00', Resource='Cardio'),
    dict(Task='Post Workout Rest', Start='2016-01-01 18:30:00', Finish='2016-01-01 19:00:00', Resource='Rest'),
    dict(Task='Dinner', Start='2016-01-01 19:00:00', Finish='2016-01-01 20:00:00', Resource='Food'),
    dict(Task='Evening Sleep', Start='2016-01-01 21:00:00', Finish='2016-01-01 23:59:00', Resource='Sleep')
]

colors = dict(Cardio = 'rgb(46, 137, 205)',
              Food = 'rgb(114, 44, 121)',
              Sleep = 'rgb(198, 47, 105)',
              Brain = 'rgb(58, 149, 136)',
              Rest = 'rgb(107, 127, 135)')

fig = ff.create_gantt(df, colors=colors, index_col='Resource', title='Daily Schedule',
                      show_colorbar=True, bar_width=0.8, showgrid_x=True, showgrid_y=True)
offline.plot(fig, filename='gantt-hours-minutes.html')
'''