from enum import Enum


class Toaster:

    def __init__(self, toaster_id):
        self.id = toaster_id
        self.status = ToasterStatus.IDLE


class ToasterStatus(Enum):
    IDLE = 0
    WAIT_MODE = 1