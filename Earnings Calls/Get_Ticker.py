import re

import os
path, dirs, files = next(os.walk("C:/Users/Scott/Documents/Python Things/Earnings Calls/Todays Videos"))

for file in files:
    s = file
    m = re.search(r"\(([A-Za-z0-9_]+)\)", s)
    print(m.group(1))
    
