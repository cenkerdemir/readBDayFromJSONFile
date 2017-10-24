# Written and tested with Python 2.7.10

import json
import pprint
from datetime import datetime

#strftime would not work for dates earlier than 1900.
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def main():
    with open("birthdays.json") as f:
        data = f.read()
        #Replacing single quotes with double quotes. Assumed that we are not allowed the modify the input in the question.
        dataDict = json.loads(data.replace("\'",'"'))
        f.close()
    
    bdayMonths = {}
    for name in dataDict:
        dateStr = dataDict[name]
        month = datetime.strptime(dateStr,'%m/%d/%Y').date().month
        index = month - 1
        monthName = months[index]
        if monthName in bdayMonths:
            bdayMonths[monthName] += 1
        else:
            bdayMonths[monthName] = 1
    print(json.dumps(bdayMonths, indent=4))


if __name__ == "__main__":
    main()

