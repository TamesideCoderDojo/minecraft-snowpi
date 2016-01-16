## To find out how to use this file, see README.md
# Import all the required libraries
import mcpi.minecraft as minecraft
import time
import RPi.GPIO as GPIO

# A Dictionary list of all the SnowPi LEDs and their related pin numbers
leds = {
    "leftEye": 23,
    "rightEye": 24,
    "nose": 25,
    "topLeftButton": 7,
    "middleLeftButton": 8,
    "bottomLeftButton": 9,
    "topRightButton": 17,
    "middleRightButton": 18,
    "bottomRightButton": 22
}

# A Dictionary list of the status of each of the SnowPi LEDs - True for on, False for off
ledStatus = {
    "leftEye": False,
    "rightEye": False,
    "nose": False,
    "topLeftButton": False,
    "middleLeftButton": False,
    "bottomLeftButton": False,
    "topRightButton": False,
    "middleRightButton": False,
    "bottomRightButton": False
}

# A Dictionary list of the locations of each of the Minecraft snowman buttons
# Replace each False value with a Dictionary of the block's coordinates - like {'x': 10, 'y': 10, 'z': 10}
buttonBlocks = {
    "leftEye": False,
    "rightEye": False,
    "nose": False,
    "topLeftButton": False,
    "middleLeftButton": False,
    "bottomLeftButton": False,
    "topRightButton": False,
    "middleRightButton": False,
    "bottomRightButton": False
}

# Disable warnings if we didn't exit cleanly
GPIO.setwarnings(False)

# Use GPIO Numbering for our LED pins
GPIO.setmode(GPIO.BCM)

# Setup LED pins as outputs and turn them all on
for ledName, ledCode in leds.iteritems():
    GPIO.setup(ledCode, GPIO.OUT)
    GPIO.output(ledCode, True)

# Wait half a second
time.sleep(0.5)

# Turn off all our LED pins
for ledName, ledCode in leds.iteritems():
    GPIO.output(ledCode, False)

# Connect to the running minecraft game
mc = minecraft.Minecraft.create()

# The main code of our program - surrounded by a try statement to neatly handle CTRL-C
try:
    # Run forever (or until we hit CTRL-C
    while True:

        # Check for blocks being it with a sword
        blockHits = mc.events.pollBlockHits()

        # Loop through all the blocks that have been hit
        for blockHit in blockHits:
            # If we have any that are hit, get the position of the block
            blockPosition = blockHit.pos

            # Display the position of the block on the console
            print("Hit at location {'x': "+`blockPosition.x`+", 'y': "+`blockPosition.y`+", 'z': "+`blockPosition.z`+'}')

            # Loop through all the button location values we set up earlier
            for buttonName, buttonLocation in buttonBlocks.iteritems():
                #  If any of the buttonBlock entries have coordinate Dictionaries instead of being False then
                if buttonLocation != False:

                    # Check if the block that was hit matches the coordinates in the Dictionary
                    if buttonLocation['x'] == blockPosition.x and buttonLocation['y'] == blockPosition.y and buttonLocation['z'] == blockPosition.z:
                        # If the LED is on turn it off
                        if ledStatus[buttonName]:
                            # Tell the console we're turning it off
                            print('Turning off '+buttonName)
                            # Turn it off
                            GPIO.output(leds[buttonName], False)
                            # Store the off status in the ledStatus Dictionary so we can check it later
                            ledStatus[buttonName] = False
                        # Otherwise turn it on
                        else:
                            # Tell the console we're turning it on
                            print('Turning on '+buttonName)
                            # Turn it on
                            GPIO.output(leds[buttonName], True)
                            # Store the on status in the ledStatus Dictionary so we can check it later
                            ledStatus[buttonName] = True
        # Wait 0.1 seconds so we don't end up triggering the script again from the same sword hit
        time.sleep(0.1)
# Somebody hit CTRL-C
except KeyboardInterrupt:
    # Exit neatly and call GPIO.cleanup() to let go of the pins
    print("\nExiting")
    GPIO.cleanup()
