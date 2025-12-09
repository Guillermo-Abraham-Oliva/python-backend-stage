import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

log = logging.getLogger(__name__)

LOG_DIR = Path("logs"); LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "app.log"

LOG_FORMAT = "%(asctime)s | %(levelname)-s | %(name)-17s | %(message)s"

def setup_logging(level=logging.INFO) -> None:
    logging.basicConfig(
        level=level,
        format=LOG_FORMAT,
        handlers=[
            logging.StreamHandler(),   # a consola
            RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=5, encoding="utf-8"),
        ], # hace 5 archivos de 1 Mb y va rotando para no acunular demasiado innecesario
    )
    log.info("Logging inicializado")
