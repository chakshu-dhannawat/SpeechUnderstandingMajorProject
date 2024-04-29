import argparse
import numpy as np
from pathlib import Path
import amfm_decompy.pYAAPT as pYAAPT
import amfm_decompy.basic_tools as basic
from tqdm import tqdm


def getPitch(file_path):
    signal = basic.SignalObj(file_path)
    return pYAAPT.yaapt(signal)


def extract_f0(args):
    print(
        f"Extracting F0 values and for dataset at {args.in_dir} saving it in {args.out_dir}")
    for in_path in tqdm(list(args.in_dir.rglob(f"*.wav"))):
        pitch = getPitch(in_path)
        out_path = args.out_dir / in_path.relative_to(args.in_dir)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        np.save(out_path.with_suffix(".npy"), pitch)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encode an audio dataset.")
    parser.add_argument(
        "in_dir",
        metavar="in-dir",
        help="path to the dataset directory.",
        type=Path,
    )
    parser.add_argument(
        "out_dir",
        metavar="out-dir",
        help="path to the output directory.",
        type=Path,
    )
    args = parser.parse_args()
    extract_f0(args)
