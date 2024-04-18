# waldl

## Overview
`waldl` is a Python script for downloading wallpapers from Wallhaven (https://wallhaven.cc/). It uses Wallhaven's API to search for wallpapers based on specified queries and downloads them to a specified directory.

## Usage
To download wallpapers:
```python waldl.py "<search_query>"```

To download random wallpapers:
```python waldl.py --random/-r```

To download wallpapers from the top list:
```python waldl.py --top/-t```

## Configuration

- [DOWNLOAD_DIR](https://github.com/ayxkaddd/waldl/blob/main/waldl.py#L17): Default directory for downloading wallpapers. Modify this variable in the script to change the download directory.