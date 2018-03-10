import re
import robobrowser
import sys

MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"
FB_AUTH = "https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=fbconnect://success&scope=basic_info%2Cemail%2Cpublic_profile%2Cuser_about_me%2Cuser_activities%2Cuser_birthday%2Cuser_education_history%2Cuser_friends%2Cuser_interests%2Cuser_likes%2Cuser_location%2Cuser_photos%2Cuser_relationship_details&response_type=token&__mref=message"


def get_access_token(email, password):
    s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")
    s.open(FB_AUTH)

    ## submit login form
    f = s.get_form()
    f["pass"] = password
    f["email"] = email
    s.submit_form(f)

    ## click the 'ok' button on the dialog informing you that you have already authenticated with the Tinder app
    f = s.get_form()
    s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])

    ## get access token from the http response
    access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]
    return access_token


email = sys.argv[1]
password = sys.argv[2]
access_token = get_access_token(email, password)

print(access_token)
