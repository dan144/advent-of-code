#!/usr/bin/python3

from collections import OrderedDict
from datetime import datetime, timedelta
import sys

print('Running:',sys.argv[0])

n = sys.argv[0][2:].index('.')
filen = sys.argv[0][5:n+1+len(str(n))]
input_file = 'input' + str(filen)
print('Reading:', input_file)

inputs = []
data_type = str
with open(input_file, 'r') as f:
    for line in f:
        inputs.append(data_type(line[:-1]))

print()
print('PART ONE')

# Lines
# [1518-05-08 00:02] Guard #659 begins shift
# [1518-06-09 00:52] falls asleep
# [1518-07-27 00:59] wakes up
guards = OrderedDict()
guard = None
min_time = None
lines = []
for line in inputs:
    date, time, rest = line.split(' ', 2)
    date = date[1:]
    time = time[:-1]
    #print(date, time, rest)
    import calendar
    timetuple = date.split('-') + time.split(':') + [0,0,0,0]
    timetuple[0] = 1970
    #print(timetuple)
    timestamp = calendar.timegm([int(i) for i in timetuple])
    if min_time is None or timestamp < min_time:
        min_time = timestamp
    #print(timestamp)
    lines.append((timestamp, line))
lines = sorted(lines, key=lambda x: x[0])

# 0 = minute spent awake, 1 = minute spent asleep
for _, line in lines:
    #print(line)
    date, time, rest = line.split(' ', 2)
    date = date[1:]
    time = time[:-1].split(':')
    time[0] = int(time[0])
    time[1] = int(time[1])
    if time[0] == 0:
        day = date
    else:
        t = datetime.strptime(date, '%Y-%m-%d')
        t += timedelta(days=1)
        n_mon = str(t.month)
        n_mon = '0' + n_mon if len(n_mon) == 1 else n_mon
        n_day = str(t.day)
        n_day = '0' + n_day if len(n_day) == 1 else n_day
        day = '-'.join(date.split('-')[:-2] + [n_mon, n_day])
        #print(day)

    if rest.startswith('Guard'):
        guard = rest.split()[1][1:]
        if guard not in guards:
            guards[guard] = OrderedDict()
        guards[guard][day] = [0] * 60
        if time[0] == 0 and time[1] != 0:
            for i in range(0, time[1]):
                guards[guard][day][i] = 1
    elif rest == 'falls asleep':
        for i in range(time[1], 60):
            guards[guard][day][i] = 1
    elif rest == 'wakes up':
        for i in range(time[1], 60):
            guards[guard][day][i] = 0

most_sleep = None
most_sleep_mins = 0
most_mins = []
import operator
for guard, sleeping in guards.items():
    sleep = 0
    guard_sleep_mins = [0] * 60
    for date, sched in sleeping.items():
        sleep += sum(sched)
        for i in range(60):
            guard_sleep_mins[i] += sched[i]
        #map(operator.add, guard_sleep_mins, sched)
        #print(guard, date, ''.join(map(str, sched)))
    if sleep > most_sleep_mins:
        most_mins = guard_sleep_mins
        most_sleep_mins = sleep
        most_sleep = guard
print(most_sleep)
print(most_mins)
print(max(most_mins))
most_min = most_mins.index(max(most_mins))
print(most_min)
print(int(most_sleep) * most_min)

print()
print('PART TWO')

for guard, sleeping in guards.items():
    total_per_min = [0] * 60
    for date, sched in sleeping.items():
        for i in range(60):
            total_per_min[i] += sched[i]
    guards[guard] = total_per_min

most_guard = None
most_sleep_per_min = 0
most_min = None
for guard, sched in guards.items():
    for i in range(60):
        if sched[i] > most_sleep_per_min:
            most_sleep_per_min = sched[i]
            most_min = i
            most_guard = guard

print(most_guard)
print(most_min)
print(int(most_guard) * most_min)
