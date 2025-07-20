#!/bin/bash
zenity --question \
    --title="Confirm Screen Lock" \
    --text="Are you sure you want to enable screen lock?" \
    --ok-label="Yes" \
    --cancel-label="No" && playerctl pause && hyprlock
