#!/bin/bash
(
    flock -n 200 || exit 1

    PACMAN_UPDATES=$(checkupdates 2>/dev/null | wc -l)
    AUR_UPDATES=$(paru -Qum --aur 2>/dev/null | wc -l)
    TOTAL_UPDATES=$((PACMAN_UPDATES + AUR_UPDATES))


    if [ "$TOTAL_UPDATES" -eq 0 ]; then
        MESSAGE="System is up to date"
        notify-send "$MESSAGE"
        echo "$MESSAGE"
        exit 0
    fi


    # Launch Kitty here with update.sh
    kitty sh -c "$HOME/.config/waybar/scripts/update_run.sh"

) 200>/tmp/update_launch_terminal.lock
