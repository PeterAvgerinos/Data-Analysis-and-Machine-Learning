find_sim_2(X, Y):- genre(X, G1),genre(X, G2),genre(Y, G1),genre(Y, G2), X \= Y.
find_sim_3(X, Y):- genre(X, G1),genre(X, G2),genre(X, G3),genre(Y, G1),genre(Y, G2), genre(Y,G3), X \= Y.
find_sim_4(X, Y):- genre(X, G1), genre(X, G2), genre(X, G3), genre(X,G4), genre(Y, G1), genre(Y, G2), genre(Y,G3), genre(Y,G4), X \= Y.
find_sim_5(X, Y):- genre(X, G1), genre(X, G2), genre(X, G3), genre(X,G4), genre(X, G5), genre(Y, G1), genre(Y, G2), genre(Y,G3), genre(Y,G4), genre(Y, G5), X \= Y.
director_sim(X, Y):- director(X, D1),director(Y, D2), X \= Y.
lang_sim(X, Y):- language(X, D1),language(Y, D2), X \= Y.
bnw_sim(X, Y):- black_and_white(X, D1), black_and_white(Y, D2), X \= Y.
country_sim(X, Y):- country(X, D1), country(Y, D2), X \= Y.
decade_sim(X, Y):- decade(X, D1), decade(Y, D2), X \= Y.
keyword_sim_1(X, Y):- keyword(X, K1),keyword(Y, K1), X \= Y.
keyword_sim_2(X, Y):- keyword(X, K1),keyword(X, K2),keyword(Y, K1),keyword(Y, K2), X \= Y.
keyword_sim_3(X, Y):- keyword(X, K1),keyword(X, K2),keyword(X, K3),keyword(Y, K1),keyword(Y, K2), keyword(Y,K3), X \= Y.
keyword_sim_4(X, Y):- keyword(X, K1), keyword(X, K2), keyword(X, K3), keyword(X,K4), keyword(Y, K1), keyword(Y, K2), keyword(Y,K3), keyword(Y,K4), X \= Y.
keyword_sim_5(X, Y):- keyword(X, K1), keyword(X, K2), keyword(X, K3), keyword(X,K4), keyword(X, K5), keyword(Y, K1), keyword(Y, K2), keyword(Y,K3), keyword(Y,K4), keyword(Y, K5), X \= Y.
studio_sim_1(X, Y):- studio(X, G1),studio(Y, G1), X \= Y.
studio_sim_2(X, Y):- studio(X, G1),studio(X, G2),studio(Y, G1),studio(Y, G2), X \= Y.
studio_sim_3(X, Y):- studio(X, G1),studio(X, G2),studio(X, G3),studio(Y, G1),studio(Y, G2), studio(Y,G3), X \= Y.
studio_sim_4(X, Y):- studio(X, G1), studio(X, G2), studio(X, G3), studio(X,G4), studio(Y, G1), studio(Y, G2), studio(Y,G3), studio(Y,G4), X \= Y.
studio_sim_5(X, Y):- studio(X, G1), studio(X, G2), studio(X, G3), studio(X,G4), studio(X, G5), studio(Y, G1), studio(Y, G2), studio(Y,G3), studio(Y,G4), studio(Y, G5), X \= Y.
actor_sim_1(X, Y):- actor1(X, G1),actor1(Y, G1), X \= Y.
actor_sim_2(X, Y):- actor1(X, G1),actor2(X, G2),actor1(Y, G1),actor2(Y, G2), X \= Y.
actor_sim_3(X, Y):- actor1(X, G1),actor2(X, G2),actor3(X, G3),actor1(Y, G1),actor2(Y, G2), actor3(Y,G3), X \= Y.
% movie_with_large_score(X, S1):- score(X,S1), S1 > 6.
process(X) :- write(X), nl.
movie_with_large_score(X,Y):- findall(M, (score(M, S1), atom_number(S1,Z), Z > 6), Y), member(M,Y), process(M).
recommender_1(X, Y):- movie_with_large_score(X,Y), find_sim_2(Y,Z), keyword_sim_1(Y,Z).
recommender_2(X, Y):- movie_with_large_score(X,Y),find_sim_1(X,Y), keyword_sim_2(X,Y).
recommender_3(X, Y):- movie_with_large_score(X,Y),find_sim_1(X,Y), keyword_sim_3(X,Y).
recommender_4(X, Y):- movie_with_large_score(X,Y),find_sim_1(X,Y), keyword_sim_4(X,Y).
recommender_5(X, Y):- movie_with_large_score(X,Y),find_sim_1(X,Y), keyword_sim_5(X,Y).
recommender_6(X, Y):- movie_with_large_score(X,Y),find_sim_2(X,Y), keyword_sim_1(X,Y).
recommender_7(X, Y):- movie_with_large_score(X,Y),find_sim_2(X,Y), keyword_sim_2(X,Y).
recommender_8(X, Y):- movie_with_large_score(X,Y),find_sim_2(X,Y), keyword_sim_3(X,Y).
recommender_9(X, Y):- movie_with_large_score(X,Y),find_sim_2(X,Y), keyword_sim_4(X,Y).
recommender_10(X, Y):- movie_with_large_score(X,Y),find_sim_2(X,Y), keyword_sim_5(X,Y).
recommender_11(X, Y):- movie_with_large_score(X,Y),find_sim_3(X,Y), keyword_sim_1(X,Y).
recommender_12(X, Y):- movie_with_large_score(X,Y),find_sim_3(X,Y), keyword_sim_2(X,Y).
recommender_13(X, Y):- movie_with_large_score(X,Y),find_sim_3(X,Y), keyword_sim_3(X,Y).
recommender_14(X, Y):- movie_with_large_score(X,Y),find_sim_3(X,Y), keyword_sim_4(X,Y).
recommender_15(X, Y):- movie_with_large_score(X,Y),find_sim_3(X,Y), keyword_sim_5(X,Y).
