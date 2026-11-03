import matplotlib.pyplot as plt
import image_loader as img_load


def show_image_jpg(path):
    image = img_load.get_raw_image(path)

    print("Висота, Ширина, Кількість каналів:", image.shape[0], image.shape[1], image.shape[2])

    plt.imshow(image, cmap="gray")
    plt.show()


def show_black_and_white_image(path):
    bw_image = img_load.get_black_white_image(path)

    print("Висота, Ширина, Кількість каналів, Максимальна яскравість: ", bw_image.shape[0], bw_image.shape[1], "1", bw_image.max())

    plt.imshow(bw_image, cmap="gray")
    plt.show()


def show_decompressed_image(decompressed_image, quality=0.95):
    print("Висота, Ширина, Кількість каналів, Максимальна яскравість: ", decompressed_image.shape[0], decompressed_image.shape[1], "1", round(decompressed_image.max(), 5))

    plt.title(f"Поріг поясненої дисперсії: {int(quality * 100)}%")
    plt.imshow(decompressed_image, cmap="gray")
    plt.show()


def show_cumulative_variance(component_counts, variance_percent, n_components, quality):
    plt.plot(component_counts, variance_percent)
    plt.axhline(y=quality * 100, linestyle="--")
    plt.axvline(x=n_components, linestyle="--")

    plt.xlabel("Кількість компонент")
    plt.ylabel("Накопичена пояснена дисперсія, %")
    plt.title("Пояснена дисперсія PCA")
    plt.show()
