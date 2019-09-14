from pathlib import Path

# Absolute Path
# c:\Program Files\Microsoft
#   or /usr/local/bin on linux
# Relative Path

path = Path()
for glob in path.glob('*'):
    print(glob)