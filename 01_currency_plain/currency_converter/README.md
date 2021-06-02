# README
This is version 0.0.1, the skeleton version just to prove that we can 
access POP and push data to kafka.

Once the base functionality is there, we will gradually implement all the features
needed.

## How to build as a module
Build a wheel file by calling. Please install wheel via pip package manager first

```
pip3 install wheel
```

Then build a so-called wheel file, which will be stored in the ./dist directory.
This needs to be exectued in the directory of this README.md file.

```
python3 setup.py bdist_wheel 
```

## How to install as module

If you want to install locally, be aware that you also need gcc installed.

You need to run things like
```
apt install gcc g++ unixodbc unixodbc-dev -y
pip install wheel
```

See also docker/Dockerfile

## Test
```
python3 -m pop_adapter -c docker/config_debug.json
```

Be aware this configuration only reads dummy data.  Once you see debug information
you can go for configuration. See also doc/config.md

## How to manually create a Docker file
docker build . -t monitoring.metan.io/PopAdapter


## Compatibility 
Works with at least Python 3.7 as we use dataclasses. Tested with Python 3.9.5