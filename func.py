import re
import pandas as pd

def parse_train_t(t):
    # x should be a list with train codes eg 123
    # {"id": "123", "type:" "bullet", direction: "south"}
    # Iterate through list
    t = pd.DataFrame(t)
    s = t['topic_train']
    if s < 1: return None
    ret = []
    for x in s:
        t = {}
        # Check train id
        x = str(x)
        # if x == '': return ''
        # elif len(x) != 3: return ''
        t["id"] = x if len(x) is 3 else -1

        # 1 = north, 2 = south
        t["direction"] = 1 if x[2] in [1,3,5,7,9] else 0

        if x[0] == '1':
            t["type"] = 0 # local
        elif x[0] == '2':
            t["type"] = 1 # limited
        elif x[0] == '3':
            t["type"] = 2 # bullet
        else:
            t["type"] = -1
        ret.append({'tweet_id': t['id'],'timestamp': t['created_at'], 'train_id':t["id"], 'train_direction':t["direction"], 'train_type': t["type"] })
    return ret
    
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
    t = re.findall('[N,S]B([0-9]{0,3})',x)
    if t:
        return t
    else:
        return ''
    
def check_late(x):
        # x should be the cleaned hashtag row
    if x == '': return ''
    t = re.findall('[N,S]B([0-9]{0,3})',x)
    if t:
        return t
    else:
        return ''
    
def rank_late(x):
    # consumes pd.series
    # Consumes a series. Takes parsed LATE and TRAIN lists, and spits out a magnitude of delay value
    # 0 = No delay, 4 = BIG delay
    
    x = pd.Series(x) # Cast just in case
    trains = x.train_topic
    