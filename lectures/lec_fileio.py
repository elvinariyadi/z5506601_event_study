""" lec_fileio.py

Companion codes for the lecture on reading and writing files
"""

import os

import toolkit_config as cfg


SRCFILE = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
DSTFILE = os.path.join(cfg.DATADIR, 'new_file.txt')


with open(SRCFILE, mode='r') as fobj:
    cnts = fobj.read()
    # Check if the object is closed inside the manager
    print(f'Is the fobj closed inside the manager? {fobj.closed}')

# Notice that we did not close the object when using a context manager
# But after exiting the context manager, the file will automatically close
print(f'Is the fobj closed after we exit the manager? {fobj.closed}')