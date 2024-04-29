from pathlib import Path
import argparse
from tqdm import tqdm


def make_data_lst(args):
    with open(args.file_name, "w") as f:
        for in_path in tqdm(list(args.in_dir.rglob(f"*.wav"))):
            f.write(in_path.removeSuffix(".wav"))
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
        metavar="file-name",
        help="name of the list file to be generated",
        type=str,
    )
    args = parser.parse_args()
    make_data_lst(args)
