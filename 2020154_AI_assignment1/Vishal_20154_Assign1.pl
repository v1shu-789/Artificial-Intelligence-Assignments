go :-   write('\n'), electives(List), write('Electives that you can take are : '),
        write(List), nl, undo.

electives(artificial_intelligence) :- artificial_intelligence, !.
electives(natural_language_processing) :- natural_language_processing, !.
electives(machine_learning) :- machine_learning, !.
electives(advanced_machine_learning) :- advanced_machine_learning, !.
electives(computer_networks) :- computer_networks, !.
electives(computer_graphics) :- computer_graphics, !.
electives(network_security) :- network_security, !.
electives(three_d_animation) :- three_d_animation, !.
electives(digital_image_processing) :- digital_image_processing, !.
electives(foundations_of_finance) :- foundations_of_finance, !.
electives(no_choices).

artificial_intelligence :-  (branch(cse); branch(csai)),
                            check_gpa(7.0),
                            done(dsa),
                            done(dm),
                            interest(artificial_intelligence),
                            (career(software_engineering); career(ai_engineer); career(user_experience); career(data_analyst)).
                            
natural_language_processing :-  (branch(cse); branch(csai)),
                                check_gpa(7.5),
                                done(pns),
                                done(ada),
                                done(ip),
                                interest(machine_learning),
                                (career(nlp_researcher); career(nlp_analyst)).
                    
machine_learning :- (branch(cse); branch(csai)),
                    check_gpa(7.5),
                    done(ip),
                    done(pns),
                    (done(m3); done(ra1)),
                    interest(machine_learning),
                    (career(ml_engineer); career(data_analyst)).
                  
advanced_machine_learning :-    (branch(cse); branch(csai)),
                                check_gpa(7.5),
                                done(pns),
                                (done(ml); done(sml); done(nlp)),
                                interest(machine_learning),
                                (career(ml_engineer); career(data_analyst); career(nlp_scientist)).
                              
computer_networks :-    (branch(cse); branch(csai); branch(ece)),
                        check_gpa(7.0),
                        done(ada),
                        interest(information_security),
                        (career(network_analyst); career(field_service_engineer); career(computer_system_analyst)).
                        
computer_graphics :-    (branch(cse); branch(csai); branch(ece)),
                        check_gpa(7.0),
                        done(ip),
                        done(dsa),
                        (interest(user_experience); interest(animation)),
                        (career(graphic_designer); career(web_designer)).
                        
network_security:-  (branch(cse); branch(csai); branch(ece)),
                    check_gpa(7.0),
                    done(cn),
                    interest(information_security),
                    (career(network_analyst); career(field_service_engineer); career(cyber_security)).
                    
three_d_animation :-    (branch(cse); branch(csai); branch(ece)),
                        check_gpa(6.5),
                        done(ip),
                        done(dsa),
                        (interest(user_experience); interest(animation)),
                        (career(graphic_designer); career(web_designer); career(film_making)).
                       
digital_image_processing :- (branch(cse); branch(csai); branch(ece)),
                            check_gpa(6.5),
                            done(pns),
                            (interest(user_experience); interest(animation)),
                            (career(graphic_designer); career(web_designer); career(film_making)).
                            
foundations_of_finance :-   (branch(cse); branch(ece)),
                            check_gpa(6.5),
                            done(mnb),
                            (interest(economics); interest(finance)),
                            (career(stock_market); career(bank_manager); career(finance_consultant)).
                         
ask_ques(Query,X) :-

    write(X),
    write(Query),
    write('? '),
    read(Resp),
    nl,
    ( 
        (Resp == yes ; Resp == y)
        ->
        assert(yes(Query));
        assert(no(Query)), fail
    ).

:- dynamic yes/1, no/1.

branch(B) :-
   (
        yes(B) -> true ; 
        (
            no(B) -> fail ; 
            ask_ques(B, 'Is your branch : ')
        )
   ).

done(D) :-
   (
        yes(D) -> true ; 
        (
            no(D) -> fail ; 
            ask_ques(D, 'Have you completed the course : ')
        )
   ).

check_gpa(G) :-
   (
        yes(G) -> true ; 
        (
            no(G) -> fail ; 
            ask_ques(G,'Is your GPA above or equal to : ')
        )
   ).

interest(I) :-
    (
        yes(I) -> true ; 
        (
            no(I) -> fail ; 
            ask_ques(I,'Are you interested in : ')
        )
    ).

career(C) :-
    (
        yes(C) -> true ; 
        (
            no(C) -> fail ; 
            ask_ques(C, 'Do you have wish this as your preferred career? : ')
        )
    ).

undo :- retract(yes(_)),fail. 
undo :- retract(no(_)),fail.
undo.