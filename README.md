__NOTE__: This repository is no longer updated. Please check out PHI handling in [dicom-utils](https://github.com/medcognetics/dicom-utils).
***

# DICOM Protected Health Information Check
Check DICOM files for confidential information and optionally overwrite the files with anonymized copies.
## Usage
First create a Python virtual environment and run all necessary setup with the following commad:
```
$ make init
```
Then run the tool with the help menu flag `-h` to see detailed information for using the tool:
```
$ env/bin/python3 -m dicom_phi_check -h
```
## Anonymization
If anonymization is enabled, fields defined in
[this script](https://github.com/medcognetics/dicom-anonymizer/blob/master/dicomanonymizer/dicomfields.py)
are anonymized
with the exception of fields which are affected by additional rules located 
[here](https://github.com/medcognetics/dicom-phi-check/blob/master/dicom_phi_check/anonymize.py).
