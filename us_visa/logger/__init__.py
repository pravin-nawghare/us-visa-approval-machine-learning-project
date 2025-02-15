#custom logger
#refer python logging documentation

import logging
import os
from pathlib import Path

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

#log_folder = Path('D:/Data-Sorting/us-visa-approval-machine-learning-project')
#logs_path = os.path.join(from_root(), log_dir, LOG_FILE) - from video
#logs_path = os.path.join(log_folder, log_dir, LOG_FILE) - mine
#os.makedirs(log_dir, exist_ok=True)
log_paths = from_root(log_dir, mkdirs=True) #from documentaion of from-root

logging.basicConfig(
    filename='logs',
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

