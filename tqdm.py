""" Simple script to showcase the tqdm library"""

from tqdm import tqdm
import time

i = 1
for _ in tqdm(range(60)):
    time.sleep(1)