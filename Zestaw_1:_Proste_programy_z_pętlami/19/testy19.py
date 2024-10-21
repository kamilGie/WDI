import sys
import os
import importlib
### TU BEDA TESTY ###


sys.path.append(
    os.path.join(
        os.path.abspath(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../")
        ),
        "skrypty",
    )
)


def StworzTesty(funkcje):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.abspath(current_dir)
    path_parts = full_path.split(os.sep)
    sciezka_do_folderu = os.path.join(path_parts[-2], path_parts[-1])

    importlib.import_module("StworzTesty").StworzTesty(19, sciezka_do_folderu, funkcje)