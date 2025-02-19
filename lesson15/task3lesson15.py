#task3lesson15.py


"""
TV controller

Create a simple prototype of a TV controller in Python. It'll use the following commands:

    first_channel() - turns on the first channel from the list.
    last_channel() - turns on the last channel from the list.
    turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
    next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
    previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
    current_channel() - returns the name of the current channel.
    exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.

 

The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.

'''

CHANNELS = ["BBC", "Discovery", "TV1000"]

 class TVController:

pass

 controller = TVController(CHANNELS)

controller.first_channel() == "BBC"

controller.last_channel() == "TV1000"

controller.turn_channel(1) == "BBC"

controller.next_channel() == "Discovery"

controller.previous_channel() == "BBC"

controller.current_channel() == "BBC"

controller.exists(4) == "No"

controller.exists("BBC") == "Yes"

'''
"""


CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_index = 0  
        
    def first_channel(self):
        self.current_index = 0
        return self.channels[self.current_index]

    def last_channel(self):
        self.current_index = len(self.channels) - 1
        return self.channels[self.current_index]

    def turn_channel(self, N):
        if 1 <= N <= len(self.channels):
            self.current_index = N - 1
            return self.channels[self.current_index]
        else:
            return "No such channel"

    def next_channel(self):
        self.current_index = (self.current_index + 1) % len(self.channels)
        return self.channels[self.current_index]

    def previous_channel(self):
        self.current_index = (self.current_index - 1) % len(self.channels)
        return self.channels[self.current_index]

    def current_channel(self):
        return self.channels[self.current_index]

    def exists(self, N_or_name):
        if isinstance(N_or_name, int):
            return "Yes" if 1 <= N_or_name <= len(self.channels) else "No"
        elif isinstance(N_or_name, str):
            return "Yes" if N_or_name in self.channels else "No"
        else:
            return "No"


def test_class():
    controller = TVController(CHANNELS)

    assert controller.first_channel() ==  "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.exists(4) == "No"
    assert controller.exists("BBC") == "Yes"
    
    return "All assertions passed."

if __name__ == "__main__":

    print(test_class())