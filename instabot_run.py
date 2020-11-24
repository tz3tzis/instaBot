# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
from instapy import get_workspace
import time
import config
import schedule


insta_username = config.username  # <- enter username here
insta_password = config.password  # <- enter password here

set_workspace(path="/Users/tz3m/Desktop/instagram")

session = InstaPy(username=insta_username, password=insta_password,headless_browser=False)

comments=[

      {'mandatory_words': ["#customaf1", "#customairforceones"], 'comments': ["Those AF1 look dope !", "Damn! What an outstanding pair of air force ones."]},

      {'mandatory_words': ["#customkicks", "#custom_kicks"], 'comments': ["Amazing kicks! They look so fresh. Keep up the good work!"]},

      {'mandatory_words': ["#customsneakers", "#custom_sneakers"], 'comments': ["Sneakers made by humans for gods! Great job mate!"]},

      {'mandatory_words': ["#customkicks", "#custom_kicks"], 'comments': ["I would kill for a pair of those!!!"]},
]



def unfollow():
  print("i am in");
  
  with smart_run(session):

    session.unfollow_users(
      amount=99, 
      instapy_followed_enabled=True, 
      instapy_followed_param="nonfollowers",
      style="FIFO",
      unfollow_after=12 * 60 * 60, 
      sleep_delay=60)


def hustle_strategy():

  with smart_run(session):

    session.set_quota_supervisor(
        enabled=True, 
        sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], 
        sleepyhead=True, 
        stochastic_flow=True, 
        notify_me=True,
        peak_likes_hourly=100,
        peak_likes_daily=789,
        peak_comments_hourly=30,
        peak_comments_daily=182,
        peak_follows_hourly=48,
        peak_follows_daily=30,
        peak_unfollows_hourly=35,
        peak_unfollows_daily=402,
        peak_server_calls_hourly=None,
        peak_server_calls_daily=4700)

    session.set_skip_users(
        skip_private=True,
        private_percentage=100,
        skip_no_profile_pic=False,
        no_profile_pic_percentage=100)

     
    session.set_relationship_bounds(
        enabled=True,
        delimit_by_numbers=True,
        max_followers=12000,
        min_followers=500,
        min_following=100,
        min_posts=3)

    # activity settings
    session.set_do_like(enabled=True, percentage=93)
    session.set_comments(comments)
    session.set_do_comment(enabled=True, percentage=25)
    session.set_do_follow(enabled=True, percentage=41, times=2)
 
    session.like_by_tags(
      ["customshoes","customaf1","customsneakers","#customkicks", "customnike", "customvans"], 
        amount=50)

#=======================================================================================================================================#
  
schedule.every().day.at("10:53").do(hustle_strategy)
schedule.every().day.at("18:31").do(hustle_strategy)
schedule.every().day.at("20:38").do(hustle_strategy)
schedule.every().day.at("21:56").do(unfollow)
schedule.every().day.at("00:38").do(hustle_strategy)
schedule.every().wednesday.at("22:01").do(unfollow)


while True: 
  schedule.run_pending()
  time.sleep(10)
  print("BOT IS SLEEPING PLEASE BE QUIET") 

