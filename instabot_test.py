# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'tie_customs'  # <- enter username here
insta_password = 'm@rkos13'  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

#Create some cool comments
comments=[

    {'mandatory_words': ["customaf1", "customairforceones"], 'comments': ["Those AF1 look dope !", "Damn! What an outstanding pair of air force ones."]},

    {'mandatory_words': ["customkicks", "custom_kicks"], 'comments': ["Amazing kicks! They look so fresh. Keep up the good work!"]},

    {'mandatory_words': ["customsneakers", "custom_sneakers"], 'comments': ["Sneakers made by humans for gods! Great job mate!"]},

    {'mandatory_words': ["customkicks", "custom_kicks"], 'comments': ["I would kill for a pair of those!!!"]},
]


with smart_run(session):

    # quota supervisor
    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=57,
                              peak_likes_daily=585,
                               peak_comments_hourly=21,
                               peak_comments_daily=182,
                                peak_follows_hourly=48,
                                peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                  peak_server_calls_hourly=None,
                                  peak_server_calls_daily=4700)

    # skip users
    session.set_skip_users(skip_private=True,
                       private_percentage=100,
                       skip_no_profile_pic=False,
                       no_profile_pic_percentage=100)

    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=5000,
                                    min_followers=50,
                                    min_following=100,
                                    min_post=5)

    # activity settings
    session.set_do_like(enabled=True, percentage=75)
    session.set_do_comment(enabled=True, percentage=23)
    session.set_do_follow(enabled=True, percentage=11, times=2)
    session.set_dont_unfollow_active_users(enabled=True, posts=5)


    # activity
    session.like_by_tags(["customshoes","customaf1","customsneakers","#customkicks", "customnike", "customvans"], amount=10)
    session.set_comments(comments)




