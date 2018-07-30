#!/bin/sh -e

PIDX=$(ps -fea | grep bot.py | grep -v ' grep ' | awk '{print $2}')
if [ -n "$PIDX" ]
then
        echo ''
else
	/usr/bin/python bot.py > /dev/null 2>&1  &
fi


exit 0

