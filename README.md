hs-restaurant-reviews
=====================

This app is a restaurant review aggregator for people around a certain area, stemming from my desire to be able to easily see my friend's restaurant reviews and the idea that people who know the reviewers can absorb the information better based on what they know about the reviewer. Would be great for a friend group or a work area. 

This was my third web app and my first app where I started to integrate users and display data that could be searchable by different metrics. I also integrated some javascript and jquery to pull restaurant names from the Foursquare API and am now using this values to keep restaurant reviews under the same name and address. 

I used: Python 2.7.3, the Bottle Framework, and MongoDB. To use my tech, go to
    requirements.txt

####To start the app:
    python sign-up.py

The app has you sign up for an account or log in to an existing account (Hacker Schoolers can go directly to the log in page because I use their auth). From there you can:
* Add a restaurant review (and preview it before it is submitted) 
* Adjust user settings (change your user name and edit/delete reviews)
* View restaurant reviews (both overall and filtered by a restaurant)
* Logout

Users can opt to log in as "anonymous" which lets you view the site but prevents you from adding or editing tasks. Cookies are used to store your session and are removed upon logout. 

###The user screens look like the following:
####Main Screen After Signing In:

![Main](https://github.com/nehalita/hs-restaurant-reviews/blob/master/screenshots/main.png?raw=true)

####Add a Review:

![Add Review](https://github.com/nehalita/hs-restaurant-reviews/blob/master/screenshots/add-review.png?raw=true)

####Preview for adding review:

![Preview](https://github.com/nehalita/hs-restaurant-reviews/blob/master/screenshots/add-preview.png?raw=true)

####Settings Page:

![Settings](https://github.com/nehalita/hs-restaurant-reviews/blob/master/screenshots/settings.png?raw=true)

####Browse Reviews:

![Browse Reviews](https://github.com/nehalita/hs-restaurant-reviews/blob/master/screenshots/browse-restaurants.png?raw=true)

####Browse Reviews for a Specific Restaurant:

![Browse Restaurant](https://github.com/nehalita/hs-restaurant-reviews/blob/master/screenshots/view-res-reviews.png?raw=true)
