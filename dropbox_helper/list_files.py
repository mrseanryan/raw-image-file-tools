import os
import dropbox
from dropbox.files import FileMetadata, FolderMetadata

def list_files(folder_path: str, recursive: bool = False):
    token = os.environ.get("DROPBOX_TOKEN")
    if not token:
        raise RuntimeError("DROPBOX_TOKEN environment variable not set")

    dbx = dropbox.Dropbox(token)

    result = dbx.files_list_folder(
        folder_path,
        recursive=recursive,
    )

    def handle_entries(entries):
        for entry in entries:
            if isinstance(entry, FolderMetadata):
                print(f"[DIR ] {entry.path_display}")
            elif isinstance(entry, FileMetadata):
                print(f"[FILE] {entry.path_display}")

    handle_entries(result.entries)

    while result.has_more:
        result = dbx.files_list_folder_continue(result.cursor)
        handle_entries(result.entries)
