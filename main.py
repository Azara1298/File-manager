from hasher import FileHasher
from files import Files
from sketch import File
from pathlib import Path
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="File organization and management tool")
    parser.add_argument(
        "directory",
        nargs="?",
        default=None,
        help="Path to the target directory (default: interactive prompt)"
    )
    args = parser.parse_args()

    # If no directory was passed, ask the user
    if args.directory is None:
        user_input = input("Enter a directory path or type 'cwd' to use the current working directory: ").strip()

        if user_input.lower() == "cwd":
            dir_path = os.getcwd()
        else:
            dir_path = os.path.abspath(user_input)
    else:
        # If a directory *was* passed via CLI
        dir_path = os.path.abspath(args.directory)

    print(f"Using directory: {dir_path}")

    
    files = Files(dir_path)
    files.deep_scan_directory()

    file_hasher = FileHasher(files)
    hash_map = file_hasher.hash_files()
    duplicates = file_hasher.find_duplicates(hash_map)

    if duplicates:
        print(f"Found {len(duplicates)} duplicate files.")
        files.delete_duplicates(duplicates)
    else:
        print("No duplicate files found.")

    files.sort_by_mtype()

if __name__ == "__main__":
    main()

