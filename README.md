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

Example output:
```bash
$ sudo pip download EvilSetup --index-url http://localhost:8000 -v
Looking in indexes: http://localhost:8000
Collecting EvilSetup
  Downloading http://localhost:8000/packages/EvilSetup-0.0.1.tar.gz (1.4 kB)
  Running command python setup.py egg_info
  running egg_info
  ### Evil Things.
  creating /tmp/pip-pip-egg-info-mx0ezypt/EvilSetup.egg-info
  writing /tmp/pip-pip-egg-info-mx0ezypt/EvilSetup.egg-info/PKG-INFO
  writing dependency_links to /tmp/pip-pip-egg-info-mx0ezypt/EvilSetup.egg-info/dependency_links.txt
  writing top-level names to /tmp/pip-pip-egg-info-mx0ezypt/EvilSetup.egg-info/top_level.txt
  writing manifest file '/tmp/pip-pip-egg-info-mx0ezypt/EvilSetup.egg-info/SOURCES.txt'
  reading manifest file '/tmp/pip-pip-egg-info-mx0ezypt/EvilSetup.egg-info/SOURCES.txt'
  writing manifest file '/tmp/pip-pip-egg-info-mx0ezypt/EvilSetup.egg-info/SOURCES.txt'
  Preparing metadata (setup.py) ... done
Saved ./EvilSetup-0.0.1.tar.gz
Successfully downloaded EvilSetup
```