#!/bin/bash
output=$(nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits)
echo "$output"
