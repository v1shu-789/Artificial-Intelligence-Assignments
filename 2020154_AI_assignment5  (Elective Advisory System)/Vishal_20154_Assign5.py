import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from pyswip import Prolog

def func (string):

    stemmer = PorterStemmer()
    words = word_tokenize(string)
    word_list = []

    for i in words:
        word_list.append(stemmer.stem(i))

    return word_list

print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\n\t\t\t\t\t\t\t\tElective Advisory System")
print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\nHi there! Welcome to our Elective Advisory System. \n\nWe would help you to build your future of your interest.")
print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\nFirst of all, Let's know about you. What is your name?")
name = input("\nMy name is - ")
print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\nHi {}! Hoping you are having a wonderful day. Let's now get to work. Shall we?".format(name))
print("\nLet's go deeper into you.")
print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------")

branch = input("\nWhat is your branch? {CSE, CSAI, ECE} - ")

tmp = func(branch.lower())

if 'commun' or 'ece' in tmp:
    branch = 'ece'

if 'intellig' or 'csai' in tmp:
    branch = 'csai'

if 'engin' or 'cse' in tmp:
    branch = 'cse'

gpa = input("\nWhat is your current gpa? - ")
gpa = float(gpa)
print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\nList of courses that you might have completed :- \n\n1. Data Structures and Algorithms\n2. Algorithm Design and Analysis\n3. Probability and Statistics\n4. Machine Learning\n5. Introduction to Programming\n6. Money and Banking\n7. Computer Networks\n8. Simple Machine Learning\n9. Natural Language Processing\n10. Discrete Mathematics\n11. Differential Equations\n12. Real Analysis")
cs = input("\nPlease list down all the courses that you have done :- ")

tmp = func(cs.lower())

courses = []

if 'structur' in tmp:
    courses.append('dsa')

if 'design' in tmp:
    courses.append('ada')

if 'statist' in tmp:
    courses.append('pns')

if 'learn' in tmp:
    courses.append('ml')

if 'program' in tmp:
    courses.append('ip')

if 'bank' in tmp:
    courses.append('mnb')

if 'simpl' in tmp:
    courses.append('sml')

if 'natur' in tmp:
    courses.append('nlp')

if 'discret' in tmp:
    courses.append('dm')

if 'equat' in tmp:
    courses.append('m3')

if 'real' in tmp:
    courses.append('ra1')

if 'comput' in tmp:
    courses.append('cn')

print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\nList of interest that you might have :-\n\n1. Economics\n2. Finance\n3. User Experience\n4. Animation\n5. Information Security\n6. Machine Learning\n7. Artificial Intelligence")
x = input("\nPlease list down all your interests :- ")

tmp = func(x.lower())

interests = []

if 'econom' in tmp:
    interests.append('economics')

if 'financ' in tmp:
    interests.append('finance')

if 'user' in tmp:
    interests.append('user_experience')

if 'anim' in tmp:
    interests.append('animation')

if 'inform' in tmp:
    interests.append('information_security')

if 'learn' in tmp:
    interests.append('machine_learning')

if 'intellig' in tmp:
    interests.append('artificial_intelligence')

print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\nList of possible careers you might have thought of pursuing :- \n\n1. Software Engineering\n2. Artificial Intelligence Engineering\n3. User Experience\n4. Data Analyst\n5. Natural Language Processing Researcher\n6. Natural Language Processing Analyst\n7. Natural Language Processing Scientist\n8. Machine Learning Engineer\n9. Network Analyst\n10. Computer System Analyst\n11. Field Service Engineer\n12. Graphic Designer\n13. Web Designer\n14. Cyber Security\n15. Film Making\n16. Stock Market\n17. Bank Manager\n19. Finance Consultant")
cr = input("\nPlease list down all your preffered career options :- ")

tmp = func(cr.lower())

careers = []

if 'softwar' in tmp:
    careers.append('software_engineering')

if 'intellig' in tmp:
    careers.append('ai_engineer')

if 'user' in tmp:
    careers.append('user_experience')

if 'data' in tmp:
    careers.append('data_analyst')

if 'research' in tmp:
    careers.append('nlp_researcher')

if 'natur' in tmp:
    if 'analyst' in tmp:
        careers.append('nlp_analyst')

if 'scientist' in tmp:
    careers.append('nlp_scientist')

if 'machin' in tmp:
    careers.append('ml_engineer')

if 'network' in tmp:
    careers.append('network_analyst')

if 'comput' in tmp:
    careers.append('computer_system_analyst')

if 'field' in tmp:
    careers.append('field_service_engineer')

if 'graphic' in tmp:
    careers.append('graphic_designer')

if 'web' in tmp:
    careers.append('web_designer')

if 'cyber' in tmp:
    careers.append('cyber_security')

if 'film' in tmp:
    careers.append('film_making')

if 'stock' in tmp:
    careers.append('stock_market')

if 'bank' in tmp:
    careers.append('bank_manager')

if 'financ' in tmp:
    careers.append('finance_consultant')

print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\nThanks for providing all the necessary information!")
print("\nThe electives that you chould take are :-")

fd = open("facts.pl", 'w')

fd.write("branch({}).\n".format(branch))
fd.write("gpa({}).\n".format(gpa))

for i in courses:
    fd.write("done({0}).\n".format(i))

for i in interests:
    fd.write("interest({}).\n".format(i))

for i in careers:
    fd.write("career({}).\n".format(i))

fd.close()

swi = Prolog()
swi.consult("C:/Users/viqha/Dropbox/My PC (LAPTOP-4G3OONOC)/Desktop/AI/Ass1.pl")
electives = list(swi.query("facts(X)"))
# print(electives)

print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\nThank You for choosing our Elective Advisory System! Have a great day ahead.")
print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------")