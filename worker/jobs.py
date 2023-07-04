import time
from datetime import datetime as dt

def do_long_task(delay:int=1):
    # Do some long task here
    print(f"Doing long task: delay {delay} sec")
    time.sleep(delay)
    return f"Some long task done in {delay} seconds"

def do_long_io_task(amount:int=1000000000):
    '''File operations (such as logging) can block the
    event loop: run them in a thread pool.'''
    print(f'[{dt.now()}] {{blocking_io}}: Starting')
    with open('/dev/urandom', 'rb') as f:
        start_time = dt.now()
        resp = f.read(amount)
        print(f'[{dt.now()}] {{blocking_io}}: took {dt.now()-start_time}')
        return resp

def do_long_cpu_task(amount:int=7):
    '''CPU-bound operations will block the event loop:
    in general it is preferable to run them in a
    process pool.'''
    print(f'[{dt.now()}] {{cpu_bound}}: Starting')
    start_time = dt.now()
    resp = sum(i * i for i in range(10 ** amount))
    print(f'[{dt.now()}] {{cpu_bound}}: took {dt.now()-start_time}')
    return resp
