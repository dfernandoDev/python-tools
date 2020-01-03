# use python3 to maintain map insert order
# to run 'python3 create-cstore-json.py'

import json

# store details
CSTORE_LOCATION='cstore_west'
INSTANCE_NAME='cstore_shard_{}'

# server details
SERVER_NAME='sj4redis{}'
SERVER_NAME_START=5
SERVER_NAME_END=10

# redis details
RADIS_PER_SERVER=30
STARTING_PORT=16000
INSTANCE_MEMORY=12

cstore_data={}
cstore_data['id']=CSTORE_LOCATION

default={}
default['maxmemory']='{}gb'.format(INSTANCE_MEMORY)
default['data_dir']='/data/redis'
default['pid_dir']='/run/redis'
default['config_dir']='/usr/local/sifi/etc/redis'
default['bgsave_policy']='cstore'
default['appendonly']=False
default['no_appendfsync_on_rewrite']=False

cstore_data['defaults']=default


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
        cstore_data[instance_id]=shard
        instance_counter=instance_counter+1
        port_num=port_num+1

with open(CSTORE_LOCATION + '_temp.json', 'w') as json_file:
    json.dump(cstore_data,json_file, indent=2)
