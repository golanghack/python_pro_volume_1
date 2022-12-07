#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--SINGLETON-->"""

import os 
import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tk 
import Main 
import TkUtil

def main():
    app = tk.Tk()
    app.title('Currency')
    TkUtil.set_application_icons(app, os.path.join(os.path.dirname(os.path.relpath(__file__)), 'images'))
    Main.Window(app)
    app.mainloop()
    
    
if __name__ == '__main__':
    main()