import os
import re
import sys

def finalize(result: list) -> str:
    # Strip trailing comma from the last key-value line
    for i in range(len(result) - 1, -1, -1):
        if result[i].strip().startswith('"'):
            result[i] = result[i].rstrip(",")
            break
    result.append("}")
    return "\n".join(result) + "\n"

def lua_to_json(content: str) -> str:
    lines = content.splitlines()
    result = ["{"]

    for line in lines:
        if re.match(r'^\s*\w+\s*=\s*\{', line) and '\"' not in line and "'" not in line:
            continue
        if re.match(r'^\s*\}\s*$', line):
            continue
        if not line.strip():
            continue

        m = re.match(r'^(\s*)(\w+)\s*=\s*(".*?"),?\s*$', line)
        if m:
            indent, key, value = m.group(1), m.group(2), m.group(3)
            value = value.replace("<br>", "\\n")
            result.append(f'    "{key}": {value},')
        else:
            result.append(line)

    return finalize(result)

def item_name_to_json(content: str) -> str:
    lines = content.splitlines()
    result = ["{"]

    for line in lines:
        if re.match(r'^\s*\w+\s*=\s*\{', line) and '\"' not in line and "'" not in line:
            continue
        if re.match(r'^\s*\}\s*$', line):
            continue
        if not line.strip():
            continue

        m = re.match(r'^(\s*)\w+_(\w+\.\w+)\s*=\s*(".*?"),?\s*$', line)
        if m:
            indent, key, value = m.group(1), m.group(2), m.group(3)
            value = value.replace("<br>", "\\n")
            result.append(f'    "{key}": {value},')
        else:
            result.append(line)

    return finalize(result)

def process(path: str, search_string: str):
    if not os.path.isdir(path):
        print(f"Error: '{path}' is not a valid directory.")
        sys.exit(1)

    matched = [
        os.path.join(root, f)
        for root, _, files in os.walk(path)
        for f in files
        if f.endswith(".txt") and search_string in f
    ]

    if not matched:
        print(f"No .txt files containing '{search_string}' found in '{path}'.")
        return

    for txt_path in matched:
        filename = os.path.basename(txt_path)
        dir_path = os.path.dirname(txt_path)

        with open(txt_path, "r", encoding="utf-8") as f:
            content = f.read()

        if "ItemName" in filename:
            json_content = item_name_to_json(content)
        else:
            json_content = lua_to_json(content)

        base = filename[:-4]  # remove .txt
        new_base = re.sub(r'_?' + re.escape(search_string) + r'_?', '', base)
        new_base = new_base.strip('_')
        json_filename = new_base + ".json"
        json_path = os.path.join(dir_path, json_filename)

        with open(json_path, "w", encoding="utf-8") as f:
            f.write(json_content)

        print(f"Converted: {txt_path} -> {json_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_txt_to_json.py <path> <lang>")
        sys.exit(1)

    process(sys.argv[1], sys.argv[2])
