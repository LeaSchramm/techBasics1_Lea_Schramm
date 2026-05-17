In this updated version of the Späti game, the code is much cleaner because it is split into smaller, organized parts called functions. 
In the old code, everything was squeezed into one big start_game() function, which made it confusing to read. 
Now, the game is divided into separate scenes like buying_beer(name) and buying_icecream(name). 
The math for the total cost is also moved into its own helper function, calculation_price(quantity), 
which calculates the math and uses a return statement to send the final price back to the game.

This change also fixes how the code handles variables and data types. Important numbers that never change, 
like BEER_PRICE, ICECREAM_PRICE, and BEER_STOCK, are now global constants written in uppercase at the very top of the script. 
This keeps them safe so the game cannot accidentally overwrite them. Other pieces of information, like the number of beers 
bought or the flavor of the ice cream, are kept as local variables inside their own functions. To connect the scenes, 
the players name is simply passed along as an argument from one function to the next.

Finally, using the right data types makes the game much more stable. 
rices use floats because they need decimal points, while stock levels use integers because you can only buy whole bottles of beer. 
Text inputs use string methods like .lower() to prevent typos from crashing the game. 
Overall, this new structure makes the code incredibly easy to read and follow. 
It also makes debugging much faster because if something breaks, you can test and fix one single function without messing up the rest of the game.
