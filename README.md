
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

#### To configure the Instant Client

#### In Windows 

* Create the oracle folder and extract the Instant Client.
* Create the network folder inside the Instant client folder.
* Create the admin folder inside the network folder (place the wallet information).
* The wallet can be found [here](https://drive.google.com/file/d/1Fze0mBvByvDIUAEWWIa2TeYak4uc2De6/view?usp=drive_link).

    ###### Set environment variables for the Instant Client

    * Add the directory to environment variables and user variables.

#### In Linux

* Create the /opt/oracle folder and extract the Instant Client.
* Create the network folder inside the Instant client folder.
* Create the admin folder inside the network folder (place the wallet information).
* The wallet can be found [here](https://drive.google.com/file/d/1Fze0mBvByvDIUAEWWIa2TeYak4uc2De6/view?usp=drive_link).

    ###### Set environment variables for the Instant Client

    * export LD_LIBRARY_PATH=/opt/oracle/instantclient_19_22:$LD_LIBRARY_PATH


#### Don't forget to make the changes in the config_vars.py file:

* BBDD_CONNECTION = "oracle+cx_oracle://claim:{password}@basededatosii_high/?encoding=UTF-8&nencoding=UTF-8"
    #### Linux
* d = "/opt/oracle/instantclient_19_22"  # version of Instant Client installed
    #### Windows 
* d = "C:\\oracle\\instantclient_19_22"  # version of Instant Client installed

#### For Oracle Databases Autonomous (instant client)
https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/connecting-python-tls.html
https://csiandal.medium.com/install-oracle-instant-client-on-ubuntu-4ffc8fdfda08

* pip install oracledb
