import sys
from PIL import Image, ImageSequence, ImageShow
import os
import pathlib


def main():
    img_path = pathlib.Path(sys.argv[1])
    print(img_path.absolute())
    img = Image.open(img_path)
    out_dir = img_path.parent / (img_path.name + "split")
    out_dir.mkdir(exist_ok=True)
    file: pathlib.Path
    for file in out_dir.iterdir():
        file.unlink()
    for i, frame in enumerate(ImageSequence.Iterator(img)):
        frame.save(out_dir / f"{i}.png")


if __name__ == "__main__":
    main()
