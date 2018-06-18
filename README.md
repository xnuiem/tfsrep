# VSTS Reports
A static way to query VSTS for a current status update.  It does not, currently, store any kind of history.  Only returns the current status.

Written with Python 3.6

# Table of Contents
* [Installation](#installation)
* [Quick Start](#quick-start)
* [Configuration Options](#configuration-options)
* [Credits](#credits)

# Usage
## <a name="installation"></a>Installation
Install the modules
```text
 pip install -r requirements.txt
```

## <a name="quick-start"></a>Quick Start
```text
python main.py
```

## <a name="configuration-optinos"></a>Configuration Options
### Environment Variables
Defaults are (<strong>bold</strong>)

#### API_HOST*
Host for VSTS in URL Format (<strong>None</strong>)

#### API_KEY*
Your API Key (<strong>None</strong>)

#### API_COLLECTION
Collection (<strong>DefaultCollection</strong>)

#### API_PROJECT
Project Name (<strong>None</strong>)

#### CASSANDRA_NODES*
A list of Cassndra nodes by IP (<strong>None</strong>)
Example: "10.10.0.1, 10.10.0.2" 

#### CASSANDRA_KEYSPACE*
The name of the Cassandra keyspace (<strong>tfsrep</strong>)


## <a name="credits"></a>Credits
- Ryan C Meinzer