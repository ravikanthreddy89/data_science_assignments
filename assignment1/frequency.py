import sys
import json
#open the tweet file
tweet_file=open(sys.argv[1])

#initialize an empyt dictionary
words={}
word_count=0
#read the file and count the words and their occurences
for line in tweet_file:
	response=json.loads(line)
	if(response.has_key("text")):
		tweet_text=response["text"]
		tweet_words=tweet_text.split()
		for word in tweet_words:
			if(words.has_key(word)):
				 words[word]=words[word]+1
			else:
				 words[word]=1
		word_count=word_count+1

for item in words.keys():
	freq=(float(words[item])/word_count)
	print item," ",freq
	

