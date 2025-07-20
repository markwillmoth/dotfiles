#!/bin/bash
zenity --question \
    --title="Confirm Suspend" \
    --text="Are you sure you want to suspend?" \
    --ok-label="Yes" \
    --cancel-label="No" && systemctl suspend
