import argparse
import os.path as osp
import os
import glob
from pathlib import Path

import numpy as np
from skimage.io import imread, imsave
from contrast_correction_engine import contrast_and_brightness

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-psr", type=str, default="./datasets/images", 
                        help="Load <image_name>.png in this folder.")
    parser.add_argument("-out", type=str, default="./datasets/output",
                        help="Write <image_name><output_postfix>.png to this folder.")
    parser.add_argument("-pfx", type=str, default="_cc",
                        help="Write to <image_name><output_postfix>.png")
    parser.add_argument("-c", type=float, default=0.0,
                        help="Adjust contrast by this amount. Can be negative.")
    parser.add_argument("-b", type=float, default=0.0,
                        help="Adjust brightness by this amount. Can be negative.")
    args = parser.parse_args()
    return args

def load_image(image_path):
    """Load <image_path> as a ndarray with shape (width, height, 3).
    Only support rgb format.

    Parameters:
        image_path (str): Load <image path>. The image should be in RGB or RGBA.
        mode (str): A flag regarding how to load the image. For now it only supports rgb
    Returns:
        np.ndarray: Load image with shape (W, H, 3) with dtype=uint8. The channel order is RGB. 
    Exception:
        TypeError: Do not try to load a grey scale image.
    """
    image_rgb = imread(image_path)

    if image_rgb.dtype != np.uint8:
        raise TypeError("load_image should return dtype=uint8. Got an image {} with dtype {}".format(image_path, image_rgb.dtype))

    return image_rgb

def loader(args):
    """ A generator to load *.png locating inside <args.psr>.

    Parameters:
        args (argparse.Namespace): A namespace with <dataset_path> argument.
    Returns:
        str: Load image name.
        np.ndarray: Load image with shape (W, H, 3) with dtype=uint8. The channel order is RGB. 
    """
    image_path_list = [p for p in sorted(glob.glob(osp.join(args.psr, "*.png"))) if args.pfx not in p]
    for image_path in image_path_list:
        # Load image
        image_name = image_path.split("/")[-1]
        image_rgb = load_image(image_path)
        yield image_name, image_rgb

def writer(image, image_name, args):
    """Write <image> to <args.out> with a new name. <image name without its filetype><args.out>.<filetype>

    This function convert RGB to BGR and use opencv to write the image.
    Sklearn package runs significantly slower than opencv.
    Make sure the image is in RGB order!

    Parameters:
        image (np.ndarray): The output image with shape (W, H, 3) with dtype=uint8. The channel order is RGB. 
        image_name (str): the image_name from the loader function.
        args (argparse.Namespace): A namespace with arguments: <output_path>, <output_postfix>
    Returns:
        None
    """
    filename, filetype = image_name.split(".")
    new_image_name = "{}{}.{}".format(filename, args.pfx, filetype)
    output_path = osp.join(args.out, new_image_name)
    print ("Write to {}".format(output_path))

    imsave(output_path, image)

def main():
    args = getArgs()

    for image_name, image_rgb in loader(args):
        image_noBg = contrast_and_brightness(image_rgb, args.c, args.b)
        writer(image_noBg, image_name, args)

if __name__ == "__main__":
    main()