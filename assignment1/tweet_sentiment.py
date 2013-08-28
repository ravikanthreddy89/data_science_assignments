import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
#    hw()
#    lines(sent_file)
#    lines(tweet_file)
    scores={}
    for line in sent_file:
	term , score= line.split("\t")
	scores[term]=int(score);
    for line in tweet_file:
	mood_score=0
	response=json.loads(line)
	if(response.has_key("text")):
		tweet_text= response["text"]
		tweet_words=tweet_text.split()
		for word in tweet_words:
			if(scores.has_key(word)):
				 mood_score=mood_score+scores[word]
		print float(mood_score)	

if __name__ == '__main__':
    main()
