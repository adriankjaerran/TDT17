from typing import Dict, List, Optional
import os


def get_files_in_directory(
    dir_path: str,
    start: Optional[str] = None,
    contains_any: Optional[List[str]] = None,
    contains_all: Optional[List[str]] = None,
    contains_none: Optional[List[str]] = None,
    end: Optional[str] = None,
):
    # Fix optional arguments
    start = start or ""
    end = end or ""
    contains_any = contains_any or []
    contains_all = contains_all or []
    contains_none = contains_none or []

    filenames = []

    for fp in os.listdir(dir_path):
        if (str(fp).startswith(start)):
            if str(fp).endswith(end):
                if all(map(fp.__contains__, contains_all)):
                    if not any(map(fp.__contains__, contains_none)):
                        if any(map(fp.__contains__,
                                   contains_any)) or len(contains_any) == 0:
                            filenames.append(fp)

    return filenames


def move_files_to_directory(
    from_path: str,
    to_path: str,
    move: Optional[bool] = False,
    verbose=True,
    start: Optional[str] = None,
    contains_any: Optional[List[str]] = None,
    contains_all: Optional[List[str]] = None,
    contains_none: Optional[List[str]] = None,
    end: Optional[str] = None,
):
    file_paths = get_files_in_directory(from_path, start, contains_any,
                                        contains_all, contains_none, end)

    for fp in file_paths:
        if verbose:
            print(fp)
        if move:
            os.rename(os.path.join(from_path, fp), os.path.join(to_path, fp))

    if not move:
        print(f"Found {len(file_paths)} files")
        print("To move files set move = True")
    else:
        print(f"Moved {len(file_paths)} files")


def remove_files_in_directory(
    dir_path: str,
    remove: bool = False,
    verbose=True,
    start: Optional[str] = None,
    contains_any: Optional[List[str]] = None,
    contains_all: Optional[List[str]] = None,
    contains_none: Optional[List[str]] = None,
    end: Optional[str] = None,
):

    file_paths = get_files_in_directory(dir_path, start, contains_any,
                                        contains_all, contains_none, end)

    for fp in file_paths:
        if verbose:
            print(fp)
        if remove:
            os.remove(os.path.join(dir_path, fp))

    if not remove:
        print(f"Found {len(file_paths)} files")
        print("To remove files set remove = True")
    else:
        print(f"Removed {len(file_paths)} files")


def rename_files_in_directory(
    dir_path: str,
    replace: Optional[Dict[str, str]],
    perform_replacement: False,
    start: Optional[str] = None,
    contains_any: Optional[List[str]] = None,
    contains_all: Optional[List[str]] = None,
    contains_none: Optional[List[str]] = None,
    end: Optional[str] = None,
):

    file_paths = get_files_in_directory(dir_path, start, contains_any,
                                        contains_all, contains_none, end)

    counter = 0
    for fp in file_paths:
        new_fp = fp
        for old_string, new_string in replace.items():
            new_fp = new_fp.replace(old_string, new_string)
        if new_fp != fp:
            if not perform_replacement:
                if os.path.exists(new_fp):
                    print(
                        f"ERROR PATH EXISTS: Will not replace {fp} -> {new_fp}"
                    )
                    continue
                print(f"Would replace: {fp}  ->  {new_fp}")
                counter += 1
            if perform_replacement:
                if os.path.exists(new_fp):
                    print(
                        f"ERROR PATH EXISTS: Could not replace {fp} -> {new_fp}"
                    )
                else:
                    counter += 1
                    os.replace(os.path.join(dir_path, fp),
                               os.path.join(dir_path, new_fp))
                    print(f"Raplced: {fp} -> {new_fp}")
    print(f"In total {counter} replacements")
