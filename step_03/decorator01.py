def decorator_function(func):
    def wrapper():
        print('Выполняем обёрнутую функцию: '+str(func))
        func()
        print('Выходим из обёртки: ')
    return wrapper

@decorator_function
def hello_world():
    print('Hello world!')

hello_world()