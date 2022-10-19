CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.current_channel = channels[0]

    def first_channel(self):
        self.current_channel = self.channels[0]
        return self.current_channel

    def last_channel(self):
        self.current_channel = self.channels[-1]
        return self.current_channel

    def turn_channel(self, n):
        self.current_channel = self.channels[n-1]
        return self.current_channel

    def next_channel(self):
        current_channel_index = self.channels.index(self.current_channel)
        self.current_channel = self.channels[(current_channel_index+1) % len(self.channels)]
        return self.current_channel

    def previous_channel(self):
        current_channel_index = self.channels.index(self.current_channel)
        current_channel = self.channels[(current_channel_index - 1) % len(self.channels)]
        return current_channel

    def current_channel_func(self):
        return self.current_channel

    def is_exist(self, channel):
        if isinstance(channel, int) and 0 < channel <= len(self.channels):
            return "Yes"
        elif channel in self.channels:
            return "Yes"
        else:
            return "No"






