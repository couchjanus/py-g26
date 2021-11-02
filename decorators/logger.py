import logging
from functools import wraps

def create_logger():
    logger = logging.getLogger('exc_logger')
    logger.setLevel(logging.INFO)
    
    logfile = logging.FileHandler('exc_logger.log')
    pattern = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    formatter = logging.Formatter(pattern)
    logfile.setFormatter(formatter)
    logger.addHandler(logfile)
    
    return logger

logger = create_logger()

# print(logger)

def exception(logger):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except:
                issue = "exception in " + f.__name__ +'\n'
                issue = issue + '----------------------\
                --------------------------------------------\n'
                logger.exception(issue)
            raise
        return wrapper
    return decorator

@exception(logger)
def divStrByInt():
    return 'Bla bla bla' / 4

@exception(logger)
def divNumbByZero():
    return 66 / 0

if __name__ == '__main__':
    # divStrByInt()
    divNumbByZero()