import os

for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith(".png") and "depth" in filename:
            os.remove(os.path.join(root, filename))