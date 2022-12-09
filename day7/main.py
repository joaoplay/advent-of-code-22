import sys


def calculate_directory_size(current_path, directory_content, sizer_per_directory):
    c_dir_size = 0
    for item_name, item_content in directory_content.items():
        if isinstance(item_content, dict):
            c_dir_size += calculate_directory_size(current_path + item_name + '/', item_content,
                                                 sizer_per_directory)
        else:
            c_dir_size += item_content

    sizer_per_directory[current_path] = directory_size

    return directory_size


def add_file(file, size, path, directories_map):
    current_path = directories_map
    for dir_or_file in path:
        current_path.setdefault(dir_or_file, {})
        current_path = current_path[dir_or_file]

    current_path[file] = size


def add_dir(directory, path, directories_map):
    current_path = directories_map
    for dir_or_file in path:
        current_path.setdefault(dir_or_file, {})
        current_path = current_path[dir_or_file]

    current_path[directory] = {}


if __name__ == '__main__':
    with open(f'data/challenge.txt') as f:
        lines = f.readlines()

        folder_map = {}

        directory_heap = []
        for line in lines:
            line = line.strip()

            if line[0] == "$":
                if line[2:4] == "cd":
                    if line[5:] == "/":
                        directory_heap = ['/']
                    elif line[5:] == "..":
                        directory_heap.pop()
                    else:
                        directory_heap.append(line[5:])
            else:
                if line[0:3] == "dir":
                    add_dir(line[4:], directory_heap, folder_map)
                else:
                    file_cmp = line.split(" ")
                    file_size = int(file_cmp[0])
                    file_name = file_cmp[1]
                    add_file(file_name, file_size, directory_heap, folder_map)

        directory_size = {}
        all_sizes = []
        result = 0
        for folder_name, folder_content in folder_map.items():
            calculate_directory_size(folder_name, folder_content, directory_size)

        for size in directory_size.values():
            if size < 100000:
                result += size

        space_used = directory_size['/']
        print("Space used: ", space_used)
        total_disk_space = 70000000
        required_space = 30000000

        available_space = total_disk_space - space_used
        print("Available space: ", available_space)

        best_delete_name = None
        best_new_available_space = sys.maxsize
        for dir_name, dir_size in directory_size.items():
            if available_space + dir_size >= required_space:
                new_available_space = available_space + dir_size
                if new_available_space < best_new_available_space:
                    best_new_available_space = new_available_space
                    best_delete_name = dir_name

        print("Best delete size: ", directory_size[best_delete_name])
