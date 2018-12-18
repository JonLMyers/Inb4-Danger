import datetime

def daily_message_count(timestamps):
    eval_date = {"Year": 0, "Month": 0, "Day": 0, "Count": 0}
    count_structure = []
    is_first = True
    for timestamp in timestamps:
        count = int(eval_date["Count"])
        year = timestamp[:4]
        month = timestamp[5:7]
        day = timestamp[8:10]

        if is_first:
            eval_date["Year"] = year
            eval_date["Month"] = month
            eval_date["Day"] = day
            eval_date["Count"] = (count + 1)
            is_first = False

        elif day == eval_date["Day"] and month == eval_date["Month"]:
            eval_date["Count"] = (count + 1)

        else:
            count_structure.append({"Year": eval_date["Year"], "Month": eval_date["Month"], "Day": eval_date["Day"], "Count": eval_date["Count"]})
            eval_date["Year"] = year
            eval_date["Month"] = month
            eval_date["Day"] = day
            eval_date["Count"] = 1
    
    return count_structure   
