### split_translator_output.py

Splits input file with translation blocks and creates dirs and files for each translation block next to the input file.

**Input example:**

`/NAME.txt`

```
LANG1
{ 
    ... 
}

LANG1
{ 
    ... 
}

LANG3
{ 
    ... 
}
```

**Output example:**

`/LANG1/NAME.json`

`/LANG2/NAME.json`

`/LANG3/NAME.json`

```
Usage: python split_translator_output.py </path/to/dir> <name>
```

### convert_txt_to_json.py

Recursively converts `.txt` translation files to `.json`

```
Usage: python convert_txt_to_json.py </path/to/dir> <lang>
```
