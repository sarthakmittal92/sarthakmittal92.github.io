---
layout: post
date: 2022-04-17
title: Peer-to-Peer Network Simulator
subtitle: CS252 (Computer Networks Lab), IIT Bombay
cover-img: https://i.imgur.com/6sKWh4m.png
---

[![Code](https://i.imgur.com/AtIPmkl.png){:style="display:block; margin-left:auto; margin-right:auto; max-width:10%;"}](https://github.com/sarthakmittal92/network-simulator)

## Description
In this project we implemented a P2P network for searching and
downloading files. The overview is as follows:

There is a network of clients which are interconnected with
each other based on a specified topology. A client is provided
with the following information as arguments. Note the same
client code can be run multiple times with different arguments
to mimic different clients.
- A directory path: this is specific to this client. The
client is the owner of all files present in that directory.
Another client may be searching for these files to download.
- A path to a configuration file. See sample file contents below.

Each of the n clients upon initialization process their
arguments; setup connections with immediate neighbors and
print relevant output (see details below).

After this, each client searches for certain files
as specified in the configuration file. It can search only
upto a specified depth d. For example d = 2 means, it will
search clients upto 2 hops away from it.

If a file is found at another client, it sets up a separate
TCP connection (if not already present) with that client
and receives the file. After reception, this connection is
closed. File search happens only via the initial
connections specified.

Sample configuration file contents:
- Client ID and port on which it is ready to listen for
incoming connections.
- A list of immediate neighbors and the ports they are
listening on. The client has direct connections with
these neighbors for search purposes.
- A list of files which the client searches for in the
network. These files the client does not possess
originally, hence it wants to search and finally
download them. The downloaded files are stored in the
above mentioned directory path under a folder
"Downloaded". These files are NOT made available to
others who are searching, since this client is not the
owner.

#### Image credits
- [Imgur](https://imgur.com/) and [BeFunky](https://www.befunky.com/dashboard/)
- [https://hoteltechreport.com/news/cloud-computing](https://hoteltechreport.com/news/cloud-computing)