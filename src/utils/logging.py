import logging

# Set up the logger for the current module
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Define the log format
logFormat = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
logFormatter = logging.Formatter(fmt=logFormat, style="%")

# Set up a stream handler to output logs to the console
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)

# Add the stream handler to the logger
logger.addHandler(streamHandler)