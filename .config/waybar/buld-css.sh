#!/bin/bash

NOTIFY=false
if [[ "$1" == "--notify" ]]; then
    NOTIFY=true
fi

pushd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null

if sassc style.scss style.css; then
    $NOTIFY && notify-send "✅ Waybar Sass compiled successfully"
    # pkill -SIGUSR2 waybar
else
    $NOTIFY && notify-send "❌ Waybar Sass compilation failed" "Check style.scss for errors"
    popd > /dev/null
    exit 1
fi

popd > /dev/null
