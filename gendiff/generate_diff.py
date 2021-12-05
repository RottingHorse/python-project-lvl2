from gendiff.parser import parse_file


def _check_diffs(all_keys, file1, file2):
    diffs = []
    for key in all_keys:
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                diffs.append((key, f'  {key}: {file1[key]}\n'))
            else:
                diffs.append((
                    key,
                    f'- {key}: {file1[key]}\n+ {key}: {file2[key]}\n',
                ))
        elif key in file1 and key not in file2:
            diffs.append((key, f'- {key}: {file1[key]}\n'))
        else:
            diffs.append((key, f'+ {key}: {file2[key]}\n'))
    diffs.sort()
    return diffs


def generate_diff(file_path1, file_path2):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)

    all_keys = set()

    for key in file1.keys():
        all_keys.add(key)
    for key in file2.keys():
        all_keys.add(key)

    diffs = _check_diffs(all_keys, file1, file2)

    return f"{{\n{''.join(string for _, string in diffs)}}}"
