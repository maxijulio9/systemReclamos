#### Bases de Datos II - dao-RECLAMOS


Data Access Objects for Claims to the goverment

#### Before you begin, you’ll need:
* IDE or Text editor 
* Python 3.6 or 3.7
* pip install --upgrade pip

#### Create database schema
* [dbscripts](dbscripts.sql)

#### Create the virtual environment(Linux)
* python3 -m venv ./venv

#### Activate the virtual environment
* source ./venv/bin/activate

#### Install jupyter
* pip install notebook 

#### Install Libs
* pip install sqlalchemy==1.4

#### For Oracle Databases
* pip install cx_Oracle==8.3

#### For Oracle Databases Autonomous (instant client)
https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/connecting-python-tls.html
https://csiandal.medium.com/install-oracle-instant-client-on-ubuntu-4ffc8fdfda08

* pip install oracledb
