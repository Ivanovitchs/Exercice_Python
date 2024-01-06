set terminal pngcairo enhanced
set output 'graphique_temps.png'
set title 'Temps moyen de tri pour différentes méthodes'
set xlabel 'Taille du tableau'
set ylabel 'Temps moyen de tri (secondes)'
plot 'resultats_stats_tri.txt' using 1:2 with lines title 'Tri Bulles', \
     '' using 1:4 with lines title 'Tri Insertion', \
     '' using 1:6 with lines title 'Tri Sélection', \
     '' using 1:8 with lines title 'Tri Rapide'

set output 'graphique_ecart_type.png'
set title 'Écart-type de tri pour différentes méthodes'
set ylabel 'Écart-type (secondes)'
plot 'resultats_stats_tri.txt' using 1:3 with lines title 'Tri Bulles', \
     '' using 1:5 with lines title 'Tri Insertion', \
     '' using 1:7 with lines title 'Tri Sélection', \
     '' using 1:9 with lines title 'Tri Rapide'
