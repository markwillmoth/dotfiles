#!/bin/bash

MONITOR_WIDTH=3440
MONITOR_HEIGHT=1440

MONITOR_X=1440
MONITOR_Y=720

OFFSET_X=100
OFFSET_Y=50
FUZZEL_WIDTH=400

POS_X=$((MONITOR_X + MONITOR_WIDTH - FUZZEL_WIDTH - OFFSET_X))
POS_Y=$((MONITOR_Y + OFFSET_Y))

SELECTION="$(printf "1 - Lock\n2 - Suspend\n3 - Log out\n4 - Reboot\n5 - Reboot to UEFI\n6 - Hard reboot\n7 - Shutdown" | fuzzel --anchor top-right --x-margin=24 --y-margin=16 --dmenu -l 7 )"

case $SELECTION in
	*"Lock")
		hyprlock;;
	*"Suspend")
		systemctl suspend;;
	*"Log out")
		hyprctl dispatch exit;;
	*"Reboot")
		systemctl reboot;;
	*"Reboot to UEFI")
		systemctl reboot --firmware-setup;;
	*"Hard reboot")
		pkexec "echo b > /proc/sysrq-trigger";;
	*"Shutdown")
		systemctl poweroff;;
esac