DOMAIN = 'box1'
from Tree import DecisionTree
import DataBase as DB
from Traffic import *
from datetime import date
from datetime import datetime
import pandas as pd
import random
import time
import string
import re
import os.path


def setup(hass, config):
    """Setup our skeleton component."""
    #States are in the format DOMAIN.OBJECT_ID.
    hass.states.set('box1.box1', 'Works!')
    model = Tree.DecisionTree()
    name = DB.getmodelname() #STAVROS CHECK HERE

    today = date.today()
    today = today.strftime("%d%m%Y")

    if (name == null || today - DB.getTrainDay() >= 7):
         model.train_all(DB.getData())
    else:
        model.load(name) #STAVROS CHECK HERE

    def isHoliday(): #currently only recognizes december 25th as a holiday.
        day = date.today()
        day = day.strftime("%d%m")
        if (day == "2512"):
            return 1
        else:
            return 0


def calculate_atime(seconds_offset):
    time_now = datetime.datetime.now()

    adatetime = time_now + datetime.timedelta(0, seconds_offset)

    atime = adatetime.time()

    return atime


def mlstring_to_astring(action, time):
    id_alias = ''.join(random.choice(string.digits) for i in range(13))
    action = action
    atime = calculate_atime(int(time))

    astring = "\n" + "- id: 'PHA" + "'\n" \
                     '  alias: ' + id_alias + '\n' \
                     '  trigger:\n' \
                     '  - platform: time\n' \
                     '    at: "' + str(atime) + '"\n' \
                     '  condition: []\n' \
                     '  action:\n' \
                     '    service: ' + action + '\n\n'

    return astring


def write_to_automations(action, time):
    path = 'config/'
    filename = 'new_automations.yaml'
    path_filename = os.path.join(path, filename)
    f = open(filename, "a+")

    f.write(mlstring_to_astring(action, time))
    f.close()
    read_from_new_automations(action, time)


def read_from_new_automations(date, time):
    path = 'config/'
    filename = 'automations.yaml'
    path_filename = os.path.join(path, filename)

    f = open(path_filename, "r+")
    contents = f.readlines()
    y = 0

    time_now = datetime.datetime.now()
    time_now = time_now.time()

    for x in contents:
        if (re.match('- id: \'PHA', contents[y])):
            for z in range(8):
                if (re.match('    at: \"\d', contents[y + z])):
                    time_of = contents[y + z].split('\"')
                    # print(str(time_of[1]))
                    time_object = datetime.datetime.strptime(time_of[1], '%H:%M:%S.%f').time()
                    if (time_now > time_object):
                        del contents[y]
                        for a in range(12):
                            if (re.match('- id: ', contents[y])):
                                break
                            del contents[y]
                    # Use this to delete all times less than the current time, so automations that have already occurred.
        y = y + 1

    b = 0
    f.close()
    file = open(path_filename, "w")

    for p in contents:
        file.write(contents[b])
        b = b + 1

    file.write(mlstring_to_astring(date, time))
    f.close()


def reload_automations():
    hass.services.call('automation', 'reload')


# Listener to handle fired events
def handle_event(event):
    today = date.today()
    today = today.strftime("%d%m%Y")
    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    user = "user1"
    weekday =  today.weekday()
    holiday = isHoliday()
    location = deviceTracker("stavrosIphone").location_name.home()
    if (location == 0):
        # getTraffic() returns the amount of above average seconds for the commute
        ETA = Traffic.getTraffic("homeAddress", "SchoolAddress")
        current_time = current_time + ETA

    action = event.event_type + event.data 
    time,action = model.predict(user,action,today,current_time,location,holiday,weekday)
    write_to_automations(action, time)
    DB.save(user,action,today,current_time,location,holiday,weekday)

# Listen for when example_component_my_cool_event is fired (example code for checking status of event. Disable for presentation)
#hass.bus.listen('example_component_my_cool_event', handle_event)

return True
