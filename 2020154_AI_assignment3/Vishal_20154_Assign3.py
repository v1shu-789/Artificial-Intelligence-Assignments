from durable.lang import *

def interest():

    print('\n\nWhich type of field would you like to pursue? :- ')
    print('\n1. Artificial Intelligence')
    print('\n2. Development')
    print('\n3. Network Security')
    print('\n4. Database Management')
    print('\n5. Design')
    print('\n6. Economics')
    print('\n7. Finance')
    print('\n8. Graphics')
    print('\n9. Psychology')
    
    print('\nEnter your choice :- ', end = " ")
    ch = input()

    return(ch)

with ruleset('interest'):

    @when_all(m.interest == 'Artificial Intelligence')
    def func(c):

        lst = ['Artificial Intelligence', 'Machine Learning', 'Natural Language Processing']

        for i in lst :

            ch = input('\nHave you done the course {0}? (press y/n) :- '.format(i))
            if (ch == 'y'):
                chh = input('\nWhat was your GPA in the course {0}? :- '.format(i))
                c.assert_fact('grade', {'course' : i, 'gpa' : float(chh)})

    @when_all(m.interest == 'Development')
    def func(c):

        lst = ['App Development', 'Web Development', 'Software Development']

        for i in lst :

            ch = input('\nHave you done the course {0}? (press y/n) :- '.format(i))
            if (ch == 'y'):
                chh = input('\nWhat was your GPA in the course {0} ? :- '.format(i))
                c.assert_fact('grade', {'course' : i, 'gpa' : float(chh)})

    @when_all(m.interest == 'Network Security')
    def func(c):

        lst = ['Computer Networks', 'Network Security']

        for i in lst :

            ch = input('\nHave you done the course {0}? (press y/n) :- '.format(i))
            if (ch == 'y'):
                chh = input('\nWhat was your GPA in the course {0}? :- '.format(i))
                c.assert_fact('grade', {'course' : i, 'gpa' : float(chh)})

    @when_all(m.interest == 'Database Management')
    def func(c):

        lst = ['Fundamentals of Database Management Systems', 'Database System Implementation']

        for i in lst :

            ch = input('\nHave you done the course {0}? (press y/n) :- '.format(i))
            if (ch == 'y'):
                chh = input('\nWhat was your GPA in the course {0}? :- '.format(i))
                c.assert_fact('grade', {'course' : i, 'gpa' : float(chh)})

    @when_all(m.interest == 'Design')
    def func(c):

        lst = ['Digital VLSI Design', 'Introduction to HCI']

        for i in lst :

            ch = input('\nHave you done the course {0}? (press y/n) :- '.format(i))
            if (ch == 'y'):
                chh = input('\nWhat was your GPA in the course {0}? :- '.format(i))
                c.assert_fact('grade', {'course' : i, 'gpa' : float(chh)})

    @when_all(m.interest == 'Economics')
    def func(c):

        lst = ['Money and Banking', 'Macroeconomics']

        for i in lst :

            ch = input('\nHave you done the course {0}? (press y/n) :- '.format(i))
            if (ch == 'y'):
                chh = input('\nWhat was your GPA in the course {0}? :- '.format(i))
                c.assert_fact('grade', {'course' : i, 'gpa' : float(chh)})

    @when_all(m.interest == 'Finance')
    def func(c):

        lst = ['Foundations of Finance', 'Entrepreneurial Finance']

        for i in lst :

            ch = input('\nHave you done the course {0}? (press y/n) :- '.format(i))
            if (ch == 'y'):
                chh = input('\nWhat was your GPA in the course {0}? :- '.format(i))
                c.assert_fact('grade', {'course' : i, 'gpa' : float(chh)})

    @when_all(m.interest == 'Graphics')
    def func(c):

        lst = ['Computer Graphics', 'Introduction to Animation and Graphics', 'Introduction to Motion Graphics']

        for i in lst :

            ch = input('\nHave you done the course {0}? (press y/n) :- '.format(i))
            if (ch == 'y'):
                chh = input('\nWhat was your GPA in the course {0}? :- '.format(i))
                c.assert_fact('grade', {'course' : i, 'gpa' : float(chh)})

    @when_all(m.interest == 'Psychology')
    def func(c):

        lst = ['Cognitive Psychology', 'Social Psychology']

        for i in lst :

            ch = input('\nHave you done the course {0}? (press y/n) :- '.format(i))
            if (ch == 'y'):
                chh = input('\nWhat was your GPA in the course {0}? :- '.format(i))
                c.assert_fact('grade', {'course' : i, 'gpa' : float(chh)})

