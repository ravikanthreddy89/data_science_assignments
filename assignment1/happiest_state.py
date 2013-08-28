import sys
import json

tweet_file=open(sys.argv[2])
sent_file=open(sys.argv[1])

scores={}
for line in sent_file:
	term, score= line.split("\t")
	scores[term]=int(score)



states={}
count=0
for line in tweet_file:
	mood_score=0
	response=json.loads(line)
	if(response.has_key("place") and (response["place"] is not None) and (response["place"]["country"]=="United States")):
		#count=count+1
		#print response["place"].keys()
		#print response["place"]["country"] 	
		if(response["text"] is not None):
			tweet_words=line.split()
			for word in tweet_words:
				if(scores.has_key(word)):
					mood_score=mood_score+scores[word]
			if(states.has_key(response["place"]["full_name"].split(",")[1].strip())):
					states[response["place"]["full_name"].split(",")[1].strip()]+=mood_score
			else:
				states[response["place"]["full_name"].split(",")[1].strip()]=mood_score
max_state=""
states[max_state]=0
for item in states.keys():
	if(states[item]>states[max_state]):
		max_state=item

print max_state
