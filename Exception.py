import time
def causeError():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1/0
    except Exception:
        print('There was some sort of error!')
    finally:
        print(f'Fucntion took {time.time - start} to execute')
causeError()

