import string
import requests
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict, Counter
import logging
from logging.handlers import RotatingFileHandler
import time

# Налаштування логера
logger = logging.getLogger('file_sorter')
logger.setLevel(logging.INFO)

# Створення обробника для логування у файл
file_handler = RotatingFileHandler('mapreduce.log', maxBytes=10**6, backupCount=5)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s [%(threadName)s] %(message)s'))
logger.addHandler(file_handler)

# Створення обробника для виведення логів в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s [%(threadName)s] %(message)s'))
logger.addHandler(console_handler)

# Функція для отримання тексту за URL
def get_text(url):
    logger.info(f"Requesting text from URL: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        logger.info("Text successfully downloaded.")
        return response.text.lower()
    except requests.RequestException as e:
        logger.error(f"An error occurred while requesting text: {e}")
        return None
    
# Функція для видалення знаків пунктуації
def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

# Функція Map
def map_function(word):
    return word, 1

# Функція Shuffle
def shuffle_function(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()

# Функція Reduce
def reduce_function(key_values):
    key, values = key_values
    return key, sum(values)

# Функція MapReduce
def map_reduce(text):
    text = remove_punctuation(text)
    words = text.split()

    with ThreadPoolExecutor() as executor:
        mapped_values = list(executor.map(map_function, words))
    shuffled_values = shuffle_function(mapped_values)

    with ThreadPoolExecutor() as executor:
        reduced_values = list(executor.map(reduce_function, shuffled_values))

    return dict(reduced_values)

# Функція для візуалізації результатів
def visualize_results(word_counts):
    top_words = Counter(word_counts).most_common(10)
    words, counts = zip(*top_words)
    words = reversed(words)
    counts = reversed(counts)
    
    plt.barh(list(words), list(counts))
    plt.xlabel('Frequency')
    plt.ylabel('Words')
    plt.title('Top 10 Most Frequent Words')
    plt.show()

if __name__ == "__main__":
    start_time = time.time()

    url = "https://gutenberg.net.au/ebooks01/0100021.txt"
    text = get_text(url)
    
    if text:
        word_counts = map_reduce(text)
        
        # Логування топ-слів
        logger.info("Top 10 most frequent words:")
        for word, count in Counter(word_counts).most_common(10):
            logger.info(f"Word: {word}, Frequency: {count}")
        
        # Логування часу виконання
        elapsed_time = time.time() - start_time
        logger.info(f"Execution time: {elapsed_time:.2f} seconds.")

        # Візуалізація результатів
        visualize_results(word_counts)
    else:
        logger.error("Error: Unable to get the input text.")
