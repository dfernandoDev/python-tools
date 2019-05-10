import json
import re

# read json output from
# https://github.com/simplifi/rebeu/blob/master/datadog/scripts/sifi_datadog_search.py
with open('monitors.json', 'r') as fp:
    jsondata = json.load(fp)

# export to match data to file
with open('matched.csv', 'w') as f:
	for m in jsondata:
		name = m["name"]
		creator=m["creator"]["name"]
		query = m["query"]
		url = "https://app.datadoghq.com/monitors/" + str(m["id"])

		# extract the text within the 'exclude' parentheses
		match=re.findall(r"\.exclude\((.*?\)).",query)
		if match:
			f.write(name + str(",") + url + "," + creator + ",\"" + str(match).replace("\"","\"\"") + str("\"\n"))
