# consul event -http-addr=consul.service.nl.consul:8500 -name "run-chef"
# print(event['ID'])
# print(event['Node'])
# print(event['ServiceMeta']['event'])
# print(event['ServiceMeta']['status'])

from cProfile import label
import requests
import time
import sys

datacenter = "us-central1"
token = ""
pollingduration = 10
maxnodestoshow = 10

cmd = "consul event -http-addr=consul.service.{ds}.consul:8500 -name \"run-chef\""
url = "http://consul.service.{ds}.consul:8500/v1/catalog/service/consul-event-chef"

def GetEvents():
  ds_url = url.format(ds = datacenter)
  response = requests.get(ds_url)
  return (response.json())

def PrintResults(nodelist, sectionlabel):
  if len(nodelist) > 0:
    c = 1
    if len(nodelist) >= maxnodestoshow:
      print ("\n---- {label} [showing {max} out of {count} Nodes] ----".format(label = sectionlabel, max = maxnodestoshow, count = len(nodelist)))
    else:
      print ("\n---- {label} [{count} Nodes] ----".format(label = sectionlabel, count = len(nodelist)))

    for event in nodelist:
      print ("{0} {1}".format(event['ID'], event['Node']))
      if c >= maxnodestoshow:
        break
      c = c + 1

def EventUpdates():
  events = GetEvents()

  for event in events:
    # print (event['ID'])
    if event['ID'] == token or token == "":
      if event['ServiceMeta']['status'] == "error":
        errornodes.append(event)
      elif event['ServiceMeta']['status'] == "success":
        successnodes.append(event)
      else:
        inprogressnodes.append(event)

  PrintResults(successnodes, "Success")
  PrintResults(inprogressnodes, "In-Progress")
  PrintResults(errornodes, "Error")

# python3 consul_event_status.py [datacenter] [token]
n = len(sys.argv)
if n>1:
  datacenter = sys.argv[1]
if n>2:
  token = sys.argv[2]

# poll consul server for event status
count = 1
errornodes=[]
successnodes=[]
inprogressnodes=[]

try:
  while 1:
    EventUpdates()
    # if len(inprogressnodes) == 0 or count == pollingduration:
    if len(inprogressnodes) == 0:
      break
    print ("----- waiting ... {0} seconds-----\n".format(count))
    # sleep for 1 sec
    time.sleep(1)
    # clean lists
    count = count + 1
    errornodes.clear()
    successnodes.clear()
    inprogressnodes.clear()
except KeyboardInterrupt:
    pass

print(cmd.format(ds = datacenter))
