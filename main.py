from Logger.logHandler import create_log
from test import Test

logger = create_log()

Test.run_all_tests(logger)
