import asyncio
from aiofile import async_open  
from aiopath import AsyncPath   
import argparse  
import logging 

# Налаштування логування
logger = logging.getLogger('file_sorter')
logger.setLevel(logging.INFO)

# Створення обробника для логування у файл
file_handler = logging.FileHandler('file_sorting.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))

# Створення обробника для логування у консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))

# Додавання обробників до логера
logger.addHandler(file_handler)
logger.addHandler(console_handler)

async def copy_file(source_path, destination_folder):
    # Функція для копіювання файлу
    destination_path = destination_folder / source_path.name
    try:
        async with async_open(source_path, 'rb') as source_file:
            content = await source_file.read()
        async with async_open(destination_path, 'wb') as dest_file:
            await dest_file.write(content)
        logger.info(f'File {source_path} has been successfully copied to {destination_path}.')
    except Exception as e:
        logger.error(f'Error copying file {source_path}: {e}')

async def read_folder(source_folder, output_folder):
    # Функція для читання директорії та виклику копіювання файлів
    async for path in source_folder.iterdir():
        if path.name.startswith('.') or path.name == '.git':
            continue  # Ігноруємо приховані файли та папки .git
        if await path.is_dir():
            await read_folder(path, output_folder)  # Рекурсивний виклик для підпапок
        else:
            # Перевіряємо, чи є у файла розширення
            if path.suffix.isalnum() or (path.suffix.startswith('.') and path.suffix[1:].isalnum()):
                extension = path.suffix[1:] 
                destination_folder = output_folder / extension
                await destination_folder.mkdir(exist_ok=True)  # Створення папки за необхідності
                await copy_file(path, destination_folder)

async def main(source_folder, output_folder):
    # Головна функція для ініціалізації процесу
    try:
        source_folder_path = AsyncPath(source_folder)
        output_folder_path = AsyncPath(output_folder)

        # Створення цільової папки, якщо вона не існує
        if not await output_folder_path.exists():
            await output_folder_path.mkdir(parents=True)
            logger.info(f'Created the target folder: {output_folder_path}')
        
        await read_folder(source_folder_path, output_folder_path)
        logger.info('File sorting script completed successfully.')
    except Exception as e:
        logger.error(f'Error in main: {e}')

if __name__ == "__main__":
    # Обробка аргументів командного рядка
    parser = argparse.ArgumentParser(description="Asynchronous file sorting into folders based on file extension.")
    parser.add_argument("source_folder", type=str, help="Source folder with files.")
    parser.add_argument("output_folder", type=str, help="Target folder for sorted files.")
    args = parser.parse_args()

    # Запуск головної функції
    asyncio.run(main(args.source_folder, args.output_folder))
