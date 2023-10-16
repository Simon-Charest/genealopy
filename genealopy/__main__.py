from datetime import datetime
from genealopy.datetime_ import get_start_time, print_execution_time
from genealopy.app import run


if __name__ == "__main__":
    start: datetime = get_start_time()
    run()
    print_execution_time(start)
