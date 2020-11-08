# imports
from instapy import InstaPy
from instapy import smart_run
import schedule


# starting_times = [  "00:00", "00:30",
#                     "01:00", "01:30", 
#                     "02:00", "02:30", 
#                     "03:00", "03:30", 
#                     "04:00", "04:30", 
#                     "05:00", "05:30", 
#                     "06:00", "06:30", 
#                     "07:00", "07:30", 
#                     "08:00", "08:30", 
#                     "09:00", "09:30",
#                     "10:00", "10:30", 
#                     "11:00", "11:30", 
#                     "12:00", "12:30", 
#                     "13:00", "13:30", 
#                     "14:00", "14:30"]

# def hustle_strategy():
  # login credentials
insta_username = 'tie_customs'  # <- enter username here
insta_password = 'm@rkos14'  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(
    username=insta_username,
    password=insta_password,
    headless_browser=False)

  #Create some cool comments
comments=[

      {'mandatory_words': ["#customaf1", "#customairforceones"], 'comments': ["Those AF1 look dope !", "Damn! What an outstanding pair of air force ones."]},

      {'mandatory_words': ["#customkicks", "#custom_kicks"], 'comments': ["Amazing kicks! They look so fresh. Keep up the good work!"]},

      {'mandatory_words': ["#customsneakers", "#custom_sneakers"], 'comments': ["Sneakers made by humans for gods! Great job mate!"]},

      {'mandatory_words': ["#customkicks", "#custom_kicks"], 'comments': ["I would kill for a pair of those!!!"]},
]


with smart_run(session):

      # quota supervisor
      session.set_quota_supervisor(
        enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
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

      # skip users
      session.set_skip_users(
        skip_private=True,
        private_percentage=100,
        skip_no_profile_pic=False,
        no_profile_pic_percentage=100)

      # general settings
      session.set_relationship_bounds(
        enabled=True,
        delimit_by_numbers=True,
        max_followers=5000,
        min_followers=500,
        min_following=100,
        min_posts=5)

      # activity settings
      session.set_do_like(enabled=True, percentage=93)
      session.set_comments(comments)
      session.set_do_comment(enabled=True, percentage=25)
      session.set_do_follow(
        enabled=True, 
        percentage=41, 
        times=2)
      session.set_dont_unfollow_active_users(
        enabled=True, 
        posts=5)
      # session.unfollow_users(
      #   amount=500, 
      #   instapy_followed_enabled=True, 
      #   instapy_followed_param="nonfollowers",
      #   style="FIFO",
      #   unfollow_after=12 * 60 * 60, sleep_delay=601)
      
      # activity
      # session.like_by_feed(
      #   amount=500, 
      #   randomize=false)
      session.like_by_tags(
        ["customshoes","customaf1","customsneakers","#customkicks", "customnike", "customvans"], 
        amount=50)

      session.end()
  #=======================================================================================================================================#
  
  # schedule.every().hour.do(hustle_strategy)
  # schedule.every().day.at("01:09").do(hustle_strategy)

  # schedule.run_pending()
  # print("RUNNED PENDING")



