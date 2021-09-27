import time


def time_decorator(func):
    def call_func(*args, **kwargs):
        begin_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - begin_time
        print(str(func.__name__) + " is running " + str(run_time) + 's')
        return ret

    return call_func


"""usage"""


@time_decorator
def test01(number):
    for i in range(number):
        continue


if __name__ == '__main__':
    test01(1000)
