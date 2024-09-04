import sys
import time

indent = 0
indent_increase = True

try:
    while True:
        print(" " * indent, end="")
        print("******")
        time.sleep(0.1)

        if indent_increase:
            indent += 1
            if indent > 4:
                indent_increase = False

        else:
            indent -= 1
            if indent == 0:
                indent_increase = True

except KeyboardInterrupt:
    sys.exit()
