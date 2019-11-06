import json

SERVER_NAME_START=13
SERVER_NAME_END=24
RADIS_PER_SERVER=40
STARTING_PORT=16000
INSTANCE_MEMORY=12

mydata={}
mydata['id']='cstore_east'

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
instance=0
for s in range(SERVER_NAME_START,SERVER_NAME_END+1):
    # uncomment if port number restart for each server
    port=STARTING_PORT
    for r in range(RADIS_PER_SERVER):
        shard={}
        shard['host']='dc6redis{}'.format(s)
        shard['port']=port
        instance_name='cstore_shard_{}'.format(instance)
        mydata[instance_name]=shard
        instance=instance+1
        port=port+1

with open('cstore.json', 'w') as json_file:
    json.dump(mydata,json_file)
