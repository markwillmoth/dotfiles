#!/bin/bash
output=$(nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader,nounits)

# Split the string into two values
IFS=',' read -r val1 val2 <<< "$output"

# Trim whitespace
used=$(echo "$val1" | xargs)
total=$(echo "$val2" | xargs)

# Convert MiB to GiB using bc
used_g=$(awk "BEGIN { printf \"%.1f\", $used / 1024 }")
total_g=$(awk "BEGIN { printf \"%.1f\", $total / 1024 }")

echo "${used_g}G/${total_g}G"
