import time

def do_long_task(delay=1):
    # Do some long task here
    print(f"Doing long task: delay {delay} sec")
    time.sleep(delay)
    # url = requests.get(
    #     "https://api.thecatapi.com/v1/images/search").json()[0]['url']
    # print(url)
    
    return f"HOLA FUNCIONA con {delay} secs!!!!!!!"