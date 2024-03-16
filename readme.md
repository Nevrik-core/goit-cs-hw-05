# File Sorting Script

This script asynchronously sorts files in a specified source directory, distributing them into subdirectories in the target directory based on their file extensions. It logs all actions to both the console and a log file, providing a detailed account of the script's operation.

## Installation

Before running the script, ensure that you have installed the required dependencies with the following command:

```bash
pip install aiofiles aiopath
```

## Usage

To run the script, use the following command in the terminal:

```
python3 main.py <path_to_source_folder> <path_to_target_folder>
```

Here, `<path_to_source_folder>` is the path to the folder with the files you want to sort, and `<path_to_target_folder>` is the path to the folder where subdirectories will be created based on file extensions and into which the sorted files will be moved.

## Features

- Asynchronous file reading and copying to enhance performance with large datasets.
- Automatic creation of subdirectories based on file extensions in the target directory.
- Ignores hidden files and directories (e.g., .git), as well as files with names that look like hash codes.
- Detailed logging of script activity to a log file and the console, providing full visibility into the sorting process.

# MapReduce Text Analysis Script

The text analysis script (map_reduce.py) performs text analysis using the MapReduce paradigm. It downloads text from a given URL, analyzes the frequency of word usage, and visualizes the top words with the highest usage frequency.

## Installation

Before running the script, ensure that you have installed the required dependencies with the following command:

```bash
pip install requests matplotlib
```

## Usage

To run the text analysis script, use the following command in the terminal:

```
python3 map_reduce.py
```

## Features

- Downloads text from a specified URL.
- Performs text analysis using the MapReduce paradigm for efficient word frequency counting.
- Uses multithreading to enhance performance when processing large datasets.
- Visualizes the top 10 most frequent words in the analyzed text.
- Logs all actions to both the console and a log file, providing detailed insights into the script's operation.

## logging

Both scripts log detailed information about their execution to file_sorting.log and mapreduce.log, respectively, and output logs to the console for easy monitoring and troubleshooting.
