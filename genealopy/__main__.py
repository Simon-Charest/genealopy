from common import test
from common.datetime_ import datetime_

import app

if __name__ == '__main__':
    start = datetime_.get_start_time()
    test.run()
    app.run()
    datetime_.print_execution_time(start)
