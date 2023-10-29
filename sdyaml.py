import io
import os
import shutil
import sys

sourcepath = sys.argv[1]
# separator = "\\" if sourcepath[-1] != ':' and sourcepath[-1] != "\\" else ''
# sourcepath = f"{sourcepath}{separator}*.yaml"
targetpath = sys.argv[2]
# separator = "\\" if targetpath[-1] != ':' and targetpath[-1] != "\\" else ''
# targetpath = f"{targetpath}{separator}*.png"
print(f"{sourcepath} => {targetpath}")
sourcefiles = [f for f in os.listdir(sourcepath) if os.path.isfile(os.path.join(sourcepath, f))]
targetfiles = [f for f in os.listdir(targetpath) if os.path.isfile(os.path.join(targetpath, f))]

for f in [t for t in targetfiles if t.endswith('.png')]:
    yaml_name = "%s.yaml" % f[:f.index(".png")] 
    if yaml_name in sourcefiles:
        print(f"{yaml_name} -> {f}")
        # print(os.path.join(targetpath, yaml_name))
        shutil.copyfile(os.path.join(sourcepath, yaml_name), os.path.join(targetpath, yaml_name))