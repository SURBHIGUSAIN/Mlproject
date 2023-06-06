# this is used to log all the execution details whenever execeution happens  to track if there are any error
# even the custom exception errors

import logging
import os
from datetime import datetime

log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# name of the log file will be the datetime of the execution i.e datetime.now
# the file name will be stored at current working directory and be named as logs+log_files
log_path = os.path.join(os.getcwd(), "logs", log_file)
# tells that even if there is a dorectory already , keep appending new files
os.makedirs(log_path, exist_ok=True)

log_file_path = os.path.join(log_path, log_file)

logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
# logging.basicConfig() : It allows you to specify the format of the log messages,
# the level of the messages to be logged, and the destination of the log output (such as a file or the console)
# The call to logging. basicConfig() is to alter the root logger
# whenevr i use logging.info or import logging and write any print message ,it will create logging.basicinfo
# then it will use this basic config and print the mentioned filename and format the message as written

if __name__ == "__main__":
    logging.info("Starting logging")
