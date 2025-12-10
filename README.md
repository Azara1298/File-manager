# File Manager

A Python-based file management utility that provides tools for organizing, hashing, and managing files efficiently.

## Features

- **File Scanning**: Recursively scan directories to discover and catalog files
- **File Hashing**: Generate SHA-256 hashes for files to identify duplicates
- **Duplicate Detection**: Find and manage duplicate files in your system
- **File Organization**: Sort files by media type (images, videos, audio, documents)
- **File Metadata**: Track file properties including size, location, and name

## Project Structure

```
file_manager/
├── sketch.py          # Base File class implementation
├── filechild.py       # MediaFile class for media-specific operations
├── files.py           # Files collection management class
├── hasher.py          # File hashing and duplicate detection
├── docs/              # Project documentation
└── README.md          # This file
```
##Still working on my naming conventions
## Classes

### File (`sketch.py`)
Base class representing a file with the following features:
- Path management using `pathlib`
- File size calculation with human-readable formatting (B, KB, MB, GB)
- SHA-256 hashing for duplicate detection
- Getters and setters for controlled access to private attributes (name, location)

### MediaFile (`filechild.py`)
Extends the `File` class with media-type classification:
- Detects file type: image, video, audio, or document
- Categorizes files based on extension

### Files (`files.py`)
Manages collections of files with methods for:
- `scan_directory()`: Scans the immediate directory for files
- `deep_scan_directory()`: Recursively scans subdirectories
- `delete_duplicates()`: Moves duplicate files to a designated folder
- `sort_by_mtype()`: Organizes files by media type

### FileHasher (`hasher.py`)
Handles file hashing and duplicate detection:
- `hash_files()`: Generates SHA-256 hashes for all files
- `find_duplicates()`: Identifies duplicate files by comparing hashes

## Usage

```python
from files import Files
from hasher import FileHasher

# Create a Files object for a directory
file_manager = Files("./my_directory")

# Scan for files
file_manager.scan_directory()

# Create a hasher and find duplicates
hasher = FileHasher(file_manager)
hash_map = hasher.hash_files()
duplicates = hasher.find_duplicates(hash_map)

# Remove duplicates
file_manager.delete_duplicates(duplicates)

# Sort files by media type
file_manager.sort_by_mtype()
```

## Requirements

- Python 3.6+
- Standard library modules: `pathlib`, `os`, `shutil`, `hashlib`

## Installation

1. Clone the repository
2. No additional dependencies required - uses only Python standard library

```bash
git clone https://github.com/yourusername/file-manager.git
cd file-manager
```

## Future Improvements

- Complete the `sort_by_mtype()` implementation
- Add file move operations with proper location handling
- Add configuration file support
- Add command-line interface
- Add unit tests
- Add more file type categories

## License

This project is open source and available under the MIT License.

## Author
This is my first python project. I started learning python a few january 2025 i was on and of because of work and life commitments but now im fully commited to learning python and becoming a proficient python developer.
Ps it might be a while before i finish this project as i am still learning some other concepts and it all gets a bit overwhelming at times but i will get there eventually.

Azara Money Makonnen - First Project
