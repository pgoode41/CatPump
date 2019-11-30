# Map GPIO Pin
# gpio79 is pin 12 on the Jetson Nano
echo 79 > /sys/class/gpio/export
# Set Direction
echo out > /sys/class/gpio/gpio79/direction
# Bit Bangin'!
echo 1 > /sys/class/gpio/gpio79/value
sleep 1
echo 0 > /sys/class/gpio/gpio79/value
# Unmap GPIO Pin
echo 79 > /sys/class/gpio/unexport
# Query Status
#cat /sys/kernel/debug/gpio

# Map GPIO Pin
# gpio79 is pin 12 on the Jetson Nano
echo 232 > /sys/class/gpio/export
# Set Direction
echo out > /sys/class/gpio/gpio232/direction
# Bit Bangin'!
echo 1 > /sys/class/gpio/gpio232/value
sleep 1
echo 0 > /sys/class/gpio/gpio232/value
# Unmap GPIO Pin
echo 232 > /sys/class/gpio/unexport
# Query Status
#cat /sys/kernel/debug/gpio

# Map GPIO Pin
# gpio79 is pin 12 on the Jetson Nano
echo 17 > /sys/class/gpio/export
# Set Direction
echo out > /sys/class/gpio/gpio17/direction
# Bit Bangin'!
echo 1 > /sys/class/gpio/gpio17/value
sleep 1
echo 0 > /sys/class/gpio/gpio17/value
# Unmap GPIO Pin
echo 217 > /sys/class/gpio/unexport
# Query Status
#cat /sys/kernel/debug/gpio

# Map GPIO Pin
# gpio79 is pin 12 on the Jetson Nano
echo 16 > /sys/class/gpio/export
# Set Direction
echo out > /sys/class/gpio/gpio16/direction
# Bit Bangin'!
echo 1 > /sys/class/gpio/gpio16/value
sleep 1
echo 0 > /sys/class/gpio/gpio16/value
# Unmap GPIO Pin
echo 16 > /sys/class/gpio/unexport
# Query Status
#cat /sys/kernel/debug/gpio


# sudo nvidia-docker run --rm -ti -p 8085:8085 --privileged  pgoode41/catpump-api bash