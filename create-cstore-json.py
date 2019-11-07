# use python3 to maintain map insert order
# to run python3 create-cstore-json.py


import json
import pprint

# store details
CSTORE_LOCATION='cstore_east'
INSTANCE_NAME='cstore_shard_{}'

# server details
SERVER_NAME='dc6redis{}'
SERVER_NAME_START=13
SERVER_NAME_END=24

# redis details
RADIS_PER_SERVER=40
STARTING_PORT=16000
INSTANCE_MEMORY=12

mydata={}
mydata['id']=CSTORE_LOCATION

default={}
default['maxmemory']='{}gb'.format(INSTANCE_MEMORY)
default['data_dir']='/data/redis'
default['pid_dir']='/run/redis'
default['config_dir']='/usr/local/sifi/etc/redis'
default['bgsave_policy']='cstore'
default['appendonly']=False
default['no_appendfsync_on_rewrite']=False

mydata['defaults']=default


# uncomment if port number continues
# port=STARTING_PORT
instance_counter=0
for s in range(SERVER_NAME_START,SERVER_NAME_END+1):
    # uncomment if port number restart for each server
    port_num=STARTING_PORT
    for r in range(RADIS_PER_SERVER):
        shard={}
        shard['host']=SERVER_NAME.format(s)
        shard['port']=port_num
        instance_id=INSTANCE_NAME.format(instance_counter)
        mydata[instance_id]=shard
        instance_counter=instance_counter+1
        port_num=port_num+1

with open(CSTORE_LOCATION + '_temp.json', 'w') as json_file:
    #json.dump(mydata,json_file, indent=2, sort_keys=True)
    json.dump(mydata,json_file, indent=2)
    #json.dump(mydata,json_file)
