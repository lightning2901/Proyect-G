#lightning2901
#here we have some calculations to get the total of players

Valores_picoBattle = [17, 10, 4, 2.6, 1.9, 2.2, 2.4, 2.2, 2.7, 1.8, 2.4, 10, 10, 6.5, 4, 5.5, 6]
#print(len(Valores_picoBattle))

Valores_picoHalo = [11.8, 8.6, 6.4, 4.5, 3.5, 3.1, 4.8, 9.1, 6.3, 5.4, 4.4, 4.9, 5.5, 5.4, 4.8, 4.5, 4.3]
#print(len(Valores_picoHalo))

Amount_of_players_Total_Both_Games = []

for i in Valores_picoBattle:
    for j in Valores_picoHalo:
        Amount_of_players_Total_Both_Games.append(i+j)

print(Amount_of_players_Total_Both_Games[0], Amount_of_players_Total_Both_Games[16], Amount_of_players_Total_Both_Games[33], Amount_of_players_Total_Both_Games[50],Amount_of_players_Total_Both_Games[67], Amount_of_players_Total_Both_Games[84],Amount_of_players_Total_Both_Games[101],Amount_of_players_Total_Both_Games[118], Amount_of_players_Total_Both_Games[135],Amount_of_players_Total_Both_Games[152], Amount_of_players_Total_Both_Games[169], Amount_of_players_Total_Both_Games[186], Amount_of_players_Total_Both_Games[203], Amount_of_players_Total_Both_Games[220], Amount_of_players_Total_Both_Games[237], Amount_of_players_Total_Both_Games[254], Amount_of_players_Total_Both_Games[271])
#print((Amount_of_players_Total_Both_Games))
print("All values are talking about thousand of players")

#E E15 F F15 M M15 A A15 M M15 J J15 Jul Jul15 AUG AUG15 SEP
#17 values

#now, here are other calculus to get the difference of players

ValoresBattle = (17, 10, 4, 2.6, 1.9, 2.2, 2.4, 2.2, 2.7, 1.8, 2.4, 10, 10, 6.5, 4, 5.5, 6)
ValoresHalo = (11.8, 8.6, 6.4, 4.5, 3.5, 3.1, 4.8, 9.1, 6.3, 5.4, 4.4, 4.9, 5.5, 5.4, 4.8, 4.5, 4.3)
suma1 = sum(ValoresBattle)
print("These are the battlefield players")
print(suma1)
suma2 = sum(ValoresHalo)
print("These are the Halo players")
print(suma2)

print("And now the comparison between Battlefield and Halo")
print(suma1-suma2)

print("The results shows that Battlefield 2042 has had a deficit of at least 6.09 thousand players, compared with Halo")