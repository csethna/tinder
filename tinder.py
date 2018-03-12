from credentials import *
import pynder

session = pynder.Session(facebook_id=FACEBOOK_ID, facebook_token=FACEBOOK_AUTH_TOKEN) #kwargs
# session.matches() # get users you have already been matched with
#session.update_location(LAT="39.011357", LON="-77.056249") # updates latitude and longitude for your profile
# session.profile  # your profile. If you update its attributes they will be updated on Tinder.
users = session.nearby_users() # returns a iterable of users nearby
matches = session.matches()

for user in users:
    print(user, end=',')
