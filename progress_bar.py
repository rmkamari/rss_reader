import time
from tqdm import tqdm


def progress(sec):
    for i in tqdm(range(sec)):
        time.sleep(1)

