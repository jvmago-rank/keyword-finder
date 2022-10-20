from utils import preprocessing as pp
from utils import keyword_finder as kf
from utils import strategies as st
from utils import auto_match_language as aml
from google_play_scraper import app
#%%
longa = """Are you craving sushi, pizza, or a salad? Download DiDi Food now to enjoy our promotions and discount coupons: get up to 50% off on your delivery order!

DiDi is a professional food delivery platform that brings food from restaurants to your door. With more than 10 million orders delivered, we are experts to get you the food you want in minutes.

Have whatever you’re craving delivered in just one tap: pizza, burgers, tacos, burritos, sushi.

Order food from restaurants easily with DiDi! In just 3 simple steps, you can enjoy your favorite delivery without leaving your home:

1. Open the app and choose your delivery address
2. Choose your favorite restaurants and select dishes from their menu
3. Choose a payment method to submit the order, and your meal will be promptly delivered to your door by one of our couriers

Very hungry? View restaurants according to the fastest delivery times and get your food as soon as possible.

Very busy? Don't worry! We have a simple delivery ordering and with just a few clicks, you can order, pay and get your food delivered in minutes.

Want to know your order's location? Track your order's entire real-time progress from ordering, to preparation, to delivery. You can even view your courier's location on the map.

At DiDi Food we want you to have the best experience. In case you need help, our support team will be happy to help you 365 days a year.

Have your next meal delivered straight to your door. Enjoy your meal! Download the app now!"""
#%%
keywordfinder = kf.KeywordFinder(
                long_description=longa,
                strategy=st.Portuguese()
)
keywordfinder.stopwords
keywordfinder.get_head_tail()
keywordfinder.get_short_tail()
keywordfinder.get_long_tail()
#%%
keywordfinderenglish = kf.KeywordFinder(
                long_description=longa,
                strategy=st.English()
)
keywordfinderenglish.get_head_tail()
keywordfinderenglish.get_short_tail()
keywordfinderenglish.get_long_tail()
#%%
keywordfinderspanish = kf.KeywordFinder(
                long_description=longa,
                strategy=st.Spanish()
)
keywordfinderspanish.get_head_tail()
keywordfinderspanish.get_short_tail()
keywordfinderspanish.get_long_tail()
#%%