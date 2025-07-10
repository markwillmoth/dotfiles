#!/bin/bash
(
    flock -n 200 || exit 1

    PACMAN_UPDATES=$(CHECKUPDATES_DB=/tmp/checkupdates-db-waybar checkupdates 2>/dev/null | wc -l)
    AUR_UPDATES=$(paru -Qum --aur 2>/dev/null | wc -l)
    TOTAL_UPDATES=$((PACMAN_UPDATES + AUR_UPDATES))

    if [ "$TOTAL_UPDATES" -ne 0 ]; then
        echo " $PACMAN_UPDATES  $AUR_UPDATES"
    fi

) 200>/tmp/update_get_count.lock
