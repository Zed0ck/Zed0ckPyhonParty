# Fourth lesson in Python Party project.
# Small animation program where string goes back and forth.

import time, sys
indent = 0
indentIncreasing = True

# Use try except to run and exit program
try:
  while True:
    print(' ' * indent, end='')
    print('********')
    time.sleep(0.1)
    
    if indentIncreasing:
      indent = indent + 1
      if indent == 20: # Change direction
        indentIncreasing = False
    
    else:
      indent = indent - 1
      if indent == 0: # Change direction
        indentIncreasing = True
        
except KeyboardInterrupt:
  sys.exit()
