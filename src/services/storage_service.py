import os

class StorageService:
    @staticmethod
    def save_image(folder, filename, content):
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, filename), 'wb') as f:
            f.write(content)

    @staticmethod
    def save_text(folder, filename, text):
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, filename), 'w', encoding='utf-8') as f:
            f.write(text)
