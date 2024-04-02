import time

class Retry(object):
    def __init__(self, function, sleep, retryCount):
        self.__maxRetries = retryCount
        self.__function = function
        self.__retrySleep = sleep

    def retry(self):
        for i in range(self.__maxRetries):
            try:
                time.sleep(self.__retrySleep) 
                self.__function()
                break
            except Exception:
                continue