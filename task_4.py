new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

completed_tasks.append(new_tasks.pop(-1))
new_tasks.pop(2)
print(completed_tasks)
print(new_tasks)
print(f'Задаче {new_tasks[-1]} подняли приоритет! Нужно срочно взять в работу.')