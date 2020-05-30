flight(toronto,air_canada,london,500,360)
flight(toronto,united,london,650,420)
flight(toronto,air_canada,madrid,900,480)
flight(toronto,united,madrid,950,540)
flight(toronto,iberia,madrid,800,480)
flight(madrid,air_canada,toronto,900,480)
flight(madrid,united,toronto,950,540)
flight(madrid,iberia,toronto,800,480)
flight(madrid,air_canada,barcelona,100,60)
flight(madrid,iberia,barcelona,120,65)
flight(madrid,iberia,valencia,40,50)
flight(madrid,iberia,malaga,50,60)
flight(barcelona,air_canada,madrid,100,60)
flight(barcelona,iberia,madrid,120,65)
flight(barcelona,iberia,valencia,110,75)
flight(barcelona,iberia,london,220,240)
flight(london,air_canada,toronto,500,360)
flight(london,united,toronto,650,420)
flight(london,iberia,barcelona,220,240)
flight(valencia,iberia,madrid,40,50)
flight(valencia,iberia,barcelona,110,75)
flight(valencia,iberia,malaga,80,120)
flight(malaga,iberia,madrid,50,60)
flight(malaga,iberia,valencia,80,120)
flight(paris,united,toulouse,35,120)
flight(toulouse,united,paris,35,120)

airport(toronto,50,60)
airport(madrid,75,45)
airport(barcelona,40,30)
airport(london,75,80)
airport(valencia,40,20)
airport(malaga,50,30)
airport(paris,50,60)
airport(toulouse,40,30)

isflight(A,B):-flight(A,airline,B,C,D).

isflightcheap(A,C,B):-flight(A,C,B,C,D),(C<400).

indirectflight(A,B):-flight(A,I,C,D,E),flight(C,G,B,F,H).

prefferedflight(A,C,B):-isflightcheap(A,C,B);flight(A,C,B,D,E),(C==air_canada).

bothexist(A,B):-flight(A,united,B,C,D),flight(A,air_canada,B,E,F).
