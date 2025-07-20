#!/bin/bash
zenity --question \
    --title="Confirm Reboot" \
    --text="Are you sure you want to reboot?" \
    --ok-label="Yes" \
    --cancel-label="No" && systemctl reboot
