import sys
from car_license_plate_identification.cli.blurring import blur_images
from car_license_plate_identification.cli.helpers import extract_argument_value

input_path = extract_argument_value(sys.argv, 'input')
output_path = extract_argument_value(sys.argv, 'output')
skip_nights = extract_argument_value(sys.argv, 'skip-nights', 'true').lower()

skip_nights = True if skip_nights == 'true' else False

blur_images(input_path, output_path, skip_nights)
