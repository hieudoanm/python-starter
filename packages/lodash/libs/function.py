"""
function
"""

import time

def debounce(func, wait = 0):
    """
    debounce
    """
    time.sleep(wait)
    func()

def delay(func, wait = 0, *args):
    """
    delay
    """
    time.sleep(wait)
    func(*args)
