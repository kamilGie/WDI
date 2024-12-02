from PIL import Image
import os


def apply_custom_color_mapping(
    input_folder,
    output_folder,
    prefix="black_",
    white_replacement=(38, 44, 54, 255),
    black_replacement=(101, 108, 118, 51),
):
    # Tworzenie folderu wyjściowego, jeśli nie istnieje
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            # Ścieżki wejściowe i wyjściowe
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{prefix}{filename}")

            # Otwórz obraz
            with Image.open(input_path).convert("RGBA") as img:
                # Utwórz tło w zadanym kolorze

                # Przeprowadź zamianę kolorów
                width, height = img.size
                pixels = img.load()
                for x in range(width):
                    for y in range(height):
                        r, g, b, a = pixels[x, y]

                        # Oblicz jasność jako średnią RGB
                        brightness = (r + g + b) / 3

                        # Oblicz współczynnik jasności
                        t = brightness / 255

                        # Interpolacja między kolorami
                        new_r = int(
                            black_replacement[0] * (1 - t) + white_replacement[0] * t
                        )
                        new_g = int(
                            black_replacement[1] * (1 - t) + white_replacement[1] * t
                        )
                        new_b = int(
                            black_replacement[2] * (1 - t) + white_replacement[2] * t
                        )
                        new_a = int(
                            black_replacement[3] * (1 - t) + white_replacement[3] * t
                        )

                        # Ustaw nowy kolor piksela
                        pixels[x, y] = (new_r, new_g, new_b, new_a)

                # Zapisz obraz wynikowy
                img.save(output_path)


# Użycie
input_folder = "."  # Folder z obrazami wejściowymi
output_folder = "."  # Folder na zapisane obrazy
apply_custom_color_mapping(
    input_folder,
    output_folder,
    white_replacement=(38, 44, 54, 255),
    black_replacement=(205, 217, 229, 26),
)
