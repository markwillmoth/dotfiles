#!/bin/bash

response=$(curl -s "https://api.open-meteo.com/v1/forecast?latitude=54.7125&longitude=-1.2334&current_weather=true")
temp=$(echo "$response" | jq '.current_weather.temperature')
code=$(echo "$response" | jq '.current_weather.weathercode')


declare -A descriptions=(
  [0]="Clear sky"
  [1]="Mainly clear"
  [2]="Partly cloudy"
  [3]="Overcast"
  [45]="Fog"
  [48]="Rime fog"
  [51]="Light drizzle"
  [53]="Moderate drizzle"
  [55]="Dense drizzle"
  [56]="Light freezing drizzle"
  [57]="Dense freezing drizzle"
  [61]="Slight rain"
  [63]="Moderate rain"
  [65]="Heavy rain"
  [66]="Light freezing rain"
  [67]="Heavy freezing rain"
  [71]="Slight snow"
  [73]="Moderate snow"
  [75]="Heavy snow"
  [77]="Snow grains"
  [80]="Light rain showers"
  [81]="Moderate rain showers"
  [82]="Heavy rain showers"
  [85]="Light snow showers"
  [86]="Heavy snow showers"
  [95]="Thunderstorm"
  [96]="Thunderstorm + light hail"
  [99]="Thunderstorm + heavy hail"
)

declare -A icons=(
  [0]="☀️"     # fa-sun
  [1]="🌤️"    # fa-cloud-sun
  [2]="⛅"     # fa-cloud-sun
  [3]="☁️"     # fa-cloud
  [45]="🌫️"    # fa-smog
  [48]="🌁"     # fa-smog
  [51]="🌦️"    # fa-cloud-rain
  [53]="🌧️"    # fa-cloud-showers-heavy
  [55]="🌧️"
  [56]="🌧️❄️"  # rain + snow
  [57]="🌧️❄️"
  [61]="🌦️"
  [63]="🌧️"
  [65]="🌧️"
  [66]="🌧️❄️"
  [67]="🌧️❄️"
  [71]="🌨️"
  [73]="🌨️"
  [75]="❄️"
  [77]="❄️"
  [80]="🌦️"
  [81]="🌧️"
  [82]="🌧️"
  [85]="🌨️"
  [86]="❄️"
  [95]="⛈️"
  [96]="⛈️❄️"
  [99]="⛈️❄️"
)

icon="${icons[$code]:-❓}"

echo "$icon $temp°C"
