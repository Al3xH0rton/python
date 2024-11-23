class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        This method is used to initialize the TV values
        """

        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        This method is used to power on and off the TV
        """

        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        This method is used to mute and unmute the TV
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        This method is used to increase the channel on the TV
        """

        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel = self.__channel + 1

    def channel_down(self) -> None:
        """
        This method is used to decrease the channel on the TV
        """

        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel = self.__channel - 1

    def volume_up(self) -> None:
        """
        This method is used to increase the volume of the TV
        """
        if self.__status and not self.__muted:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume = self.__volume + 1
        elif self.__status and self.__muted:
                self.__volume = self.__volume + 1
                self.__muted = not self.__muted

    def volume_down(self) -> None:
        """
        This method is used to decrease the volume of the TV
        """
        if self.__status and not self.__muted:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume = self.__volume - 1
        elif self.__status and self.__muted:
                self.__volume = self.__volume - 1
                self.__muted = not self.__muted

    def __str__(self) -> str:
        """
        This method is used to provide data back to the main function
        :return:
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'