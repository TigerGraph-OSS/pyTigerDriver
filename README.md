
# pyTigerDriver 



## Installation

install with pip:

```shell script
pip install pyTigerDriver
```


## Usage


> **Architecture:** You can instatiate any **Interface [GSQL or REST]** in the **pyTigerDriver** seperately.


This flowchart illustrates the Classes:

```mermaid
graph LR
A[pyTigerDriver as tgCl] -- Gsql --> B((Gsql_Client))
A -- Rest --> C((Rest_Client))
B --> D{TigerGraph Database}
C --> D
```
### Sample Code :
```python

import pyTigerDriver as tg


tgCl = tg.Client(server_ip="127.0.0.1",username="tigergraph",password="tigergraph",version="3.0.5")

print("======================== SIMPLE RESTPP Queries ==================================")
print(tgCl.Rest.version())

print("============================== SIMPLE LS ===========================================")
res = tgCl.Gsql.query("ls")
print(res)

print("==============================   LIST USERS   ======================================")
res = tgCl.Gsql.query("SHOW USER")
print(res)

print("==============================   Create a Secret   ======================================")
res = tgCl.Gsql.query("USE GRAPH MyGraph") # change MyGraph --> to your graph
res = tgCl.Gsql.query("create secret  mys") # Create a secret
print(res)

print("==============================   Get Secrets   ======================================")
res = tgCl.Gsql.get_secrets("MyGraph")
print(res)

print("=============================== Print Version =========================================")
print(tgCl.Gsql.version())


```
# Code Linting And Unit Testing

## Code Linting :

Linting using PEP8 Standards

```Shell

user@box:~$ flake8 --exclude=venv* --ignore=E501 --statistics pyTigerGraphBeta/pyTigerGraphBeta.py

```

## Running the tests : 

run unit tests using pytest :

```Shell

user@box:~$ pytest -v

```
## CircleCi Work flow :

1. create a folder named .circleci in the root of the repo
2. within that folder create a file called **config.yml**  containing the folloing flow :

```yaml
version: 2.1

orbs:
  python: circleci/python@0.2.1


jobs:
  build-and-test:
    executor: python/default
    steps:
      # Step 1: obtain repo from GitHub
      - checkout
      # Step 2: create virtual env and install dependencies
      - run:
          name: install dependencies
          command: |
            python3 -m venv venv
            . venv/bin/activate
            pip install -r requirements.txt
      # Step 3: run linter and tests
      - run:
          name: run tests
          command: |
            . venv/bin/activate
            flake8 --exclude=venv* --ignore=E501  --statistics pyTigerDriver/pyDriver.py
            flake8 --exclude=venv* --ignore=E501  --statistics pyTigerDriver/restDriver.py
            pytest -v


workflows:
  main:
    jobs:
      - build-and-test

```
