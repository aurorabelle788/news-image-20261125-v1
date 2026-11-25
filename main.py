"""Copy the entry image to the output directory.

The entry is a single hand-drawn newspaper front page (entry.png) that sums
up the world news of Wednesday 25 November 2026. This program does nothing
but copy that image, byte for byte, to $MAKEFUN_OUTPUT_DIR/entry.png, so the
two grader runs always produce identical bytes. Standard library only.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    src_size = os.path.getsize(SRC)
    dst_size = os.path.getsize(dst)
    if dst_size != src_size:
        raise SystemExit("copy failed: size mismatch %d != %d" % (dst_size, src_size))
    if _sha256(dst) != _sha256(SRC):
        raise SystemExit("copy failed: sha256 mismatch")
    print("wrote %s (%d bytes)" % (dst, dst_size))


if __name__ == "__main__":
    main()
