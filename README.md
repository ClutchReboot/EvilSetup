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

```bash
# Install
pip install pypiserver

# Run
pypi-server run -v -p 8080 ./packages
```

Download from the pypi server.
```bash
pip download EvilSetup --index-url http://localhost:8080 -v
````