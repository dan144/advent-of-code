#!/usr/bin/python3

from collections import OrderedDict
from datetime import datetime, timedelta

import operator
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

# 0 = minute spent awake, 1 = minute spent asleep
guards = OrderedDict()
lines = sorted(inputs)
for line in lines:
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

sleepiest_guard = None
most_sleep_mins = 0
most_sleep_schedule = []
for guard, sleeping in guards.items():
    sleep = 0
    guard_sleep_mins = [0] * 60
    for date, sleep_schedule in sleeping.items():
        sleep += sum(sleep_schedule)
        for i in range(60):
            guard_sleep_mins[i] += sleep_schedule[i]
        #print(guard, date, ''.join(map(str, sleep_schedule)))
    if sleep > most_sleep_mins:
        # this guard slept more than the sleepiest guard
        most_sleep_schedule = guard_sleep_mins
        most_sleep_mins = sleep
        sleepiest_guard = guard
print('Guard ID:', sleepiest_guard)
print('Most sleep:', max(most_sleep_schedule))
most_minutes = most_sleep_schedule.index(max(most_sleep_schedule))
print('Sleepiest minute:', most_minutes)
print('Guard*Minute:', int(sleepiest_guard) * most_minutes)

print()
print('PART TWO')

for guard, sleeping in guards.items():
    total_per_min = [0] * 60
    for date, sleep_schedule in sleeping.items():
        for i in range(60):
            total_per_min[i] += sleep_schedule[i]
    guards[guard] = total_per_min

sleepiest_guard = None
most_sleep_per_min = 0
most_minutes = None
for guard, sleep_schedule in guards.items():
    for i in range(60):
        if sleep_schedule[i] > most_sleep_per_min:
            most_sleep_per_min = sleep_schedule[i]
            most_minutes = i
            sleepiest_guard = guard

print('Guard ID:', sleepiest_guard)
print('Sleepiest minute:', most_minutes)
print('Guard*Minute:', int(sleepiest_guard) * most_minutes)
