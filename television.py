"""
Class represents a television with basic functionality such as power, mute
,channel control, and volume control.
"""


class Television:
    """
    Local variables created for purposes
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Sets initial values for the television's status, mute state, volume, and channel.
        ::status:: Boolean set to off
        ::muted:: Boolean set to off
        ::volume:: Integer set to minimum volume
        ::channel:: Integer set to minimum channel
        """
        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the power status of the television.
        If the television is off, it turns on. If it's on, it turns off.
        """
        if self.status == False:
            self.status = True
        else:
            self.status = False

    def mute(self) -> None:
        """
        Toggles the mute status of the television.
        If the television is not muted, it mutes it. If it's muted, it unmutes it.
        """
        if self.status == True:
            if self.muted == False:
                self.muted = True
            else:
                self.muted = False

    def channel_up(self) -> None:
        """
        Increases the channel number by 1, wrapping around to the minimum channel if the maximum channel is reached.
        This method only works if the television is on."""
        if self.status == True:
            if self.channel == self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL
            else:
                self.channel = self.channel + 1

    def channel_down(self) -> None:
        """
        Decreases the channel number by 1, wrapping around to the maximum channel if the minimum channel is reached.
        This method only works if the television is on.
        """
        if self.status == True:
            if self.channel == self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL
            else:
                self.channel = self.channel - 1

    def volume_up(self) -> None:
        """
        Increases the volume number by 1, wrapping around to the maximum volume if the minimum volume is reached.
        This method only works if the television is on.
        """
        if self.status == True:
            if self.volume == self.MAX_VOLUME:
                self.volume = self.MAX_VOLUME
            else:
                self.volume = self.volume + 1
            if self.muted == True:
                self.muted = False

    def volume_down(self) -> None:
        """
        Decreases the volume number by 1, wrapping around to the minimum volume if the maximum volume is reached.
        This method only works if the television is on.
        """
        if self.status == True:
            if self.volume == self.MIN_VOLUME:
                self.volume = self.MIN_VOLUME
            else:
                self.volume = self.volume - 1
            if self.muted == True:
                self.muted = False

    def __str__(self) -> str:
        """
        Returns a string representation of the television's current status, channel, and volume.
        If the television is muted, the volume is displayed as the minimum volume.
        """
        if self.muted == True and self.status != False:
            return f"Power = {self.status}, Channel = {self.channel}, Volume = {self.MIN_VOLUME}"
        else:
            return f"Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}"