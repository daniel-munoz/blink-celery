from blink.blink import Blink
import os


def connect():
    return Blink(email=os.getenv('BLINK_USER'), password=os.getnev('BLINK_PASSWORD'))
