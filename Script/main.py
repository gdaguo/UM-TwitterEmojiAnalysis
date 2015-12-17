import os
import tweepy


def authenticate():


	CONSUMER_KEY = open("Authentication/Consumer_Key.txt").read().rstrip("\n")
	CONSUMER_SECRET = open("Authentication/Consumer_Secret.txt").read().rstrip("\n")

	ACCESS_TOKEN = open("Authentication/Access_Token.txt").read().rstrip("\n")
	ACCESS_TOKEN_SECRET = open("Authentication/Access_Token_Secret.txt").read().rstrip("\n")
	
	oauth_handler = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	oauth_handler.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	return oauth_handler	

def read_user_id_file_to_list(filename):
	infile = open(filename)
	user_id_list = []
	for user_id in infile:
		user_id_list.append(user_id.rstrip('\n'))		
	infile.close()
	return user_id_list

def main():
	script_directory = os.path.dirname(os.path.realpath(__file__))
	main_directory = os.path.split(current_directory)[0]
	authentication_directory = 	
	print(main_directory)

	

"""
	authentication = authenticate()
	api = tweepy.API(authentication, 
					 wait_on_rate_limit = True,
					 wait_on_rate_limit_notify = True)


	group_name_list = ["US", "Canada", "Japan", "Brazil", "Korea"]
	id_list = []	
	us_id_list = read_user_id_file_to_list("Screen_name/US_id.txt")
	canada_id_list = read_user_id_file_to_list("Screen_name/Canada_id.txt")
	japan_id_list = read_user_id_file_to_list("Screen_name/Japan_id.txt")
	brazil_id_list = read_user_id_file_to_list("Screen_name/Brazil_id.txt")
	korea_id_list = read_user_id_file_to_list("Screen_name/Korea_id.txt")

	
	print(os.getcwd())
	print(__file__)
"""
"""
	outfilename = "US_tweets.txt"

	outfile = open("~/Tweets/US/US_tweets.txt")
	outfile.write("hello")
	outfile.close()
"""
"""
	for user_id in us_id_list:

		for status in tweepy.Cursor(api.user_timeline, id=user_id).items():
			outstring = "<Text_Begin ID=" + user_id + ">" + status.text + "<Text_End>\n"
			outfile.write(outstring)
	outfile.close()
"""

		
main()

