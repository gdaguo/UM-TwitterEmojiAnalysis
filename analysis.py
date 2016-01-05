import os
import re

class Tweet:
	def __init__(self, user, tweet, country, charLength):
		self.user = user
		self.tweet = tweet
		self.country = country
		self.charLength = charLength
		self.emojiUnicode = -1
		self.emojiPersonalPositive = -1
		self.emojiPersonalNegative = -1
		self.emojiPersonalNeutral = -1
		self.emojiNonpersonal = -1
		self.emojiActivity = -1
		self.emojiAnimalsAndNature = -1
		self.emojiFlags = -1
		self.emojiFoodAndDrink = -1
		self.emojiObjects = -1
		self.emojiSmileyAndPeople = -1
		self.emojiSymbols = -1
		self.emojiTravelAndPlaces = -1
		
	def countEmoji(self, emojiList):
		self.emojiActivity = 0
		self.emojiAnimalsAndNature = 0
		self.emojiFlags = 0
		self.emojiFoodAndDrink = 0
		self.emojiObjects = 0
		self.emojiSmileyAndPeople = 0
		self.emojiSymbols = 0
		self.emojiTravelAndPlaces = 0
		self.emojiPersonalPositive = 0
		self.emojiPersonalNegative = 0
		self.emojiPersonalNeutral = 0
		for emoji in emojiList:
			if emoji.unicodeType == "Activity.md":
				self.emojiActivity += self.tweet.count(emoji.emoji)
			elif emoji.unicodeType == "Animals_and_Nature.md":
				self.emojiAnimalsAndNature += self.tweet.count(emoji.emoji)
			elif emoji.unicodeType == "Flags.md":
				self.emojiFlags += self.tweet.count(emoji.emoji)
			elif emoji.unicodeType == "Food_and_Drink.md":
				self.emojiFoodAndDrink += self.tweet.count(emoji.emoji)
			elif emoji.unicodeType == "Objects.md":
				self.emojiObjects += self.tweet.count(emoji.emoji)
			elif emoji.unicodeType == "Smileys_and_People.md":
				self.emojiSmileyAndPeople += self.tweet.count(emoji.emoji)
			elif emoji.unicodeType == "Symbols.md":
				self.emojiSymbols += self.tweet.count(emoji.emoji)
			elif emoji.unicodeType == "Travel_and_Places.md":
				self.emojiTravelAndPlaces += self.tweet.count(emoji.emoji)
			elif emoji.unicodeType == "Unicode_9.md":
				pass
			elif emoji.unicodeType == "people_positive.txt":
				self.emojiPersonalPositive += self.tweet.count(emoji.emoji)
			elif emoji.unicodeType == "people_neutral.txt":
				self.emojiPersonalNeutral += self.tweet.count(emoji.emoji)
			elif emoji.unicodeType == "people_negative.txt":
				self.emojiPersonalNegative += self.tweet.count(emoji.emoji)
			else:
				print("unicodeType:" + emoji.unicodeType)
				exit(1)

	def countEmojiPersonal(self, emojiList):
		self.emojiPersonalPositive = 0
		self.emojiPersonalNegative = 0
		self.emojiPersonalNeutral = 0
		for emoji in emojiList:
			if emoji.unicodeType == "people_positive.txt":
				self.emojiPersonalPositive += self.tweet.count(emoji.emoji)
			elif emoji.unicodeType == "people_neutral.txt":
				self.emojiPersonalNeutral += self.tweet.count(emoji.emoji)
			elif emoji.unicodeType == "people_negative.txt":
				self.emojiPersonalNegative += self.tweet.count(emoji.emoji)
			else:
				print("unicodeType:" + emoji.unicodeType)				
				exit(1)

	def write(self):
		print(self.user+ '\t' + self.country + '\t' + str(self.charLength) + '\t' +  str(self.emojiPersonalPositive) + '\t' + str(self.emojiPersonalNeutral) + '\t' + str(self.emojiPersonalNegative) + '\t' + str(self.emojiActivity) + '\t' + str(self.emojiAnimalsAndNature) + '\t' + str(self.emojiFlags) + '\t' + str(self.emojiFoodAndDrink) + '\t' + str(self.emojiObjects) + '\t' + str(self.emojiSmileyAndPeople) + '\t' + str(self.emojiSymbols) + '\t' + str(self.emojiTravelAndPlaces) )

	# percent of message that have emoticon per user.
	def stats(self, unicodeEmojiList):
		# user id, number of tweets, minimum number of tweets, 
		print(self.user+'\t' )
		print("number of tweets : " + str(len(self.tweets)))
		print("minimum number of tweets : " + str(len(min(self.tweets, key=len))))
		print("maximum number of tweets : " + str(len(max(self.tweets, key=len))))

	def unicodeStats(self, unicodeEmojiList):
		emojiCount = 0
		for unicodeEmoji in unicodeEmojiList:
			emojiCount += self.tweets.count(unicodeEmoji.emoji)		
		print(emojiCount)

class UnicodeEmoji:
	def __init__(self, emoji, descr, unicodeType):
		self.emoji = emoji
		self.descr = descr
		self.unicodeType = unicodeType

	def write(self):
		print(self.emoji + '\t' + self.unicodeType + '\t' + self.descr)

	def store(self, filename):
		pass	

def readTweets(directory, country):
	tweet_list = []
	for file in os.listdir(directory):
		infile = open(directory + "/" + file)
		corpus = infile.read()
		infile.close()
		pattern = r"<Text_Begin> (.*) <Text_End>"
		result = re.findall(pattern, corpus)
		for tweet in result:			
			charLength = len(tweet)
			tweet_list.append(Tweet(file, tweet, country, charLength))
	return tweet_list	

def readUnicode(directory):
	unicodeList = []
	for file in os.listdir(directory):
		infile = open(directory + "/" + file)
		for line in infile:
			line = line.rstrip("\n")
			line = line.lstrip(" ")
			lineList = line.split(' ', 1)
			unicodeList.append(UnicodeEmoji(lineList[0], lineList[1], file))
	return unicodeList

def countUnicode(unicodeEmojiList, tweetList):
	pass

def main():
	# directory names
	dirTop = os.getcwd()
	dirTweet = dirTop + "/Tweets"
	dirAnalysis = dirTop + "/Analysis"
	dirEmoji = dirTop + "/Emoji"

	# create a list of tweets
	#koreanTweetsList = readTweets(dirTweet + "/Korea", "Korea")
	#japanTweetsList = readTweets(dirTweet + "/Japan", "Japan")
	#usTweetsList = readTweets(dirTweet + "/US", "US")
	canadaTweetsList = readTweets(dirTweet + "/Canada", "Canada")

	unicodeEmojiList = readUnicode(dirEmoji + "/Unicode")	
	
	"""
	for koreanTweet in koreanTweetsList:
		koreanTweet.countEmoji(unicodeEmojiList)
		print(koreanTweet.write())
	"""	
	"""	
	for usTweet in usTweetsList:
		usTweet.countEmoji(unicodeEmojiList)
		print(usTweet.write())
	"""
	"""	
	for japanTweet in japanTweetsList:
		japanTweet.countEmoji(unicodeEmojiList)
		print(japanTweet.write())
	"""	

	for canadaTweet in canadaTweetsList:
		canadaTweet.countEmoji(unicodeEmojiList)
		print(canadaTweet.write())

main()
