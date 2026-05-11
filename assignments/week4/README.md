#4 The generative art

This project is a little study of generative art using Python and first time the Turtle library. I toughts its interesting how we can use code to create a balance between perfect order and organic chaos with mathmatics, using randomness. 

The artwork starts with a strict plan: the grid of rows and columns created by "nested loops." To make the colors and whole artwork look beautiful, the code uses interpolation, for that effect i aked gemini how to do that. the interpolation calculates the position of each square to create a smooth color gradient that changes from red at the top to blue at the bottom. However, to keep it from looking too "perfect," every square gets a tiny random change in its color, creating a from of texture. 

The "artistic" feel comes from adding randomness to the grid. Instead of placing the squares in a perfect line, the code adds a "shaky" offset to the position of each shape, which mimics the small mistakes of a human hand. There is also a 10% chance that a square will not be drawn at all. This creates "gaps" in the image, making it look like an eroded or vintage pattern. Finally, the code uses a special "instant drawing" mode (tracer(0)) so that the computer can finish all the math behind the scenes and show the final masterpiece all at once. Its also interesting to "perform" the art with the (tracer(1)) but that needs some time to finish that, so i decided on the instant one. 

The artwork was inpired by the shown examnple in the exercise and I wanted to add the gradient from an artwork i saw a while ago but unfortunately cant remember the artist.
