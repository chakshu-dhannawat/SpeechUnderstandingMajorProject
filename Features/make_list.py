import os
import argparse

def make_data_lst(args):
    with open(args.file_name, "w") as f:
        for file in os.listdir(args.in_dir):
            f.write(file[:-4] + "\n")
        f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "in_dir",
        metavar="in-dir",
        help="path to the dataset directory.",
        type=str,
    )
    parser.add_argument(
        "file_name",
        type=str,
    )
    # parser.add_argument()
    args = parser.parse_args()
    make_data_lst(args)