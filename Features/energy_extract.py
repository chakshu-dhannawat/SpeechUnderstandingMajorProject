import numpy as np
import argparse
import numpy as np
from pathlib import Path
from tqdm import tqdm
from scipy.io.wavfile import read


def calculate_energy_features(signal, sample_rate, window_length_ms=25, shift_ms=10):
    window_length_samples = int(window_length_ms * sample_rate / 1000)
    shift_samples = int(shift_ms * sample_rate / 1000)
    energy_features = []
    for i in range(0, len(signal) - window_length_samples + 1, shift_samples):
        window = signal[i:i+window_length_samples]
        energy = np.sum(window ** 2)
        energy_features.append(energy)
    return np.array(energy_features)


def extract_energy(args):
    print(
        f"Extracting energy values for dataset at {args.in_dir} and saving it in {args.out_dir}")
    for in_path in tqdm(list(args.in_dir.rglob("*.wav"))):
        sr, audio = read(in_path)
        energy = calculate_energy_features(audio, sr)
        out_path = args.out_dir / in_path.relative_to(args.in_dir)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        np.save(out_path.with_suffix(".npy"), energy)


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
    extract_energy(args)
