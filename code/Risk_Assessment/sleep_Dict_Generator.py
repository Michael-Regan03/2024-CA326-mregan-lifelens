def sleep_time_mapping(value):
    if 1 <= value <= 4:
        return '1-4'
    elif 4 < value <= 8:
        return '4-8'
    elif 8 < value <= 12:
        return '8-12'
    elif value > 12:
        return '12+'
    else:
        return 'Unknown' 
    
