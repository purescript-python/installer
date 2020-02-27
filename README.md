## Installer for PureScript Python

### Prerequisites
You must install the following packages on your system prior to running the main installation steps  
- Python 3.x or greater - (https://www.python.org/downloads/)
- pip - (https://pypi.org/project/pip/)
- setuptools - (https://pypi.org/project/setuptools/) 

Alternatively, if you wish to use python virtual environments, the only packages needed are  
- Python 3.x or greater
- virtualenv - (https://virtualenv.pypa.io/en/latest/installation.html)

NOTE: `virtualenv` comes with `pip` and `setuptools` prepackaged.

### Main Installation steps

1. Install `nodejs`. `npm` should be bundled.
2. `npm install -g purescript` and `npm install -g spago`.
3. Use `pip` and install repo.

```
npm install -g purescript
npm install -g spago
pip install git+https://github.com/purescript-python/installer
```

NOTE: installing this package sometimes takes a long time, because we will download  the binary files and invoke 2 `setup.py install`.
