#!D:\Coding_notes\notes\���ݽṹ&�㷨\���ݽṹ\data_structure_python\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'python-pyqt5-vstructui==0.4.0','console_scripts','vstructui'
__requires__ = 'python-pyqt5-vstructui==0.4.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('python-pyqt5-vstructui==0.4.0', 'console_scripts', 'vstructui')()
    )
