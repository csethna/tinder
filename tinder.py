from credentials import *
import pynder

# session = pynder.Session(facebook_id=FACEBOOK_ID, facebook_token=FACEBOOK_AUTH_TOKEN) #kwargs
# session.matches() # get users you have already been matched with
# #session.update_location(LAT="39.011357", LON="-77.056249") # updates latitude and longitude for your profile
# session.profile  # your profile. If you update its attributes they will be updated on Tinder.
# users = session.nearby_users() # returns a iterable of users nearby
#
# print(",".join([x.photos for x in users]))

session = pynder.Session(facebook_id=FACEBOOK_ID, facebook_token=FACEBOOK_AUTH_TOKEN)
friends = session.get_fb_friends()

# Print the names of all facebook friends using Tinder Social.
print(", ".join([x.name for x in friends]))

# # Get the user_info of these facebook friends.
# user_info_objects = []
# for friend in friends:
#     user_info_objects.append(friend.get_tinder_information())
#
# # Print the bios.
# for user_info, friend in zip(user_info_objects, friends):
#     print("=" * 50)
#     # Use Friend.name, as user_info.name only contains first name.
#     print(friend.name)
#     print(friend.facebook_link)
#     print("-" * 50)
#     print(user_info.bio)
#     print("=" * 50)
