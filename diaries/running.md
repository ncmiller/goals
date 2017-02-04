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
