from __future__ import annotations
import logging

class LoggerDecorator:
    
    def __init__(self, func: callable) -> None:
        self.func = func
        
    def __call__(self, *args: list, **kwargs: dict) -> any:
        try:
            return self.func(*args, **kwargs)
        except:
            issue = "exception in " + self.func.__name__ +'\n'
            issue = issue + '----------------------\
            --------------------------------------------\n'
            self.create_logger().exception(issue)    
        raise TypeError("Type Error exception")
    
    
    def create_logger(self) -> Logger:
        logger = logging.getLogger('exc_logger')
        logger.setLevel(logging.INFO)
        
        logfile = logging.FileHandler('exc_logger.log')
        pattern = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        
        formatter = logging.Formatter(pattern)
        logfile.setFormatter(formatter)
        logger.addHandler(logfile)
        
        return logger
 
@LoggerDecorator
def divStringByInt():
    return 'Bla bla bla' / 4

@LoggerDecorator
def divNumberByZero():
    return 66 / 0

if __name__ == '__main__':
    # divStringByInt()
    divNumberByZero()
