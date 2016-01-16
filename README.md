Minecraft SnowPi
================

Here's how to use minecraft to control the lights on your SnowPi snowman.

First, connect up your Pi, and plug your SnowPi snowman onto the GPIO pins of your Pi.

Next, start up a new game in Minecraft, and make sure the window is moved to one side so you can still have room for the Python console.

Build a model of your SnowPi snowman in Minecraft. Make sure you add blocks to use as buttons for all the LEDs!

Once you've built your snowman, open a command prompt. Type `sudo idle` to start IDLE with root privileges so your script can control the GPIO pins.
 
Open the minecraft_snowpi.py script in IDLE using the File > Open menu option.

Run the script using F5. Once it is running the LEDs on the SnowPi will flash on for half a second.

Using a sword in Minecraft, hit the blocks you added as buttons for the LEDs. As you hit each block, the console will show the coordinates of the block that you can add to the buttonBlocks Dictionary, instead of False.

Do this for each button block, until you have entered all the coordinates for all the buttons. Once you're happy you have the right coordinates, save the script. Stop the currently running version of the script using CTRL-C in the console.

Run your updated script using F5.

Using your Minecraft sword, hit the button blocks again - the SnowPi lights matching each block should turn on or off when you hit the block. Don't worry if they don't work first time - check the coordinates in the console for each block you hit, and make sure they match with the coordinates in the buttonBlocks Dictionary.

Keep on saving, stopping the script and restarting it using F5 until it works.

Extra Challenges
----------------

1. Instead of turning the lights on and off - can you make them flash when you hit the button block?
2. Can you make the button block change colour to show if the light is on or off?



