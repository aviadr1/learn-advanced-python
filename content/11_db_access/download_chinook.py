import urllib.request
import zipfile
from functools import partial
import os
import sys

chinook_url = 'http://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip'
chinook_zip = 'chinook.zip'
chinook_db = 'chinook.db'

def download(url=chinook_url, zipname=chinook_zip, filename=chinook_db):
    if not os.path.exists(zipname):
        print('downloading', zipname, end='', file=sys.stderr)
        with urllib.request.urlopen(url) as response:
            with open(zipname, 'wb') as f:
                for data in iter(partial(response.read, 8*1024), b''):
                    print('.', end='', file=sys.stderr)
                    f.write(data)

    zipfile.ZipFile(zipname).extractall()
    assert os.path.exists(filename)
    print ('ready:', os.path.realpath(filename))

if __name__ == '__main__':
    download()
