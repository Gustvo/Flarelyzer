<img align="right" src="http://i.imgur.com/Lgwgp5D.gif" alt="Flare Sorcerer">
<span class="badge-paypal"><a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=XU6L3JCZGKHSG" title="Donate to this project using Paypal"><img src="https://img.shields.io/badge/paypal-donate-blue.svg" alt="PayPal donate button" /></a></span>

# Flarelyzer

[![Join the chat at https://gitter.im/Javieracost/Flarelyzer](https://badges.gitter.im/Javieracost/Flarelyzer.svg)](https://gitter.im/Javieracost/Flarelyzer?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Linux compatible version of the [Tibialyzer](https://github.com/Mytherin/Tibialyzer) extension for the MMORPG Tibia

Currently implements a minimal subset of Tibialyzer's functionality, namely the on-rare-drop alerts. And just like it, Flarelyzer scans the server log and messages from the Tibia client in real-time by reading its memory in order to gather various statistics.

#### Whats with the name?
Original, isnt it? After i saw what Mytherin accomplished (*_on Linux!_*) before creating Tibialyzer, and being a Python and Linux enthusiast myself, i just couldnt help but expanding on his work! And thats where this project's name comes from: kind of a Tibialyzer, _a la_ me [[Flare Sorcerer](http://www.tibia.com/community/?subtopic=characters&name=Flare+Sorcerer)] (:

#### And what about the Tibia Rules?
Flarelyzer does not alter the Tibia client in any way, nor does it play the game for you. It only passively scans the Tibia process memoryto check for server log and chat messages and therefore it does not go against the [Tibia Rules](.tibia.com/support/?subtopic=tibiarules&rule=3b).

### Requirements
* __Pypy:__
    Fast, alternative, python implementation. You can grab portable binaries from [here](github.com/squeaky-pl/portable-pypy#latest-python-27-release) or simply install from your distribution's repositories (`sudo apt-get install pypy` for debian-based distros).
* __Libnotify-bin:__
    Library to send desktop notifications.  To install it, you can just run `sudo apt-get install libnotify-bin` as well.

### Usage
To use Flarelyzer simply download and extract the archive anywhere and run Flarelyzer.py (either by clicking on it, or from the command line) after opening the Tibia client, enter your superuser password, and an initial notification should pop up!

### Configuring
For the time being, Flarelyzer's customizability isnt all that great. To manage the items you want to be notified about, open the _agent.py_ file with any text editor and add/remove the items that are relevant to you in the `interesting` set at the beginning. It is also possible to adjust the pop-up duration in the line below.

### What's next?
Other than the necessary performance improvements and fixes under-the-hood, the following features are on the way:
* Full Fledged Qt Based UI
* Improved notifications<br>
  <img src="http://i.imgur.com/jJtMJjE.jpg"><br>
  _(preview, and these work even with the client on fullscreen!)_
* Allow key remapping

So stay tuned! The best is yet to come.
