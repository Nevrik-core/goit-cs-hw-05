# File Sorting Script

This script asynchronously sorts files in a specified source directory, distributing them into subdirectories in the target directory based on their file extensions. It logs all actions to both the console and a log file, providing a detailed account of the script's operation.

## Installation

Before running the script, ensure that you have installed the required dependencies with the following command:

```bash
pip install aiofiles aiopath aioshutil
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

## logging

The script logs detailed information about its execution, including the files being copied and any errors encountered. Logs are written to file_sorting.log in the current directory and are also output to the console. This allows for easy monitoring and troubleshooting.
