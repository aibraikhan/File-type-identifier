from pathlib import Path

def open_file(files):
    with open(files, "rb") as f:
        return f.read(16)

signatures = {
    b'\x89PNG\r\n\x1a\n': "PNG",
    b'%PDF-': "PDF",
    b'\xff\xd8\xff': "JPEG",
    b'#!': "sh"
}

def main():
    while True:
        try:
            files =  Path(input("Укажите файл: "))
            magic_bytes = open_file(files)
        except FileNotFoundError:
            print("Не наход")
            continue

        found = False
        for sig, name in signatures.items():
            if magic_bytes.startswith(sig):
                print("Название: ", name, "Сигнатура: ", sig.hex())
                print("Расширение файла: ", files.suffix)
                if name == "sh":
                    with open(files, "r") as r:
                       reading = r.read()
                       print("Вывод коммандного файла: ", reading)
                found = True
                break
        if not found:
            print("Неизвестный тип файла или Text file")
        what = input("\nНажмите Enter, чтобы проверить другой файл...")


