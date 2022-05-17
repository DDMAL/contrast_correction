# Contrast-Correction

Repository of the Rodan wrapper for Contrast Correction

# Python dependencies:
  * scikit-image (0.19.2)
  * numpy (1.22.3)

# Local Usage
Use **ColorCorrectionLocalTask.py** to run this job locally.
Parameters:
  * **-psr** `Path to folder with the original images` (**Default:** *datasets/images*)
  * **-out** `Path to folder for output processed images` (**Default:** *datasets/output*)
  * **-pfx** `Postfix for output files <image_name><output_postfix>.png` (**Default:** *_cc*)
  * **-c** `Amount to adjust contrast by. Can be negative.` (**Default:** *0.0*)
  * **-b** `Amount to adjust brightness by. Can be negative` (**Default:** *0.0*)
    
Example: `python3 ContrastCorrectionLocalTask.py -psr datasets/images/MS73 -out datasets/output/MS73 -pfx _cbc -c 127.0 -b 5.0`
