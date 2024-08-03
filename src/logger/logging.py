import os
import sys
import logging
from pathlib import Path

logging_str = "[%(asctime)s]: %(message)s"

log_filepath = os.path.join(Path(__file__).parent, "running_logs.log")

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)],
)

Logger = logging.getLogger("CNN_Classifier")
