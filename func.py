def parse_train(x):
    # x should be the train code eg 123
    # {"id": "123", "type:" "bullet", direction: "south"}
    t = {}
    t["id"] = x if len(x) is 3 else -1
    if x[0] == 1:
        t["type"] = "local"
    elif x[0] == 2:
        t["type"] = "limited"
    elif x[0] == 3:
        t["type"] = "bullet"
    
    t["direction"] = "north" if x[2] in [1,3,5,7,9] else "south"
    return t
    
    
    

def get_time_of_day(x):
    # x should be datetime object
        if x.hour <= 6 and x.hour >= 23:
            return "Offline"
        elif x.hour > 10 and x.hour < 16:
            return "Workday"
        elif x.hour >= 16 and x.hour < 7:
            return "Peak,Evening"
        elif x.hour > 6 and x.hour <=10:
            return "Peak,Morning"