# upyflashed
A script to watch for new hex files from https://github.com/ntoll/upyed and flash the micro:bit immediately

`upyflashed` will poll your browser download directory for new hex files. If one is found it will copy it to the Micro:bit storage location.

**Note**: currently only tested on Linux (Ubuntu). The approach attempts to be cross platform but bug reports / fixes gratefully accepted.

## Installation

```bash
pip install git+git://github.com/tomviner/upyflashed.git
```

## Usage

```bash
$ upyflashed --help
usage: upyflashed [-h] [--download_path DOWNLOAD_PATH]
                  [--microbit_path MICROBIT_PATH] [-v]

A script to watch for new hex files from https://github.com/ntoll/upyed and
flash the micro:bit immediately

optional arguments:
  -h, --help            show this help message and exit
  --download_path DOWNLOAD_PATH
                        Filepath your browser stores downloads
  --microbit_path MICROBIT_PATH
                        Filepath your computer mounts the Micro:bit at
  -v, --verbose
```
