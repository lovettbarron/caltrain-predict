import re
import pandas as pd

def parse_train(x):
    # x should be the train code eg 123
    # {"id": "123", "type:" "bullet", direction: "south"}
    x = str(x)
    if x == '': return ''
    elif len(x) != 3: return ''
    t = {}
    t["id"] = x if len(x) is 3 else -1
    t["direction"] = "north" if x[2] in [1,3,5,7,9] else "south"
    if x[0] == '1':
        t["type"] = "local"
    elif x[0] == '2':
        t["type"] = "limited"
    elif x[0] == '3':
        t["type"] = "bullet"
        
    t = pd.DataFrame(t)
    return t
    
def get_time_of_day(x):
    # x should be datetime object
    # offline: -1
    # peak-morning: 1
    # workday: 2
    # peak-evening: 3
    #average 0
    
        if x.hour <= 6 and x.hour >= 23:
            return -1
        elif x.hour > 10 and x.hour < 16:
            return 2
        elif x.hour >= 16 and x.hour <= 19:
            return 3
        elif x.hour > 6 and x.hour <=10:
            return 1
        else:
            return 0
        
def check_hashtag(x):
    # x should be the cleaned hashtag row
    if x == '': return ''
    t = re.search('[N,S]B([0-9]{0,3})',x)
    if t:
        return t.group(1)
    else:
        return ''