import re
import pandas as pd

ret = []

def parse_train(t):
# Revised this function to work with categorical variables
# x should be a list with train codes eg 123
# {"id": "123", "type:" "bullet", direction: "south"}

    try:
        s = t['topic_train'].split(',')
    except:
        return t['topic_train']
    if s[0] == '':
        return np.nan
    for x in s:
        q = {}
        x = str(x)
        x = re.sub('[^0-9]','', x)
        if len(x)<3: continue

        # 1 = north, 0 = south
        q["t_northbound"] = 1 if int(x[2]) in [1,3,5,7,9] else 0
        q['t_limited'] = 0
        q['t_bullet'] = 0
        
        if x[0] == '1':
            q['t_limited'] = 0
        elif x[0] == '2':
            q["t_limited"] = 1 # limited
        elif x[0] == '3':
            q["t_bullet"] = 1 # bullet
        else:
            q['t_limited'] = 0

        ret.append({'tweet_id': t['id'],
                    'timestamp': t['created_at'], 
                    'train_id': int(x),
                    't_northbound':q["t_northbound"], 
                    't_limited': q["t_limited"],
                    't_bullet': q['t_bullet']})
    return s


def get_time_of_day(x):
    # x should be datetime object
    # offline: -1
    # peak-morning: 1
    # workday: 2
    # peak-evening: 3
    #average 0
    if x.hour >= 16 and x.hour <= 19:
        return 1 # Evening rush
    elif x.hour > 6 and x.hour <=10:
        return 1 # Morning Rush
    else:
        return 0

def check_train_id(x):
    # x should be the cleaned hashtag row
    if x == '': return ''
    t = re.findall('#?[N,S][B,b]\s?([0-9]{0,3})',x) # Seems more robust
    # t = re.findall('[N,S]B([0-9]{0,3})',x)
    if t:
        return t
    else:
        return ''
    
def check_late(x):
        # x should be the cleaned hashtag row
    if x == '': return ''
    t = re.findall('[N,S]B([0-9]{0,3})',x)
    if t:
        return t # { is_delayed, magnitude 1-5 }
    else:
        return ''
    
def rank_late(x):
    # consumes pd.series
    # Consumes a series. Takes parsed LATE and TRAIN lists, and spits out a magnitude of delay value
    # 0 = No delay, 4 = BIG delay
    
    x = pd.Series(x) # Cast just in case
    trains = x.train_topic
    