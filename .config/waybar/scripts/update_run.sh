#!/bin/bash

paru -Syu --noconfirm
status=$?

if [ $status -eq 0 ]; then
    echo "Update completed"
else
    echo
    echo "Update failed with status $status"
fi

echo

# Countdown function
for i in {5..1}; do
    echo -ne "\rClosing in $i... (press any key to close)"
    read -t 1 -n 1 key && break
done

# Reload Waybar after countdown or key press
pkill -SIGUSR2 waybar
exit $status
