def add_time(start, duration, week=''):
    #Starting variables 
    hours = 0
    minutes = 0
    #detecting if PM is present in start time
    PM = 'PM'
    twelve = '12' 

    #Converting to 24h clock 
    if PM in start and twelve not in start[:3]:
        hours += 12
    
    #Converting string into numbers
    start_string = ''
    duration_string = ''
    for num in start:
        if num.isdigit():
            start_string += num
    for num2 in duration: 
        if num2.isdigit():
            duration_string += num2

    #Original am / pm modifier
    original_mod = ''
    for char in start:
        if char.isalpha():
            original_mod += char
            #print(original_mod)
    #Opp mod
    opp_mod = ''
    if original_mod == 'PM':
        opp_mod = 'AM'
    if original_mod == "AM":
        opp_mod = 'PM'

    #Adding the hours together
    hours += int(start_string[:-2]) + int(duration_string[:-2])
    minutes = int(start_string[-2:]) + int(duration_string[-2:])
    if minutes >= 60:
        minutes = minutes % 60
        hours += 1
        minutes_string = '0' + f'{minutes}'
    elif minutes < 10:
        minutes_string = '0' + f'{minutes}'
    else:
        minutes_string = f'{minutes}'


    #Calculating days later
    days_after = hours // 24
    hours = hours % 24

    if week != '':
        #Calculating new week
        week = week.casefold()
        weak_dict = {
            'sunday': 1,
            'monday': 2,
            'tuesday': 3,
            'wednesday': 4,
            'thursday': 5,
            'friday': 6,
            'saturday': 7,
        }
        week_num = weak_dict.get(week) + (days_after % 7)

        #print(days_after % 7)
        #print(week_num)

        if week_num >= 8:
            week_num -= 7

        #print(week_num)

        week_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thurday', 'friday', 'saturday']

        new_week =  ', ' + week_list[week_num -1].capitalize()

        #print(new_week)
    else:
        new_week = ''


    #Adding am / pm
    if hours < 12:
        minutes_string += ' AM'
    elif hours > 12:
        minutes_string += ' PM'
        hours -= 12
    elif hours == 12 and days_after > 1:
        minutes_string +=  f' {original_mod}'
    elif hours == 12 and days_after < 1:
        minutes_string +=  f' {opp_mod}'
    else:
        minutes_string += f' {original_mod}'

    #Making midnight = 12
    if hours == 0:
        hours = 12


    #Print statement
    if days_after == 1:
        print(f'{hours}' + ':' + f'{minutes_string}' + f'{new_week}' + ' (next day)')
    elif 1 < days_after < 2:
        print(f'{hours}' + ':' + f'{minutes_string}' + f'{new_week}' + ' (next day)')
    elif days_after >= 2:
        print(f'{hours}' + ':' + f'{minutes_string}' +  f'{new_week}' + f' ({days_after} days later)') 
    else:
        print(f'{hours}' + ':' + f'{minutes_string}' + f'{new_week}')


    #Return statement
    if days_after == 1:
        return(f'{hours}' + ':' + f'{minutes_string}' + f'{new_week}' + ' (next day)')
    elif 1 < days_after < 2:
        return(f'{hours}' + ':' + f'{minutes_string}' + f'{new_week}' + ' (next day)')
    elif days_after >= 2:
        return(f'{hours}' + ':' + f'{minutes_string}' +  f'{new_week}' + f' ({days_after} days later)') 
    else:
        return(f'{hours}' + ':' + f'{minutes_string}' + f'{new_week}')

add_time('3:30 PM', '2:12')
