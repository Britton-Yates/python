class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL

    def power(self):
        if self.status == False:
            self.status = True
        else:
            self.status = False

    def mute(self):
        if self.muted == False:
            self.muted = True
        else:
            self.muted = False

    def channel_up(self):
        if self.status == True:
            if self.channel == self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL
            else:
                self.channel = self.channel + 1

    def channel_down(self):
        if self.status == True:
            if self.channel == self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL
            else:
                self.channel = self.channel - 1

    def volume_up(self):
        if self.status == True:
            if self.volume == self.MAX_VOLUME:
                self.volume = self.MAX_VOLUME
            else:
                self.volume = self.volume + 1
            if self.muted == True:
                self.muted = False

    def volume_down(self):
        if self.status == True:
            if self.volume == self.MIN_VOLUME:
                self.volume = self.MIN_VOLUME
            else:
                self.volume = self.volume - 1
            if self.muted == True:
                self.muted = False

    def __str__(self):
        if self.muted == True and self.status != False:
            return f"Power = {self.status}, Channel = {self.channel}, Volume = {self.MIN_VOLUME}"
        else:
            return f"Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}"