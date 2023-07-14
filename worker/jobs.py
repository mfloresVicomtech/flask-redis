import time
from datetime import datetime as dt


# Do a long task based on the specified delay:
def long_task(args):
    delay = int(args.get('delay', 1))
    print(f"Doing long task: delay {delay} sec")
    time.sleep(delay)
    return f"Some long task done in {delay} seconds"


# Do a IO intensive task based on a specified amount of data to read:
def io_task(args):
    '''File operations (such as logging) can block the
    event loop: run them in a thread pool.'''
    amount = int(args.get('amount', 1000000000))
    print(f'[{dt.now()}] {{blocking_io}}: Starting')
    with open('/dev/urandom', 'rb') as f:
        start_time = dt.now()
        resp = f.read(amount)
        print(f'[{dt.now()}] {{blocking_io}}: took {dt.now()-start_time}')
        return resp


# Do a CPU intensive task based on a specified power to elevate 10 to for a math operation:
def cpu_task(args):
    '''CPU-bound operations will block the event loop:
    in general it is preferable to run them in a
    process pool.'''
    power = int(args.get('power', 7))
    print(f'[{dt.now()}] {{cpu_bound}}: Starting')
    start_time = dt.now()
    resp = sum(i * i for i in range(10 ** power))
    print(f'[{dt.now()}] {{cpu_bound}}: took {dt.now()-start_time}')
    return resp

