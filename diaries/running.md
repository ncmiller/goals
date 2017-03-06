## Sunday, March 5. 2017

A perfect week. I ran all 6 days (18.4 miles total), set a new PR (sub-23), and hit all my
upper-body workouts. Let's do it again.

## Sunday, February 26, 2017

Okay, this was a pretty bad week, only 8.6 miles. My legs were sore from last Sunday until
Thursday, which prevented me from running. I've decided it's probably a good
idea to remove strength training for my legs, since they get enough of
a workout by running. I was extra sore since it was the first leg
workout in a while, but to reach my sub-20 goal, I need to prioritize running.
I want my legs to be as fresh as possible. I'll still continue to do
upper-body workout 3x a week.

I absolutely love the new bluetooth headphones I purchased. Total game
changer. Sure the sound quality may not be as good as wired, and there are
occasional hiccups in the playback, but not having that wire makes things so
much easier. I created a running playlist, mostly with electronic and techno
music. It's doing its job - it really pumps me up. In particular, [The
Heat](https://www.youtube.com/watch?v=EZgLXq0hIVs) really gets my blood
flowing. I have to fight the urge to crank up the treadmill speed by 2 mph
every time it comes on. I feel like I could go twice as fast when that song
comes on! I need to fill out my playlist with some more stuff so it doesn't
get stale. Right now, I've got ~35 songs, but I can tell it will get old soon.

I could really use a perfect week, where I don't miss a single day, and I hit
all my targets. So far so good - had a great workout today, with upper body
followed by a 5K at 7 mph. I even bumped to 8.6 mph for the last half mile.
The whole workout felt really great.

## Sunday, February 19, 2017

Ran a 10K for the first time yesterday. It was harder than expected, despite
starting out a relatively slow place of 6.5 mph. In fact, I even had to lower
to 6.3 mph for the last 1.5 miles. I'm not even sure what the limiting factor
was - my breathing didn't feel too fast or heavy, my muscles felt fine; it was
just hard! I feel great that I was able to do it on my first try, but not too
happy with the pace, since it took an hour to run. I don't plan to run farther
than 10k at any one time, and probably only once a week. If I can get my time
down to 45 minutes, I'll be pretty happy, though that is probably just as hard
or harder than a sub-20 5k.

I ran a lot more this week - 5 out of 7 days, for a total of 18.65 miles, or
about twice as much as last week. The plan was to run 6 days, but I added in
an extra rest day due to soreness from lifting weights.

Lifting weights last Sunday felt good, but I pushed it way too hard,
considering it was the first time in a good 6 months. I was incredibly sore
the first part of the week, to the point where I couldn't even fully extend my
arms above my head. Even today, a full week later, I am sore, though I'm
feeling good enough to hit the weights again. Sometimes another session
actually helps relieve the soreness. I'll make sure to stretch better this
time, and not use too much weight.

I looked up some of Kevin Caster's race results, since he's the best runner
I know personally. In May of last year, he ran the Downtown Melbourne 5K in 18:57.
If he can do it, so can I.

My plan is to run 6 days this week, mixing in 3 weightlifting sessions (SuWF),
with one full rest day on Monday. Tuesday will be my max effort day.

```
M: Rest
T: 3.1 miles @ 7.8 mph
W: 3.1 miles @ 6.8 mph (after lifting)
T: 3.1 miles @ 7.6 mph
F: 3.1 miles @ 6.8 mph (after lifting)
S: 6.25 miles @ 6.6 mph
S: 4.0 miles @ 6.5 mph (after lifting)

Total MPW: 22.65
```

## Saturday, February 11, 2017

This week was...okay. I ran MWF, so at least I showed up.

```
M: 4 miles @ 7.2 mph
W: 3.1 miles @ 7.8 mph
F: 2.15 miles @ 7.9 mph :(
```

The Friday run was dissapointing, since I thought I'd be able to handle the
small speed increase, but my heart just couldn't keep up. It seems like 7.8
mph for 5K is my upper limit right now.

After reading a bit online ([this](https://drive.google.com/file/d/0B3TYR3d9S1s1dFpwa3E4NmZfOW8/view)
page is really helpful), I think it makes sense to start running more days per
week at a lower average intensity. Something like:

```
M: 3.1 miles @ 7.4 mph
T: 3.1 miles @ 7.4 mph
W: Rest
T: 3.1 miles @ 7.8 mph
F: 3.1 miles @ 7.4 mph
S: 5.0 miles @ 6.6 mph
S: 5.0 miles @ 6.6 mph

Total MPW: 22.4
```

I'll give this a shot for a bit. After a couple of weeks of this, I'll
probably start mixing in more high intensity workouts per week
so that I can continue to chip away at my sub-20 goal.

## Saturday, February 4, 2017

Another good week, ran MWF.

My Monday run was rough. After a successful 7.8 mph run the Saturday before,
I decided to go for 8.0, but only made it 2 miles into the run. I was
completely gassed, so I dropped it down to 7.6, but only made it another half
mile and called it quits for the day. Was not too happy about that.

I stuck with the 7.8 pace for Wednesday and Friday. By Friday, 7.8 wasn't that
bad. I was getting somewhat tired with about 0.5 miles to go in the 5K, but
overall, it felt much easier.

It's probably time to start mixing in some lower-intensity longer runs. I'm
thinking a 10K at 7.0 mph should be doable. I'm feeling a little sick today,
so it may be best to just relax this weekend.

It seems the rule of thumb for long-distance running is - if you can sing
you're going too slow, if you can't hold a conversation you're going too fast.
I think my 5K pace is right at the upper end of barely being able to hold
a conversation. But I think that's okay for 5K, because it's really not that
long. I really like that I can be done with a 5K run in 25 minutes or less.

## Saturday, January 28, 2017

I ran all three days this week (MWF), making progress with each run:

* Monday - 3.2 miles @ 7.2 mph
* Wednesday - 3.2 miles @ 7.4 mph
* Friday - 3.2 miles @ 7.6 mph

I've nearly achieved my first small goal, which is a 25-minute 5k. Actually,
I just looked this up, and apparently 5 km is only 3.107 miles, not 3.2.
So I need to redo my goals. I believe I've hit the first one with my 7.6 mph
pace.

Here's a useful snippet of python for computing 5k times:

```python
from datetime import datetime, timedelta
import math

# How long will it take to run a 5K with a certain treadmill speed
def time_for_5k(mph):
  secs = ((mph/3.107)**-1)*3600.0
  return datetime.fromtimestamp(secs).strftime('%M:%S')


# What should the treadmill speed be to run a 5k in a certain time
def mph_for_5k_time(mins, secs):
  td = timedelta(minutes=mins, seconds=secs)
  total_seconds = td.total_seconds()
  mph = ((total_seconds/3600.0)/3.107)**-1

  # Only keep one decimal place, and always round up
  return math.ceil(mph*10.0)/10.0
```

So with my 7.6 mph pace, I've run the 5k in 24:31. In fact, I've very nearly
reached my next small goal, which requires a 7.8 pace.

*(Update)* - Was restless this evening, so I decided to do some running and
knocked out a 5K at 7.8 mph, which completes my second sub-goal (sub-24)!
I'm about a month and a half ahead of schedule. Now the real work begins.

## Friday, January 20, 2017

Ran 3.2 miles this morning at a 7.2 for 80% of the way and 7.0 for the
remainder. This was my second day running after a month-long break, so I was
a little winded. But still strictly better than the previous run, which was at
7.0.

The near-term goal is a 25 minute 5K, which I am fairly close to. That would
require a 7.7 speed on the treadmill. I know I've done 7.6 in the past
6 months at some point, so it should be achievable by Feb 15.

I plan to do most of my running on the treadmill, for science and stuff. It's
just easier to track. I enjoy running in mission bay too - perhaps I'll do
that on the weekends. Right now, I plan to run 3 days a week (MWF), though
I'll probably have to ramp up the training as I get closer to my goal.

People online suggest that it's typical to run 40 miles/week to get to
sub-20! That's a lot of running. Right now I'm only running 10 MPW, and I feel
a lot of latent potential in me, even just running 3 times. My plan is to
continue to run 3x a week until I feel myself stalling. I don't want to make
the mistake of running too much early on, then fizzling out later.

I think I have a natural talent for running, but I've never really pushed
myself very hard. I recall running a 6:30 mile in middle school, but then
I got caught up in other activites. I look forward to finding out what my
limits are.
