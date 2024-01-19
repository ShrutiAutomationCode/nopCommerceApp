import logging


class LogGen:
    @staticmethod
    def loggen():

        logger = logging.getLogger('')
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler('./Logs/automation.log')
        file_handler.setLevel(logging.INFO)

        # Set the formatter for the file handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S%p')

        file_handler.setFormatter(formatter)
        # Add the file handler to the logger

        logger.addHandler(file_handler)
        return logger