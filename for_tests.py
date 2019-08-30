
# statuses_check_run = ['completed', 'failture', 'completed']
statuses_check_run = ['completed', 'completed', 'completed']


if all(elem == 'completed' for elem in statuses_check_run):
    print(statuses_check_run)
else:
    print('not all is completed')