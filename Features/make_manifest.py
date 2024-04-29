import argparse
from tqdm import tqdm
from pathlib import Path

def make_manifest(args):
    with open(args.file_name, "w") as f:
        for in_path in tqdm(list(args.in_dir.rglob(f"*.wav"))):
            f.write(in_path+" speaker1" + "\n")
        f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "in_dir",
        metavar="in-dir",
        help="path to the dataset directory.",
        type=Path,
    )
    parser.add_argument(
        "file_name",
        type=str,
    )
    parser.add_argument()
    args = parser.parse_args()
    make_manifest(args)