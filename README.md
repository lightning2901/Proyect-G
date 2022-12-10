# Proyect-G
# Author
José Ángel López Gutiérrez, student from ENES Morelia
# Contact
jalg030129@gmail.com 
# License
GNU General Public License v3.0
Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

# Installation Info
To install and run you'll need to have installed Python 3 on your device, you can download an IDE like Pycharm, Visual Studio Code, emacs, etc. Once you got it installed you're going to dowldoad the file geometría.py or just copy the code if it's easier for you, and run it on your computer by pressing the button "run" on your IDE or by ./geometría.py on your terminal, you won't need anything else; be sure you give access to read an execute the file before running.

# Methodology
To do this posible the first step was the analysis of the data presented by steamcharts.com and then, looking at each 1st day of the month and taking notes about the number of players of each game, but also taking in count that some holidays and in-game updates may be the cause of the variability of the graphic.
Once we selected the infromation, in the program Geometría.py, there's two set of list, each one has 17 elements, we divides the month by two (1st and 15th day), selected the data, and by operating the set of list we get to know with proximity the difference between the amount of players.
# Proofs
Not only these games are avaliable on steam, they're also in platforms like EA PLay, Playstation Store, Xbox Gamepass, etc, but the biggest base of players still is Steam, and by consulting the information wich is transparent to everyone you can see it, also the JSON files can show you this, considering that is 2022 period January - August 

# Introduction
The objective of this project is to compare and see how it's been the behaviour in terms of the number of players between these 2 games, Battlefield being a new game that promised a lot, and Halo The Master Chief collection wich has 5 classic games from Halo Combat Evolved (2001) to Halo 4 (2012). The comparison will show us the difference on the amount of players each month from january to the very last day of august in 2022. Both are FPS (First Person Shooters) games with multiplayer online and with updates still going.



The first one is Battlefield
![BallefieldGrafica](https://user-images.githubusercontent.com/119823416/205553928-a5236422-c935-47cf-9f54-486d596562c1.png)

And the next is Halo The Master Chief Collection

![HaloMCCGrafica](https://user-images.githubusercontent.com/119823416/205553965-abb9e8cb-4332-47e8-9c75-64e074da0275.png)




Thanks to a webpage https://apps.automeris.io/wpd/ i was able to get the point of a graphic, and save it into a JSON wich is gonna be bellow, and get a CSV.
With those Files i was able to generate a graphic to compare both of them and see what the difference is.
# Results

![Comparacion Halo Battlefield](https://user-images.githubusercontent.com/119823416/206823339-ca082932-8854-42cd-9920-61b6b16587fd.png)

Battlefield is the blue line and Halo the orange one.




# Conclusion
As a conclusion,  got that Battlefield has a deficit from about 6 thousand players, those calculations are in the python file, with an explanation about how it works.
As we can see Halo's numbers are constant most of the time, and lately, they're growing, but the same can't be said for Battlefield. If we take a look at the feedback from the users we can say that a newer videogame is not always best that the classsic ones, but ultimately, having fresh content continously leads to be succesfull like Halo

# Bibliography 
https://steamplayercount.com/app/976730
https://steamplayercount.com/app/1517290
https://store.steampowered.com/app/976730/Halo_The_Master_Chief_Collection/
https://store.steampowered.com/app/1517290/Battlefield_2042/


