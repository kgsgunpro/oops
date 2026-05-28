#facebook like project
class Chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input=input('welcome to chatbook \n' \
        '1.press 1 to signup \n' \
        '2. press 2 to signin \n' \
        '3. press 3 to write a post \n' \
        '4. press 4 to message a friend \n' \
        '5. press any other key to exit \n')
        if user_input == '1' :
            self.signup()
        elif user_input == '2' :
            self.signin()
        elif user_input == '3' :
            self.my_post()
        elif user_input == '4' :
            self.send_msg()
        else :
            exit()
    
    def signup(self):
        email = input('enter your email : ')
        passw = input('enter your password')
        self.username= email
        self.password = passw
        print('You have signed up successfully! \n ')
        self.menu()
    
    def signin(self):
        if self.username =='' and self.password=='' :
            print('please sign up')
        else:
            email = input('enter your email : ')
            passw = input('enter your password')
            if self.username==email and self.password ==passw :
                print('successfully logged in')
                self.loggedin =True
            else:
                print('incorrect credentials')
        print('\n')        
        self.menu()


    def my_post(self):
        if self.loggedin==True:
            txt = input('Whats on your mind ?')
            print('Following content has been posted ' , txt)
        else :
            print('you need to sign in first \n')
            self.menu()

    def send_msg(self):
        if self.loggedin == True :
            txt = input('Enter msg to send ')
            frnd = input('whom to send')
            print('Your messege sent to ' , frnd)
        else:
            print('please sign in \n')
        self.menu()








        
obj = Chatbook()


