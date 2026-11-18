from memory_profiler import profile
import time


@profile
def slow_function():
    time.sleep(2)
    total = 0
    for i in range(10000):
        total += i ** 2
    return total

#before optimization
# @profile
# def fast_function():
#     total = 0
#     for i in range(100):
#         total += i ** 2
#     return total

#after optimization
@profile
def optimized_fast_function():
    n = 100
    return (n - 1) * n * (2 * n - 1) // 6  

@profile
def memory_intensive_function():
    total = 0
    for i in range(10000000):
        total += i ** 2
    return total


def main():
    slow_function()
    #fast_function()
    optimized_fast_function()
    memory_intensive_function()


if __name__ == "__main__":
    main()
