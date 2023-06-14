## CSV To Mongo Data Import
This script lets you import your CSV data into mongodb collection. The process happens in a batch process and the number of records to process in a single batch can be configured as well.

### Pre-Requisites
* Python3
* Pip3

### Packages Required
* pymongo

### Install All the Requirements
All the required packages are listed in *requirements.txt* file. To install the required packages, use the following command.
```
pip3 install -r requirements.txt
```

### Configure Host, Port and Other Variables

Navigate to the file *csvToMongo.py* and change the variables as needed.

### Configure Batch Size
Navigate to the file *csvToMongo.py* and change the variable *batch_size* accordingly. Default is 100.
> batch_size = 100


### Running the Script
Use the command below to start the import process. The script should show you the number of record being processed. After all records are imported, the script will terminate.
```
python3 csvToMongo.py
```

## Tools Used
* Python