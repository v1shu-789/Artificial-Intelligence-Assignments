:- dynamic branch/1.
:- dynamic gpa/1.
:- dynamic done/1.
:- dynamic interest/1.
:- dynamic career/1.

electives(artificial_intelligence) :- artificial_intelligence. 
electives(natural_language_processing) :- natural_language_processing.
electives(machine_learning) :- machine_learning.
electives(advanced_machine_learning) :- advanced_machine_learning.
electives(computer_networks) :- computer_networks.
electives(computer_graphics) :- computer_graphics.
electives(network_security) :- network_security.
electives(three_d_animation) :- three_d_animation.
electives(digital_image_processing) :- digital_image_processing.
electives(foundations_of_finance) :- foundations_of_finance.

check_gpa(X):- gpa(Y), Y >= X.

artificial_intelligence :-  (branch(cse); branch(csai)),
                            check_gpa(7.0),
                            done(dsa),
                            done(dm),
                            interest(artificial_intelligence),
                            (career(software_engineering); career(ai_engineer); career(user_experience); career(data_analyst)),
                            write("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------"), nl,
                            write("\n\tARTIFICIAL INTELLIGENCE"), nl.

natural_language_processing :-  (branch(cse); branch(csai)),
                                check_gpa(7.5),
                                done(pns),
                                done(ada),
                                done(ip),
                                interest(machine_learning),
                                (career(nlp_researcher); career(nlp_analyst)),
                                write("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------"), nl,
                                write("\n\tNATURAL LANGUAGE PROCESSING"), nl.


machine_learning :- (branch(cse); branch(csai)),
                    check_gpa(7.5),
                    done(ip),
                    done(pns),
                    (done(m3); done(ra1)),
                    interest(machine_learning),
                    (career(ml_engineer); career(data_analyst)),
                    write("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------"), nl,
                    write("\n\tMACHINE LEARNING"), nl.

           
advanced_machine_learning :-    (branch(cse); branch(csai)),
                                check_gpa(7.5),
                                done(pns),
                                (done(ml); done(sml); done(nlp)),
                                interest(machine_learning),
                                (career(ml_engineer); career(data_analyst); career(nlp_scientist)),
                                write("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------"), nl,
                                write("\n\tADVANCED MACHINE LEARNING"), nl.


computer_networks :-    (branch(cse); branch(csai); branch(ece)),
                        check_gpa(7.0),
                        done(ada),
                        interest(information_security),
                        (career(network_analyst); career(field_service_engineer); career(computer_system_analyst)),
                        write("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------"), nl,
                        write("\n\tCOMPUTER NETWORKS"), nl.

computer_graphics :-    (branch(cse); branch(csai); branch(ece)),
                        check_gpa(7.0),
                        done(ip),
                        done(dsa),
                        (interest(user_experience); interest(animation)),
                        (career(graphic_designer); career(web_designer)),
                        write("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------"), nl,
                        write("\n\tCOMPUTER GRAPHICS"), nl.
                         
network_security:-  (branch(cse); branch(csai); branch(ece)),
                    check_gpa(7.0),
                    done(cn),
                    interest(information_security),
                    (career(network_analyst); career(field_service_engineer); career(cyber_security)),
                    write("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------"), nl,
                    write("\n\tNETWORK SECURITY"), nl.

three_d_animation :-    (branch(cse); branch(csai); branch(ece)),
                        check_gpa(6.5),
                        done(ip),
                        done(dsa),
                        (interest(user_experience); interest(animation)),
                        (career(graphic_designer); career(web_designer); career(film_making)),
                        write("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------"), nl,
                        write("\n\t3D ANIMATION"), nl.

digital_image_processing :- (branch(cse); branch(csai); branch(ece)),
                            check_gpa(6.5),
                            done(pns),
                            (interest(user_experience); interest(animation)),
                            (career(graphic_designer); career(web_designer); career(film_making)),
                            write("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------"), nl,
                            write("\n\tDIGITAL IMAGE PROCESSING"), nl.

foundations_of_finance :-   (branch(cse); branch(ece)),
                            check_gpa(6.5),
                            done(mnb),
                            (interest(economics); interest(finance)),
                            (career(stock_market); career(bank_manager); career(finance_consultant)),
                            write("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------"), nl,
                            write("\n\tFOUNDATIONS OF FINANCE"), nl.

facts(X):-
    ['facts.pl'],
    electives(X).