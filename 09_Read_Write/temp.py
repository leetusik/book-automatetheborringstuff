import os
from pathlib import Path

print(Path.cwd())
os.chdir("/Users/sugang/Desktop/projects")
print(Path.cwd())
print(Path.home())
