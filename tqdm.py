""" Simple script to showcase the tqdm library"""
from tqdm import tqdm
import time

i = 1
for i in tqdm(range(int(60))):
    time.sleep(1)