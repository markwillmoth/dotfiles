#!/bin/bash
zenity --question \
    --title="Confirm Shutdown" \
    --text="Are you sure you want to shutdown?" \
    --ok-label="Yes" \
    --cancel-label="No" && systemctl poweroff
