import subprocess
from src.core.logger import get_logger

log = get_logger(level="DEBUG")
#result = subprocess.run(['systeminfo'], capture_output=True, text=True)
result = subprocess.run(['uname', '-a'], capture_output=True, text=True)
log.debug(result.stdout)