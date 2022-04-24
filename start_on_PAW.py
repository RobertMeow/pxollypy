from Application.webhook import main, app
import os
import sys

for module in ['flask']:
    if module not in sys.modules:
        os.system('python3 -m pip install {} --user'.format(module))

main()
