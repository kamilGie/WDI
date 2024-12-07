from PIL import Image
import os

# nie refaktoryzowalme to tylko napisalem w 15 m prosze nie oceniac plz


def apply_custom_color_mapping(
    input_folder,
    output_folder,
    prefix="black_",
    white_replacement=(38, 44, 54, 255),
    black_replacement=(101, 108, 118, 255),
):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{prefix}{filename}")

            with Image.open(input_path).convert("RGBA") as img:
                width, height = img.size
                pixels = img.load()

                for x in range(width):
                    for y in range(height):
                        r, g, b, a = pixels[x, y]

                        brightness = (r + g + b) / 3
                        t = brightness / 255

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

                        pixels[x, y] = (new_r, new_g, new_b, new_a)

                # Konwersja na tryb RGB przed zapisem
                img_rgb = img.convert("RGB")
                img_rgb.save(output_path, "JPEG")
                print(f"Zapisano: {output_path}")


# Użycie
inputOutput_folder = "../../../../kolosy/"
apply_custom_color_mapping(
    inputOutput_folder,
    inputOutput_folder,
    white_replacement=(38, 44, 54, 255),
    black_replacement=(205, 217, 229, 255),
)
