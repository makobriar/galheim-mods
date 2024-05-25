import urllib.request
import os
import shutil

CURR_DIR        = print(os.path.dirname(os.path.realpath(__file__)))
TMP_DIR_NAME    = 'tmp-downloads'
TMP_DIR         = tmpDir = os.path.join(CURR_DIR, TMP_DIR_NAME)

def create_tmp_dir():
    if not os.path.exists(TMP_DIR):
        os.makedirs(TMP_DIR)


def delete_tmp_dir():
    shutil.rmtree(TMP_DIR)


def download_vortex_mod(url, modName):
    create_tmp_dir()
    urllib.request.urlretrieve(url, os.path.join(TMP_DIR, modName))