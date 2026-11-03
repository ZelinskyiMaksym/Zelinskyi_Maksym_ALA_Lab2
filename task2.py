import image_compression as img_comp
import visualization as vis
from pathlib import Path


def show_one_compression(path):
    compressed_image, image_mean, matrix_ofk_eigenvectors = img_comp.compress_image(path, show_cum_var=True)
    image = img_comp.image_decompression(compressed_image, image_mean, matrix_ofk_eigenvectors)

    vis.show_image_jpg(path)
    vis.show_black_and_white_image(path)
    vis.show_decompressed_image(image)


def show_difference_in_compressions(path):
    # Quality = 95%
    compressed_image, image_mean, matrix_of_selected_eigenvectors = img_comp.compress_image(path)
    image = img_comp.image_decompression(compressed_image, image_mean, matrix_of_selected_eigenvectors)

    vis.show_decompressed_image(image)

    # Quality = 30%
    compressed_image, image_mean, matrix_of_selected_eigenvectors = img_comp.compress_image(path, 0.3)
    image = img_comp.image_decompression(compressed_image, image_mean, matrix_of_selected_eigenvectors)

    vis.show_decompressed_image(image, 0.3)

    # Quality = 60%
    compressed_image, image_mean, matrix_of_selected_eigenvectors = img_comp.compress_image(path, 0.6)
    image = img_comp.image_decompression(compressed_image, image_mean, matrix_of_selected_eigenvectors)

    vis.show_decompressed_image(image, 0.6)

    # Quality = 90%
    compressed_image, image_mean, matrix_of_selected_eigenvectors = img_comp.compress_image(path, 0.9)
    image = img_comp.image_decompression(compressed_image, image_mean, matrix_of_selected_eigenvectors)

    vis.show_decompressed_image(image, 0.9)

    # Quality = 99%
    compressed_image, image_mean, matrix_of_selected_eigenvectors = img_comp.compress_image(path, 0.99)
    image = img_comp.image_decompression(compressed_image, image_mean, matrix_of_selected_eigenvectors)

    vis.show_decompressed_image(image, 0.99)


def run_task2():
    print("\nЗадача 2")
    images_dir = Path(__file__).resolve().parent / "images"
    show_one_compression(images_dir / "SnowOwlBear.jpg")
    show_one_compression(images_dir / "Cool_Image_of_players_in_DND.jpg")
    show_one_compression(images_dir / "Cool_Pumpkin.jpg")

    show_difference_in_compressions(images_dir / "Description_of_DND.jpg")
    show_difference_in_compressions(images_dir / "Dragon_fight_colored.jpg")

    # show_one_compression(images_dir / "Crusader.jpg")
    # show_one_compression(images_dir / "Death.jpg")
    # show_one_compression(images_dir / "Death_Knight.jpg")
    # show_one_compression(images_dir / "Description_of_DND.jpg")
    # show_one_compression(images_dir / "Dragon_fight.jpg")
    # show_one_compression(images_dir / "Dragon_fight_colored.jpg")
    # show_one_compression(images_dir / "Epic_Dragon_Fight.jpg")
    # show_one_compression(images_dir / "Flamy_rain.jpg")
    # show_one_compression(images_dir / "Lich.jpg")
    # show_one_compression(images_dir / "War.jpg")
    # show_one_compression(images_dir / "Scary_medusa.jpg")
    # show_one_compression(images_dir / "Tiamat.jpg")
    print("Завершено виконання: Задача 2\n")
