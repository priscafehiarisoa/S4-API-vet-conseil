INSERT INTO globale_race(designation) VALUES
    ('Chien'),
    ('Chat'),
    ('Poisson'),
    ('Oiseau'),
    ('Hamster'),
    ('Lapin'),
    ('Reptile');


INSERT INTO hebergement_nourriture(designation, description, prix_par_unite, unite) VALUES
    ('Croquettes pour chats', 'Croquettes équilibrées pour chats adultes', 12.99, 1.0),
    ('Croquettes pour chiens', 'Croquettes riches en protéines pour chiens de toutes tailles', 18.99, 1.0),
    ('Pâtée pour chiens', 'Pâtée savoureuse pour chiens de toutes races', 2.99, 1.0),
    ('Friandises pour chiens', 'Friandises à mâcher pour chiens de petite taille', 5.49, 1.0),
    ('Litière pour chats', 'Litière absorbante pour chats', 8.99, 1.0),
    ('Granulés pour rongeurs', 'Granulés nutritifs pour hamsters et cochons d''Inde', 4.99, 1.0),
    ('Paille pour litière', 'Paille de qualité pour litière de petits animaux', 3.49, 1.0),
    ('Graines pour oiseaux', 'Mélange de graines variées pour oiseaux de compagnie', 7.99, 1.0),
    ('Nourriture pour poissons rouges', 'Aliments en flocons pour poissons rouges', 9.99, 1.0),
    ('Nourriture pour tortues', 'Granulés spéciaux pour une alimentation équilibrée des tortues', 12.49, 1.0),
    ('Graines pour poules', 'Mélange de graines pour une alimentation saine des poules', 6.99, 1.0),
    ('Foin pour lapins', 'Foin frais et de qualité pour lapins nains', 4.99, 1.0),
    ('Aliments pour chiots', 'Aliments riches en nutriments pour chiots en pleine croissance', 15.99, 1.0),
    ('Nourriture pour furets', 'Aliments spécialement formulés pour les furets', 11.99, 1.0),
    ('Nourriture pour serpents', 'Rats congelés pour l''alimentation des serpents', 3.99, 1.0);


INSERT INTO hebergement_attribution(debut_interval_poids, fin_interval_poids, nourriture_id, race_id) VALUES
    (0, 100, 1, 2),
    (0, 100, 2, 1),
    (0, 100, 3, 1),
    (0, 100, 4, 1),
    (0, 100, 5, 2),
    (0, 100, 6, 5),
    (0, 100, 7, 2),
    (0, 100, 8, 4),
    (0, 100, 9, 3),
    (0, 100, 10, 7),
    (0, 100,11, 4),
    (0, 100,12, 5),
    (0, 100,13, 1),
    (0, 100,14, 5),
    (0, 100,15, 7);

insert into globale_client (nom,prenom,adresse,mail,contact)
values
       ('Andriamilamina','Manohy Arivelo','Ambohipo','mail@gmail.com','+2610345667889'),
       ('Rakotondrabary','Ravo hary','ambohipo','mail2@gmail.com','+261324545645'),
       ('andriamanarinivo ','aina daniella','ambohipo','mail3@gmail.com','+261345645643');

insert into globale_patient(age, nom, nature_id, proprietaire_id) VALUES
                    (4,'milou',1,1),
                    (3,'max',2,2),
                    (2,'boby',3,3);

INSERT INTO public.hebergement_tarifs_hebergement (id, date_changement_tarif, montant_journalier, montant_horaire, race_id) VALUES (1, '2023-06-26', 20000.00, 2000.00, 1);
INSERT INTO public.hebergement_tarifs_hebergement (id, date_changement_tarif, montant_journalier, montant_horaire, race_id) VALUES (2, '2023-06-26', 20000.00, 2000.00, 2);
INSERT INTO public.hebergement_tarifs_hebergement (id, date_changement_tarif, montant_journalier, montant_horaire, race_id) VALUES (3, '2023-06-26', 20000.00, 2000.00, 3);
INSERT INTO public.hebergement_tarifs_hebergement (id, date_changement_tarif, montant_journalier, montant_horaire, race_id) VALUES (4, '2023-06-26', 20000.00, 2000.00, 4);
INSERT INTO public.hebergement_tarifs_hebergement (id, date_changement_tarif, montant_journalier, montant_horaire, race_id) VALUES (5, '2023-06-26', 20000.00, 2000.00, 5);
INSERT INTO public.hebergement_tarifs_hebergement (id, date_changement_tarif, montant_journalier, montant_horaire, race_id) VALUES (6, '2023-06-26', 20000.00, 2000.00, 6);
INSERT INTO public.hebergement_tarifs_hebergement (id, date_changement_tarif, montant_journalier, montant_horaire, race_id) VALUES (7, '2023-06-26', 20000.00, 2000.00, 7);
