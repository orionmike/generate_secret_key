cd ..
pyinstaller --onefile --windowed --icon=icon/icon.ico generate_secret_key.py --exclude-module matplotlib ^
                           --exclude-module scipy ^
                           --exclude-module distutils ^
                           --exclude-module PyQt4 ^
                           --exclude-module PyQt5 ^
                           --exclude-module pydoc ^
                           --exclude-module pythoncom ^
                           --exclude-module pytz ^
                           --exclude-module sqlite3 ^
                           --exclude-module pyz ^
                           --exclude-module pandas ^
                           --exclude-module numpy ^
                           --exclude-module sklearn ^
                           --exclude-module scapy ^
                           --exclude-module scrapy ^
                           --exclude-module sympy ^
                           --exclude-module kivy ^
                           --exclude-module pyramid ^
                           --exclude-module opencv ^
                           --exclude-module tensorflow ^
                           --exclude-module pipenv ^
                           --exclude-module pattern ^
                           --exclude-module mechanize ^
                           --exclude-module wxPython ^
                           --exclude-module pygi ^
                           --exclude-module pillow ^
                           --exclude-module pygame ^
                           --exclude-module pyglet ^
                           --exclude-module flask ^
                           --exclude-module django ^
                           --exclude-module pylint ^
                           --exclude-module pytube ^
                           --exclude-module odfpy ^
                           --exclude-module mccabe ^
                           --exclude-module pilkit ^
                           --exclude-module six ^
                           --exclude-module wrapt ^
                           --exclude-module astroid ^
                           --exclude-module isort ^
                           --exclude-module difflib ^
                           --exclude-module jinja2
pause