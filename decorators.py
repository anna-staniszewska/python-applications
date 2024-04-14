import time

def execution_time(unit='microseconds'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if unit == 'seconds':
                print(f"Execution time: {elapsed_time:.6f} seconds")
            elif unit == 'microseconds':
                print(f"Execution time: {elapsed_time * 1e6:.2f} microseconds")
            return result
        return wrapper
    return decorator

@execution_time(unit='microseconds')
def example_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

result = example_function()
print(f"Wynik funkcji przykładowej: {result}.")