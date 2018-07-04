# chaoshub-tck

Technology Compatibility Kit (TCK) for [Chaos Hub][chaoshub] client and servers implementations.

## Purpose

The purpose of this project is to provide a technology compatibility kit for client and server developers of [Chaos Hub][chaoshub] systems. The commercial [Chaos Hub][chaoshub] uses and maintains this TCK to ensure that it's API remains open and compatible with all other client and server implementations.

[chaoshub]: http://chaoshub.com

## Features

The project contains [Chaos Hub][chaoshub] server and client TCKs that aim to faciliate and accelerate the development of both Chaos Hub server and client compatible implementations.

## Usage

### For Chaos Hub Server developers

There are two features in this project that support the development of compatible Chaos Hub servers:

* [An Open API specification](chaoshubtck/chaoshubserver/chaoshubserver.yaml) that describes the API that your Chaos Hub server must support.
* A set of example interactions and scenarios that you can use to test the behaviour of your Chaos Hub server

#### Chaos Hub Server API Specification

This project contains a sample [Open API (Swagger) specification][spec] for the interface that should be supported by a compatible Chaos Hub server implementation. Your starting point for developing your own Chaos Hub compatible server should be [this specification][spec]).

[spec]: chaoshubtck/chaoshubserver/chaoshubserver.yaml

The easiest way to begin your Chaos Hub server (and client) side development is to take the Chaos Hub Open API 2 specification and use the free [Swagger Codegen tool][codegen].

#### Interaction and Scenario Tests

Also included is a growing set of example interactions and scenarios that work against your server implementation to ensure its behaviour matches what is expected beyond the simple Open API 2 specification.

You can execute these scenarios by changing the [usageTests.sh](usageTests.sh) file to point at your own server's URL and then executing the `usageTests.sh` script.

### For Chaos Hub Client developers

There are two features in this project that support the development of compatible clients for the Chaos Hub:

* [An Open API specification][spec] that can be used to generate client-side code.
* A [sample server][server] that can be executed to test your client-side code against.

[server]: /servertck.py

#### Generating Client-side code from the Open API 2 specification

The easiest way to begin your Chaos Hub client (and server) side development is to take the Chaos Hub Open API 2 specification and use the free [Swagger Codegen tool][codegen] to generate client stubs for your chosen language and frameworks.

[codegen]: https://swagger.io/tools/swagger-codegen/

#### Using the Sample Chaos Hub Server

The sample Chaos Hub server is built using the `connexion` Python library. You will need to set up this project for development in order to use the server by executing the following command.

```console
$ python setup.py develop
```

Once you have set up the project the sample Chaos Hub server can be executed using the following command from the root directory of this project:

```console
$ python servertck.py
```

The sample Chaos Hub server takes advantage of connexion's support for an in-built Swagger UI that you can use to explore the [Chaos Hub's Open API specification][spec]. Once the server is running you can access this UI by opening `http://localhost:8080/ui` in your browser. 

## Contribute

Contributors to this project are welcome as this is an open-source effort that
seeks [discussions][join] and continuous improvement.

[join]: https://join.chaostoolkit.org/

From a code perspective, if you wish to contribute, you will need to run a 
Python 3.5+ environment. Then, fork this repository and submit a PR. The
project cares for code readability and checks the code style to match best
practices defined in [PEP8][pep8]. Please also make sure you provide tests
whenever you submit a PR so we keep the code reliable.

[pep8]: https://pycodestyle.readthedocs.io/en/latest/

### Develop

If you wish to develop on this project, make sure to install the development
dependencies. But first, [create a virtual environment][venv] and then install
those dependencies.

[venv]: http://chaostoolkit.org/reference/usage/install/#create-a-virtual-environment

```console
$ pip install -r requirements-dev.txt -r requirements.txt 
```

Then, point your environment to this directory:

```console
$ python setup.py develop
```

### Test

To run the tests for the project execute the following:

```
$ pytest
```