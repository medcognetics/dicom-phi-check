import argparse

from dicom_phi_check.find_phi import find_phi


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="CLI tool for identifying and optionally overwriting DICOM fields with patient health information."
    )
    parser.add_argument("path", help="path to a DICOM file or folder with DICOM files")
    parser.add_argument(
        "--overwrite", help="overwrite original DICOM files with anonymized files", default=False, action="store_true"
    )
    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    find_phi(args.path, args.overwrite)


if __name__ == "__main__":
    main(parse_args())
