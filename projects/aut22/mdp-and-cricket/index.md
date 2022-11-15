---
layout: post
date: 2022-10-14
title: MDP Planning & Cricket
subtitle: CS747 (Reinforcement Learning), IIT Bombay
cover-img: https://i.imgur.com/AFtLsMT.png
---

[![Code](https://i.imgur.com/AtIPmkl.png){:style="display:block; margin-left:auto; margin-right:auto; max-width:10%;"}](https://github.com/sarthakmittal92/mdp-and-cricket)

## Description
This project has code to compute an optimal policy for a
given MDP using the algorithms that were discussed in the
course: Value Iteration, Howard's Policy Iteration, and
Linear Programming (using PuLP). Input to these algorithms will be an MDP
and the expected output is the optimal value function, along
with an optimal policy. There is an optional command line
argument for the policy, which evaluates the value function
for a given policy instead of finding the optimal policy, and
returns the action and value function for each state in the
same format.

MDP solvers have a variety of applications. The second part of
this project uses the solver to find an optimal policy for
a batter chasing a target during the last wicket in a game of
cricket.

#### Image credits
- [Imgur](https://imgur.com/) and [BeFunky](https://www.befunky.com/dashboard/)
- [https://vitalflux.com/reinforcement-learning-real-world-examples/](https://vitalflux.com/reinforcement-learning-real-world-examples/)