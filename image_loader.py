from matplotlib.image import imread


def get_raw_image(path):
    raw_image = imread(path)
    return raw_image


def get_black_white_image(path):
    raw_image = get_raw_image(path)
    raw_image_sum = raw_image.sum(axis=2)

    bw_image = raw_image_sum
    if raw_image_sum.max() != 0:
        bw_image = raw_image_sum/raw_image_sum.max()

    return bw_image
