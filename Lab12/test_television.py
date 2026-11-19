import pytest

from television import *



class TestTelevision:
    def test__init__(self) -> None:
        tv = Television()
        assert tv.status == False
        assert tv.muted == False
        assert tv.volume == Television.MIN_VOLUME
        assert tv.channel == Television.MIN_CHANNEL

    def test_power(self) -> None:
        tv = Television()
        tv.power()
        assert tv.status == True
        tv.power()
        assert tv.status == False

    def test_mute(self) -> None:
        tv = Television()
        tv.power()
        tv.mute()
        assert tv.muted == True
        tv.mute()
        assert tv.muted == False
        tv.volume_up()
        tv.mute()
        assert tv.muted == True
        tv.volume_down()
        tv.power()
        tv.mute()
        assert tv.muted == False
        tv.power()
        tv.mute()
        assert tv.muted == True

    def test_channel_up(self) -> None:
        tv = Television()
        tv.power()
        tv.channel_up()
        assert tv.channel == 1
        tv.power()
        tv.channel_up()
        assert tv.channel == 1
        tv.power()
        tv.channel_up()
        tv.channel_up()
        tv.channel_up()
        assert tv.channel == 0


    def test_channel_down(self) -> None:
        tv = Television()
        tv.power()
        tv.channel_down()
        assert tv.channel == 3
        tv.power()
        tv.channel_down()
        assert tv.channel == 3
        tv.power()
        tv.channel_down()
        tv.channel_down()
        tv.channel_down()
        tv.channel_down()
        assert tv.channel == 3

    def test_volume_up(self) -> None:
        tv = Television()
        tv.power()
        tv.muted()
        tv.volume_up()
        assert tv.volume == 1
        tv.muted()
        tv.power()
        tv.volume_up()
        assert tv.volume == 1
        tv.power()
        tv.volume_up()
        assert tv.volume == 2
        tv.volume_up()
        assert tv.volume == 2

    def test_volume_down(self) -> None:
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()
        assert tv.volume == 2
        tv.power()
        tv.volume_down()
        assert tv.volume == 2
        tv.power()
        tv.volume_down()
        assert tv.volume == 1
        tv.volume_down()
        assert tv.volume == 0
        tv.volume_down()
        assert tv.volume == 0

if __name__ == "__main__":
    test = TestTelevision()
    test.test__init__()
    test.test_power()
    test.test_mute()
    test.test_channel_up()
    test.test_channel_down()
    test.test_volume_up()
    test.test_volume_down()