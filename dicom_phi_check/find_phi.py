import copy
import difflib
import os
from typing import Iterator

import pydicom
from colorama import Fore, init
from dicomanonymizer import anonymizeDataset
from tqdm import tqdm

from dicom_phi_check.rules import rules

init()


def color_diff(diff):
    for line in diff:
        if line.startswith("+"):
            yield Fore.GREEN + line + Fore.RESET
        elif line.startswith("-"):
            yield Fore.RED + line + Fore.RESET
        elif line.startswith("?"):
            yield Fore.BLUE + line + Fore.RESET
        else:
            pass


def is_dicom(filename: str) -> bool:
    """DICOM files have a 128 byte preamble followed by bytes 'DICM'."""
    return open(filename, "rb").read()[128:132] == b"DICM"


def gen_dicoms(path: str) -> Iterator[str]:
    for root, folders, filenames in os.walk(path):
        for f in filenames:
            filename = os.path.join(root, f)
            if is_dicom(filename):
                yield filename


def find_phi(path: str, overwrite: bool) -> None:
    filenames = [path] if os.path.isfile(path) else gen_dicoms(path)

    for filename in tqdm(filenames):
        ds = pydicom.dcmread(filename)
        ds_str = str(copy.deepcopy(ds)).splitlines(keepends=True)
        anonymizeDataset(ds, rules)

        for diff in color_diff(difflib.ndiff(ds_str, str(ds).splitlines(keepends=True))):
            print(diff)

        if overwrite:
            ds.save_as(filename)
