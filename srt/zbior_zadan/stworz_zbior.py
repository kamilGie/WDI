import fitz  # PyMuPDF
import os


def extract_tasks_from_pdf(pdf_path, output_folder, keyword="Zadania"):
    # Stwórz folder wyjściowy, jeśli nie istnieje
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Otwórz dokument PDF
    doc = fitz.open(pdf_path)
    task_counter = 1

    for page_number in range(len(doc)):
        page = doc[page_number]
        text_instances = page.search_for(keyword)  # Szukaj słowa kluczowego na stronie

        for rect in text_instances:
            # Rozszerz prostokąt wokół słowa kluczowego, aby uchwycić całe zadanie
            expanded_rect = fitz.Rect(
                rect.x0 - 50, rect.y0 - 50, rect.x1 + 50, rect.y1 + 100
            )
            # Wytnij zadanie jako obraz
            pix = page.get_pixmap(clip=expanded_rect)
            output_path = os.path.join(output_folder, f"{task_counter}.png")
            pix.save(output_path)
            print(f"Saved task {task_counter}: {output_path}")
            task_counter += 1

    doc.close()


# Użycie funkcji
pdf_path = "ZbiorZadan.pdf"
output_folder = "Zadania"
extract_tasks_from_pdf(pdf_path, output_folder)
