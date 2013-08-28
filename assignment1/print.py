import urllib
import json


raw_response=urllib.urlopen("http://search.twitter.com/search.json?q=NaMo");
response=json.load(raw_response);
print type(response);
print response.keys();
#print type(response["results"]);
#print type(response["results"][0]);
#print response["results"][0]["text"];
for item in response["results"]:
	print item["text"];
	print "\n";

