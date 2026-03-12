import os
import re
import sys

if len(sys.argv) < 3:
    print("Usage: python split_translator_output.py <path> <lang>")
    sys.exit(1)

input_dir = sys.argv[1]
output_name = sys.argv[2]

pattern = r'([A-Z]+)\s*\{.*?\}'

for root, _, files in os.walk(input_dir):
    for file in files:
        if not file.endswith(".txt"):
            continue

        path = os.path.join(root, file)

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        for match in re.finditer(pattern, content, re.DOTALL):
            lang = match.group(1)
            block_text = match.group(0)

            json_content = block_text[len(lang) + 1:].strip()

            output_dir = os.path.join(root, lang)
            os.makedirs(output_dir, exist_ok=True)

            output_file = os.path.join(output_dir, f"{output_name}.json")

            with open(output_file, "w", encoding="utf-8") as out:
                out.write(json_content)

            print(f"Created {output_file}")

print("Done")
