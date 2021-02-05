""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run
import config

# login credentials
insta_username = config.username  # <- enter username here
insta_password = config.password  # <- enter password here

uname = "vayermaking"

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    """ Activity flow """
    # general settings
    '''
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "#store"])

    # activity
    session.like_by_tags(["natgeo"], amount=10)
'''
    session.follow_user_followers(uname, amount=100,
                          randomize=False, interact=False)
