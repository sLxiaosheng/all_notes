#!D:\Coding_notes\notes\���ݽṹ&�㷨\���ݽṹ\data_structure_python\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'vext==0.7.3','console_scripts','vext'
__requires__ = 'vext==0.7.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('vext==0.7.3', 'console_scripts', 'vext')()
    )
