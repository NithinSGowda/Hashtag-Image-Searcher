from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Dog']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'gCMpUH2ENFFIYqkDooZA6U3YM',
        consumer_secret = '7SdGDDuYtVp2WccLJh6gnA5X048DBHHhjhPAtbPJQnA2Mcwz5Q',
        access_token = '904541724214624257-5vv8K0dWsONBnkgE0jAiq994yHkdnwz',
        access_token_secret = 'LFHSXLXjPapDR7l3mKtoplTR3gp6MtC3QUZIsda90HErY'
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
