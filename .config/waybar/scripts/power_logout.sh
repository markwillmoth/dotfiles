#!/bin/bash
zenity --question \
    --title="Confirm Logout" \
    --text="Are you sure you want to logout?" \
    --ok-label="Yes" \
    --cancel-label="No" && hyprctl dispatch exit
