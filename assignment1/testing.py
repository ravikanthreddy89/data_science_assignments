import sys
import json

tweet_file=open(sys.argv[1])


hash_tags={}
count=0
for line in tweet_file:
	response=json.loads(line)
	if(response.has_key("entities")):
		if(response["entities"] is not None):
			if(response["entities"]["hashtags"] is not None and len(response["entities"]["hashtags"])>0 and response.has_key("lang") and response["lang"]=="en"):
				#print response["entities"]["hashtags"][0]["text"]
				hash_word=response["entities"]["hashtags"][0]["text"]
				if(hash_tags.has_key(hash_word)):
					hash_tags[hash_word]+=1
				else:
					hash_tags[hash_word]=1				


for item in hash_tags.keys():
	if(count==10):
		break
	print item," ",float(hash_tags[item])			
	count=count+1
