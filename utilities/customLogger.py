import logging
import os

class CustomLogger:

    @staticmethod
    def setup_logger():
        # Ensure logs folder exists
        os.makedirs("logs", exist_ok=True)

        # Configure logging
        logging.basicConfig(
            filename="logs/automation.log",
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            force=True  # ensures reconfiguration even if logging was set before
        )

        # Return a named logger
        return logging.getLogger("automation")