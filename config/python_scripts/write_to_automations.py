import datetime
import random
import string
import os.path
# import appdaemon.plugins.hass.hassapi as hass


def parse_mlstring(mlstring):
    action = mlstring.split("@")[0]
    seconds_offset = mlstring.split("@")[1]

    return action, seconds_offset


def calculate_atime(seconds_offset):
    time_now = datetime.datetime.now()

    adatetime = time_now + datetime.timedelta(0, seconds_offset)
    atime = adatetime.time()

    return atime


def mlstring_to_astring(mlstring):
    id_alias = ''.join(random.choice(string.digits) for i in range(13))
    action_offset_tuple = parse_mlstring(mlstring)
    action = action_offset_tuple[0]
    atime = calculate_atime(int(action_offset_tuple[1]))

    astring = "- id: '" + id_alias + "'\n" \
              '  alias: ' + id_alias + '\n' \
              '  trigger:\n' \
              '  - platform: time\n' \
              '    at: "' + str(atime) + '"\n'\
              '  condition: []\n' \
              '  action:\n' \
              '    service: ' + action + '\n'

    return astring


def write_to_automations(mlstring):
    path = 'config/'
    filename = 'automations.yaml'
    path_filename = os.path.join(path, filename)
    f = open(path_filename, "w+")

    f.write(mlstring_to_astring(mlstring))

    f.close()

# TODO: service call not currently working
# def reload_automations():  
#     hass.services.call('automation', 'reload')


mock_mlstring = 'light.toggle@10'  # mock machine learning output - '@' as deliminator

print(mlstring_to_astring('light.toggle@10'))  # test print with mock string
write_to_automations('light.toggle@10')  # test write with mock string
