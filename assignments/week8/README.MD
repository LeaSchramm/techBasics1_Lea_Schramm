## The nostalgic DVD Screen

For this assignment, I decided to go with the classic DVD video logo. Even though the prompt asks us to use our favorite image, 
I really wanted to recreate the famous, nostalgic DVD loading screen that we all used to stare at as kids, just waiting for the logo to hit the corner perfectly.

To meet the project requirements, I built a custom DVDLogo class that works as the blueprint for the animation. 
The program spawns exactly three individual objects from this class. To make each logo unique, the code uses random variables 
during the initiation process; every time you run the script, the logos start at completely random positions, move at different speeds, 
and get their own unique, randomized RGB color tint.

The animation focuses entirely on linear movement, using precise edge-collision checks to make the logos bounce smoothly off the 
walls of the 1200x800 window. While working on the code, I used Gemini as an AI assistant for research—specifically to get a better grasp 
on how classes isolate data for different objects, and to figure out how to 
dynamically change the color of a PNG image in Pygame using the pygame.BLEND_RGBA_MULT flag.
