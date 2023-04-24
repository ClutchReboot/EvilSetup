# EvilSetup
Demonstration showing malicious `setup.py`.
Inspiration comes from [wunderwuzzi23](https://github.com/wunderwuzzi23/this_is_fine_wuzzi/).

## Pre-requisites
```commandline
pip install setuptools
pip install build
```

## Build
Build the package. This will create a `.tar.gz` and `whl` in `dist/`.
```bash
python -m build
```


## Pypi Server (Optional)
A quick pypi server can be stood up to provide the file.

Note: If the wheel is availble for download, it will be used instead of the `.tar.gz`.
```bash
# Install
pip install pypiserver

# Setup and Run
mkdir packages && cp dist/EvilSetup-0.0.1.tar.gz packages/
pypi-server run -v -p 8000 ./packages
```

Download from the pypi server.
```bash
pip download EvilSetup --index-url http://localhost:8000 -v
````