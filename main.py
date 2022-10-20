from utils import preprocessing as pp
from utils import keyword_finder as kf
from utils import strategies as st
from google_play_scraper import app
#%%
longa = """¡Let your dollar travel further with DiDi’s everyday low fares and offers. Download DiDi Rider now to unlock discounts!



DiDi is an industry-leading ridesharing platform that offers safe and fast rides. We are available in 28 cities across Australia and New Zealand and 17+ countries, connecting over 600 million riders across Africa, Asia, Latin America & Russia.

DiDi Rider Services

Express:
Quick and affordable rides, up to 2 people. Easy & affordable.

Max:
Spacious and affordable rides for groups up to 6 or extra luggage.

Rideshare:
Match with another traveler in the same direction and split the cost. Up to 40% cheaper than DiDi Express rides.

Delivery:
Affordable, on-demand city-wide delivery. Low delivery fares starting from $6.30 for 24/7 on-demand delivery.


Whether you’re heading out with friends or need a ride from the airport, DiDi can get you there safely, at a fraction of the cost. Request a ride with DiDi Rider!

Let your dollar travel further with our everyday low fares and exceptional service. Head to the app to enjoy affordable rides by riding with DiDi.

Why choose DiDi Rider?

Low Fares Every Day

At DiDi we believe that ridesharing should be an affordable experience for everyone. That’s why we charge less for our service than competing ridesharing services. DiDi fares are consistently lower than other ride-hailing and taxi services, which means you get to save more money to spend on the activities you love.

Request a ride to enjoy affordable rides by riding with DiDi.

Fast & Reliable

We’ve got over 130,000 drivers at your fingertips across Australia & New Zealand, which means you can find a ride fast.

Easily connect to a driver via the DiDi Rider app in seconds, and you’ll have a car at your location in minutes! Request a ride now!

Safety First

Get added peace of mind while you're riding. We’re committed to helping make every ride with DiDi as safe as possible.

All our drivers have undergone extensive background checks, facial verification, vehicle inspections, ongoing monitoring & more. We offer world-leading in-app safety features such as trip check-ins, phone number, and home address anonymization, sharing your trip with trusted contacts, and more.

Award Winning Rideshare

Aussies have rated DiDi the best ridesharing service in Canstar Blue’s 2020 review, giving it five stars over 8 categories, including reliability, customer service, cleanliness, value for money, and more!

Driver Friendly

Our drivers get to keep more of your fare compared to competing for ride-hailing services, which means that by using DiDi you also support the livelihood of local drivers. It’s a win-win choice for both you and your driver.


Questions about DiDi Rider Australia or need help with our ridesharing platform? Access to: https://australia.didiglobal.com/rider/help/ or email us help.rider@au.didiglobal.com

Request a ride to enjoy affordable rides. Download DiDi Rider now!"""
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