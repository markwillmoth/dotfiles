#!/bin/bash

if pgrep -x "mitmweb" > /dev/null; then
    echo "mitmweb is running. Stopping it..."
    pkill -x "mitmweb"
    echo "mitmweb stopped."
else
    echo "mitmweb is not running. Starting it..."
    # Start mitmweb in the background
    mitmweb --no-http2 &
    echo "mitmweb started."
fi
