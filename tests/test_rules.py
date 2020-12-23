import pytest

from dicom_phi_check.rules import *


@pytest.mark.parametrize(
    "test_data",
    [
        ("1", 1),
        ("078Y", 78),
        ("090Y", 90),
        ("abcdefgh120ijklmnopqrts", 120),
    ],
)
def test_str_to_first_int(test_data) -> None:
    input_string, expected_int = test_data
    assert expected_int == str_to_first_int(input_string)


@pytest.mark.parametrize(
    "test_data",
    [
        ("1", "001Y"),
        ("000078Y", "078Y"),
        ("90Y", "90Y+"),
        ("abcdefgh120ijklmnopqrts", "90Y+"),
    ],
)
def test_age_to_anonymized_age(test_data) -> None:
    input_string, expected_output = test_data
    assert expected_output == age_to_anonymized_age(input_string)


def test_Handler_init() -> None:
    Handler(lambda x: x)


def test_Handler() -> None:
    ds = pydicom.Dataset()
    tag = 0x00000001
    ds[tag] = pydicom.DataElement(value=b"1", tag=tag, VR="CS")
    handler = Handler(lambda _: "x")
    handler(ds, tag)
    assert ds[tag].value == "x"
