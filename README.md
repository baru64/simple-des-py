# simple-des-py
Simple DES implementation in Python

```
usage: des.py [-h] [-k KEY_HEX] [-f KEY_FILENAME] [--debug]

Simple DES implementation

optional arguments:
  -h, --help            show this help message and exit
  -k KEY_HEX, --key-hex KEY_HEX
                        Pass key in hex
  -f KEY_FILENAME, --key-filename KEY_FILENAME
                        Pass binary file with key
  --debug               Debug mode, output in binary text
```

## Example use
```
$ echo "Your lip" | python3 des.py --debug -k 0E329232EA6D0D73
1100000010011001100111111101110111100011011110001101011111101101
```
