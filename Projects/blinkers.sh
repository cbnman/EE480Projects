#!/bin/sh

cd /sys/class/leds/led0
sudo sh -c "echo mmc0 > trigger"

cd ~
cd /sys/class/leds/led1
sudo sh -c "echo mmc0 > trigger"
