import logging
import datetime
logging.basicConfig(
    filename ="Y_M_D.log",
    filemode="w",
    level=logging.INFO,
    format=" %(levelname)s - %(message)s"
)
data = datetime.datetime.now().strftime("%Y-%m-%d")
logging.info(f"date - {data}")