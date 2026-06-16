import os
import sys

def main():
    this_dir = os.path.abspath(os.path.dirname(__file__))
    package_dir = os.path.join(os.path.dirname(this_dir), "form-packages")
    if not package_dir.endswith(os.path.sep):
        package_dir += os.path.sep
    tmp_dir = os.environb.get(b"TMPDIR", b"/tmp")
    os.environb.setdefault(b"FORMTMP", tmp_dir)
    os.environb.setdefault(b"FORMTMPSORT", tmp_dir)
    form_path = os.path.join(this_dir, "tform")
    args = [form_path, "-I", package_dir] + sys.argv[1:]
    os.execv(form_path, args)
    exit(11)

if __name__ == "__main__":
    main()
