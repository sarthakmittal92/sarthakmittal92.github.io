---
layout: post
date: 2022-09-12
title: Multi-Armed Bandits
subtitle: CS747 (Reinforcement Learning), IIT Bombay
cover-img: https://i.imgur.com/i8cGLfJ.png
---

[![Code](https://i.imgur.com/AtIPmkl.png){:style="display:block; margin-left:auto; margin-right:auto; max-width:10%;"}](https://github.com/sarthakmittal92/multi-armed-bandits)

## Description
This project is about the regret minimization algorithms
discussed in the course, and ability to extend them to
different scenarios.

Task 1 has implementation of UCB, KL-UCB, and Thompson Sampling,
more or less identical to the versions discussed in the course.

Task 2 involves an algorithm for batched sampling. The idea is
that at every decision making step, the algorithm specifies an
entire batch of arms to pull (for example, if the batch size
is 100, it could be split as perhaps 25 pulls for arm 1, 55
pulls for arm 2, and 20 pulls for arm 3). All these pulls are
performed and the results returned to the algorithm in aggregate
before its next batch of pulls.

Task 3 has an algorithm for the case when the horizon is equal
to the number of arms, but it is given that the arm means are
distributed uniformly (so if the horizon is 100, the arm means
are a permutation of [0, 0.01, 0.02, …, 0.99]).

#### Image credits
- [Imgur](https://imgur.com/) and [BeFunky](https://www.befunky.com/dashboard/)
- [https://en.wikipedia.org/wiki/Slot_machines_by_country](https://en.wikipedia.org/wiki/Slot_machines_by_country)