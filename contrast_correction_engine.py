from skimage.io import imread, imsave
import numpy as np

def load_image(input_path):
    # Import image
    img = imread(input_path)
    return img

def save_image(output_path, img):
    # Save results
    imsave(output_path, img)

def contrast_and_brightness(img, contrast, brightness):
    """ Adjusts the contrast and brightness of the image.

    Parameters:
        img (np.ndarray): Image with shape (W, H, 4) or (W, H, 3) or (W, H) with dtype=uint8.
        contrast (float): The amount to adjust contrast by.
        brightness (float): The amount to adjust brightness by.

    Returns:
        img (np.ndarray): Image with same shape as input image and dtype=uint8.
    """

    img = np.int16(img)
    img = img * (contrast/127+1) - contrast + brightness
    img = np.clip(img, 0, 255)
    img = np.uint8(img)

    return img

def main():
    img = load_image('../datasets/images/bounding/test.png')
    img = contrast_and_brightness(img, 127, 0.0)
    save_image('../datasets/results/result.png', img)

if __name__ == "__main__":
    main()