with ruleset('grade'):

    @when_all((m.course == 'Artificial Intelligence') & (m.gpa >= 7.0))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'AI Engineer'})
        c.assert_fact({'career': 'AI Data Analyst'})
        c.assert_fact({'career': 'Robotic Scientist'})

    @when_all((m.course == 'Machine Learning') & (m.gpa >= 7.5))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'ML Engineer'})
        c.assert_fact({'career': 'ML Data Scientist'})

    @when_all((m.course == 'Natural Language Processing') & (m.gpa >= 7.5))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'NLP Engineer'})
        c.assert_fact({'career': 'NLP Data Scientist'})
    
    @when_all((m.course == 'App Development') & (m.gpa >= 6.5))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'App Developer'})

    @when_all((m.course == 'Web Development') & (m.gpa >= 6.0))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'Front-end Developer'})
        c.assert_fact({'career': 'Back-end Developer'})
        c.assert_fact({'career': 'Full-stack Developer'})

    @when_all((m.course == 'Software Development') & (m.gpa >= 7.0))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'IT Security Specialist '})
        c.assert_fact({'career': 'Software Engineer'})
        c.assert_fact({'career': 'Cloud Engineer'})

    @when_all((m.course == 'Computer Networks') & (m.gpa >= 7.5))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'Network Security Manager'})
        c.assert_fact({'career': 'Network Architect'})
        c.assert_fact({'career': 'System Engineer'})

    @when_all((m.course == 'Network Security') & (m.gpa >= 8.0))
    def func(c):
        print("\n\nCareer options for you :- ")
        c.assert_fact({'career': 'Application Security Engineer'})
        c.assert_fact({'career': 'Malware Analyst'})
        c.assert_fact({'career': 'Cybersecurity Engineer'})

    @when_all((m.course == 'Fundamentals of Database Management Systems') & (m.gpa >= 7.0))
    def func(c):
        print("\n\nCareer options for you :- ")
        c.assert_fact({'career': 'Database Administrator'})

    @when_all((m.course == 'Database System Implementation') & (m.gpa >= 7.0))
    def func(c):
        print("\n\nCareer options for you :- ")
        c.assert_fact({'career': 'Database Manager'})
        c.assert_fact({'career': 'Data Modeler'})

    @when_all((m.course == 'Digital VLSI Design') & (m.gpa >= 6.0))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'Front-end Verification Engineer'})
        c.assert_fact({'career': 'IP Design Engineer'})

    @when_all((m.course == 'Introduction to HCI') & (m.gpa >= 6.5))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'UX Researcher'})
        c.assert_fact({'career': 'Product Manager'})

    @when_all((m.course == 'Money and Banking') & (m.gpa >= 6.0))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'Foreign Exchange Trader'})
        c.assert_fact({'career': 'Budget Analyst'})
        c.assert_fact({'career': 'Bank Manager'})

    @when_all((m.course == 'Macroeconomics') & (m.gpa >= 7.0))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'Supply Chain Analyst'})
        c.assert_fact({'career': 'Economic Consultant'})

    @when_all((m.course == 'Foundations of Finance') & (m.gpa >= 7.0))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'Corporate Finance'})
        c.assert_fact({'career': 'Commercial Banking'})
        c.assert_fact({'career': 'Investment Banking'})

    @when_all((m.course == 'Entrepreneurial Finance') & (m.gpa >= 6.0))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'Senior Attorney'})
        c.assert_fact({'career': 'Financial Services Consultant'})
        c.assert_fact({'career': 'Managing Director'})

    @when_all((m.course == 'Computer Graphics') & (m.gpa >= 7.0))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': '3D Production Artist'})
        c.assert_fact({'career': 'Digital Marketing Specialist'})
        c.assert_fact({'career': 'Graphic Designer'})

    @when_all((m.course == 'Introduction to Animation and Graphics') & (m.gpa >= 7.5))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': '3D Animator'})
        c.assert_fact({'career': 'Video Game Designer'})

    @when_all((m.course == 'Introduction to Motion Graphics') & (m.gpa >= 6.0))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'Video Editors'})
        c.assert_fact({'career': 'Art Directors'})

    @when_all((m.course == 'Cognitive Psychology') & (m.gpa >= 6.0))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'Human Factors Consultant'})
        c.assert_fact({'career': 'Usability Specialist'})

    @when_all((m.course == 'Social Psychology') & (m.gpa >= 5.0))
    def func(c):
        print("\nCareer options for you :- ")
        c.assert_fact({'career': 'Consultant'})

    @when_all(+m.career)
    def output(c):
        print("{0}".format(c.m.career))
       
# the main function
if __name__ == '__main__':

    print("\n\n---------------------------------------------------------------------------------")
    print("\n\n\t\tHey there, Welcome to our carrer advisory system !!")
    print("\n\n---------------------------------------------------------------------------------")
    print("\n\nBefore we begin .. Let's know about you a little. Shall we?")

    intrst = interest()

    print("\n---------------------------------------------------------------------------------")
    
    assert_fact('interest', {'interest' : intrst})