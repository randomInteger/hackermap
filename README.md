# hackermap
hackermap produces a histogram of the attempts to log into a debian linux box via SSH, stacked by country.

This python3 tool is designed to run on any debian/ubuntu linux system.

This tool depends on the host system having the 'geoiplookup' utility installed.

To install that tool, run:  sudo apt-get install geoip-bin

If you are disturbed by the results, please consider installing a tool like
fail2ban.

Run the tool:  python3 ./ssh_location_tracker.py

Example output screenshot:
