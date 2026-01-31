import sys
from dropbox_helper.list_files import list_files

def main():
    if len(sys.argv) < 4:
        print("Usage:")
        print("  dropbox_helper list /path [--recursive]")
        print("  dropbox_helper rename_starred /path [--dry-run]")
        sys.exit(1)

    command = sys.argv[1]
    path = sys.argv[2]
    recursive = "--recursive" in sys.argv

    if command == "list":
        list_files(path, recursive=recursive)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
