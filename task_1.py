str_time = '1h 45m,360s,25m,30m 120s,2h 60s'
list_time = str_time.replace(',', ' ').split()

sum_time = 0

for i in list_time:
    if i.find('m') != -1:
        sum_time += int(i.replace('m',''))
    elif i.find('h') != -1:
        sum_time += int((i.replace('h',''))) * 60
    elif i.find('s') != -1:
        sum_time += int((i.replace('s',''))) / 60
    else:
        print('Еденица времени не найдена!')
        
print(sum_time)