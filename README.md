# hackermap
hackermap produces a histogram of the attempts to log into a debian linux box via SSH, stacked by country.

This python3 tool is designed to run on any debian/ubuntu linux system, and is intended to allow you to easily monitor how many SSH login attempts your box is getting.  This is especially useful for AWS/Cloud instances and boxes that face the public internet (webservers, bitcoin nodes, etc...).  

This tool depends on the host system having the 'geoiplookup' utility installed.

To install that tool, run:  sudo apt-get install geoip-bin

If you are disturbed by the results, please consider installing a tool like
fail2ban:  https://github.com/fail2ban

Run the tool:  python3 ./ssh_location_tracker.py

Example output screenshot:

<img src="https://github.com/randomInteger/hackermap/blob/master/hackermap.png" width="600" heighth="400">

Future updates:  Please ping me if you use this tool and want improvements.  I am considering adding JSON/XML output support, database support, and potentially google maps api integration so the results can be plotted globally.

