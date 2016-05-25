#!/bin/sh

echo "21"  | sudo tee -a /sys/class/gpio/export
echo "out" | sudo tee -a /sys/class/gpio/gpio21/direction
echo "1"   | sudo tee -a  /sys/class/gpio/gpio21/value

