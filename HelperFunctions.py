def get_tile_size_of_img(input_image):
    height = input_image.shape[0]
    # length = input_image.shape[1]
    size_of_tile = height / 5
    return size_of_tile