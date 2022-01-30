# Imporing OS for executing the Linux Commands 
import os
#importing getpass for echo back less authentication
import getpass


#from aws import aws
from devops import docker 
#from linux_basic import lvm
#from hadoop import
#from mlops import



#################                Functions             ###################


####################             Credits              ####################
def credits():
    os.system("tput setaf 11")
    print("\t\t\t\t\t\tMade by ARTH2020_03 Gr.17")
    print("\n")
    os.system("tput setaf 7")


###########################################################################


#Username Password Auth Function
def auth():
    os.system("tput setaf 3")
    passwd = getpass.getpass("Enter your Password to login to console:")
    apass = "redhat"
    if passwd != apass:
        print("\n")
        os.system("tput setaf 1")
        print("Incorrect Password! Try Again.....")
    else:
        os.system("tput setaf 2")
        print("Logging to the console")
        credits()

###################################################

def main():
    while True:
        head()
        os.system("tput setaf 2")
        print("\t\t\tWhich service You want to access?")
        os.system("tput setaf 3")
        print('''
            \t\t1.AWS
            \t\t2.Hadoop
            \t\t3.devops
            \t\t4.docker
            \t\t5.Web Server
            \t\t6.Machine Learning
            \t\t7.Basics of Linux
            \t\t8.Exit
            ''')
        os.system("tput setaf 7")
        ch = int(input("What do you want to do:"))	
        if ch==1:
            print("AWS")
            #aws.aws()
            continue    
        elif ch==2:
            #hadoop.hadoop()
            print("Hadoop")
        elif ch==3:
            print("devops")
        elif ch==4:
            print("docker")
            docker.run()
        elif ch==5:
            print("webserver")
        elif ch==6:
            print("machine learning")   
        elif ch==7:            
            print("basic linux")       
        elif ch==8:
            os.system("clear")
            os.system("tput setaf 2")
            print("\t\t\t\tThank You ")
            print("\t\t\tExiting from our system")
            os.system("tput setaf 3")
            print("--------------------------------------------------------------------------------")
            credits()
            input("Press Enter to continue....")
            os.system("tput setaf 7")
            os.system("clear")
            break
        else:
            print("Please enter a valid choice")



#################################

# Heading Display function
def head():
    os.system("clear")
    print("\n\n")
    os.system("tput setaf 1")
    print("\t\t\tHey! Welcome to our System")
    os.system("tput setaf 7")
    print("--------------------------------------------------------------------------------")



###########################


################               Authentication            ######################
head()
auth()
os.system("sleep 1 ")
################               Main functions             ####### #############
main()
os.system("clear")












