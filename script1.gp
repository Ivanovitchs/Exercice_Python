set terminal pngcairo enhanced
set output 'graphique.png'
set title 'Évolution du temps nécessaire au tri à bulles'
set xlabel 'Taille du tableau'
set ylabel 'Temps moyen de tri (secondes)'
plot 'resultats_stats_ordonne.txt' with lines title 'Ordonné', \
     'resultats_stats_inverse.txt' with lines title 'Inverse', \
     'resultats_stats_melange.txt' with lines title 'Mélangé'
