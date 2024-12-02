from pdf2image import convert_from_path
import pytesseract
import os
from PIL import Image

# napisalem to w 15 minut i nie refaktorozowalem plz nie oceniac tego


def sklej_zdjecia(image1_path, image2_path, output_path):
    image1, image2 = Image.open(image1_path), Image.open(image2_path)

    total_height = image1.height + image2.height - 30
    max_width = max(image1.width, image2.width)

    new_image = Image.new("RGB", (max_width, total_height))

    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (0, image1.height - 30))

    new_image.save(output_path)


def podziel_pdf():
    """
    Dzieli ZbiorZadan.pdf na mniejsze obrazy w oparciu o lokalizację tekstu "Zadanie"

    """

    pdf_path = "../../ZbiorZadan.pdf"
    output_folder = "../zbior_zadan/"
    os.makedirs(output_folder, exist_ok=True)

    images = convert_from_path(pdf_path)
    for image in images:
        ocr_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

        pozycje, nr_zadan = [], []
        for i in range(len(ocr_data["text"]) - 1):
            text, nastepny_text = ocr_data["text"][i], ocr_data["text"][i + 1]
            if text.startswith("Zadanie") and (("." in nastepny_text) or ("." in text)):
                pozycje.append(ocr_data["top"][i] - 20)
                nr_zadan.append(nastepny_text.rstrip("."))

        poprzednia_wysokosci = 0
        for y, nr in zip(pozycje + [image.height], nr_zadan):
            zdjecie = image.crop((0, poprzednia_wysokosci, image.width, y))
            cropped_path = os.path.join(output_folder, f"{int(nr)-1}.png")
            if os.path.exists(cropped_path):
                zdjecie = image.crop((0, poprzednia_wysokosci + 180, image.width, y))
                tmp = os.path.splitext(cropped_path)[0] + "_2.png"
                zdjecie.save(tmp, "PNG")
                sklej_zdjecia(cropped_path, tmp, cropped_path)
                os.remove(tmp)
            else:
                zdjecie.save(cropped_path, "PNG")

            print(f"Zapisano fragment: {cropped_path}")
            poprzednia_wysokosci = y

        if pozycje:
            zdjecie = image.crop(
                (0, poprzednia_wysokosci, image.width, image.height - 250)
            )
            cropped_path = os.path.join(output_folder, f"{int(nr_zadan[-1])}.png")
            zdjecie.save(cropped_path, "PNG")


if __name__ == "__main__":
    podziel_pdf()
