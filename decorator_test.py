import functools

def log(text):
    def decora(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decora
  
@log('execute')
def now():
    print '2013-12-25'
