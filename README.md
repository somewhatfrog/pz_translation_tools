### split_translator_output

splits the file piled with translation blocks and creates dirs and files for each translation block next to the input file.

**Source example:**

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

<br>

### convert_txt_to_json

recursively converts `.txt` translation files to `.json`

```
Usage: python convert_txt_to_json.py </path/to/dir> <lang>
```
