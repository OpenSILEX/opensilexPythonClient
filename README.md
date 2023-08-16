# Python client for Opensilex

Author : Gabriel Besombes  
Contact : gabriel.besombes@inrae.fr  
08/11/2022  

## Requirements

For this package to work you will need the following :

* Python 3.6+
* The opensilexClientToolsPython package version that corresponds with your Opensilex instance's version and must be equal or higher than version 1.0.0-rc+5 (for details on this package check [this github repository](https://github.com/OpenSILEX/opensilexClientToolsPython))
  
## Installation

Once your environnement fulfills the prerequisites, simply run the following command :

```sh
pip install git+https://github.com/OpenSILEX/opensilexClientPython@new_client_package
```

## Building localy

If you make any changes to this package you can re-build it localy and install it with this command from the root of the directory :

```sh
python3 -m build && python3 -m pip install .
```

## Usage

Examples can be found in the examples subdirectory
