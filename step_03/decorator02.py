def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'[*] Время выполнения: {end-start} секунд.')
    return wrapper

@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')

@benchmark
def fetch_webpage1():
    import requests
    webpage = requests.get('http://ya.ru')


fetch_webpage()
fetch_webpage1()
