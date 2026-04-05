import os
import shutil
from datetime import datetime, timedelta

# 🔸 Base directory to start search
BASE_PATH = r"D:\your\root\directory"   # <-- change this

# 🔸 Config
TARGET_FOLDER_NAME = "Transformers"
DAYS_OLD = 5

cutoff_time = datetime.now() - timedelta(days=DAYS_OLD)


def find_transformer_folders(base_path):
    transformer_paths = []
    for root, dirs, files in os.walk(base_path):
        for d in dirs:
            if d.lower() == TARGET_FOLDER_NAME.lower():
                transformer_paths.append(os.path.join(root, d))
    return transformer_paths


def get_old_subfolders(folder_path):
    subfolders = []

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isdir(item_path):
            modified_time = datetime.fromtimestamp(os.path.getmtime(item_path))

            if modified_time < cutoff_time:
                subfolders.append((item_path, modified_time))

    # 🔸 Sort HIGH → LOW (newest first)
    subfolders.sort(key=lambda x: x[1], reverse=True)

    return subfolders


def delete_folders(folders):
    for path, mtime in folders:
        try:
            shutil.rmtree(path)
            print(f"Deleted: {path} | Last Modified: {mtime}")
        except Exception as e:
            print(f"Error deleting {path}: {e}")


def main():
    transformer_dirs = find_transformer_folders(BASE_PATH)

    if not transformer_dirs:
        print("No 'Transformers' folders found.")
        return

    for t_dir in transformer_dirs:
        print(f"\nProcessing: {t_dir}")

        old_subfolders = get_old_subfolders(t_dir)

        if not old_subfolders:
            print("No subfolders older than 5 days.")
            continue

        print("\nFolders to delete (sorted newest → oldest):")
        for path, mtime in old_subfolders:
            print(f"{path} | {mtime}")

        # 🔴 DELETE (be careful)
        delete_folders(old_subfolders)


if __name__ == "__main__":
    main()