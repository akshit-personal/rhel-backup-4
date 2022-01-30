import os
import subprocess as sp
###########################
def credits():
    os.system("tput setaf 11")
    print("\t\t\t\t\t\t\t\t\t\t\t    Made by ARTH2020_03 Gr.17")
    print("\t\t\t\t\t\t\t\t\t\t\t Akshit Modi, kodgire Ashutosh")
    print("\t\t\t\t\t\t\t\t\t  Janhavi Jain,Gursimar Singh, Sourav Pattnaik")
    os.system("tput setaf 7")

####################################
def install_aws_cli():
    os.system("tput setaf 3")
    print("Downloading latest CLI version...")
    cmd = "sudo curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip"
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        print("Unzipping file...")
        cmd2 = "sudo unzip awscliv2.zip"
        ans2 = sp.getstatusoutput(cmd2)
        if ans2[0] == 0:
            print("Installing CLI...")
            cmd3 = "sudo ./aws/install"
            ans3 = sp.getstatusoutput(cmd3)
            if ans3[0]==0:
                print("Successfully installed latest version of AWS CLI")
            else:
                os.system("sudo tput setaf 1")
                print("Some error occured... Can not start docker service")
                os.system("sudo tput setaf 7")	
        else:
            os.system("sudo tput setaf 1")
            print("Some error occured... Can not start docker service")
            os.system("sudo tput setaf 7")
    else:
        os.system("sudo tput setaf 1")
        print("Some error occured... Can not start docker service")
        os.system("sudo tput setaf 7")

#################################
def config():
    os.system("tput setaf 3")
    print("aws configured")
    os.system("tput setaf 7")




#####################################
def launch_ec2(ami,itype,count,subnet,sg,key):
    cmd = "sudo aws ec2 run-instances --image-id {0} --instance-type {1} --count {2} --subnet-id {3} --security-group-ids {4} --key-name {5}".format(ami,itype,count,subnet,sg,key)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 2")
        print("Launching instance...")
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")


######################
def create_sg(sg):
    cmd = "sudo aws ec2 create-security-group --group-name {}".format(sg)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 2")
        print("Security group created Successfully")
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

#####################
def create_key(key): 
    cmd = "sudo aws ec2 create-key-pair --key-name {}".format(key)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 2")
        print("Key created succesfully")
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

#######################
def launch_ebs(az,vt,size):
    cmd = "sudo aws ec2 create-volume --availability-zone {0} --volume-type {1} --size {}".format(az,vt,size)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 2")
        print("EBS Volume Launched Successfully")
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")




    #######################
def attach_ebs_to_ec2(vi,iid,device_name):
    cmd = "sudo aws ec2 attach-volume  --volume-id {0}  --instance-id {1} --device {2}".format(vi,iid,device_name)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 2")
        print("EBS Volume Attached Successfully")
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")


##########################
def launch_s3(bn):
    cmd = "sudo aws s3 mb s3://{}".format(bn)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 2")
        print("S3 Bucket Created Successfully")
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

#############
def list_all_s3_bucket(bn):
    cmd = "sudo aws s3 ls s3://{}".format(bn)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 2")
        print("All s3 buckets")
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

##############
def create_cloudfront(bn,image):
    cmd = "sudo aws cloudfront create-distribution --origin-domain-name {0}.s3.amazonaws.com --default-root-object {1}".format(vb,image)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 2")
        print("Cloud Front Distribution Created Successfully")
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

##########################################
def menu_style():
    os.system("clear")
    print("\n")
    os.system("tput setaf 2")
    print("\t\t\t\t\t\tWelcome to AWS console")
    os.system("tput setaf 7")
    print("----------------------------------------------------------------------------------------------------------------------")

############################################

def menu():
    menu_style()
    os.system("tput setaf 3")
    print('''
        \t\t\t\t1: Install latest AWS CLI
        \t\t\t\t2: Configure system
        \t\t\t\t3: To Launch EC2 Instance
        \t\t\t\t4: To Create Security Group
        \t\t\t\t5: To Create Key Pair
        \t\t\t\t6: To Launch EBS Volume
        \t\t\t\t7: To Attach EBS Volume With EC2 Instance
        \t\t\t\t8: To Launched S3 Buckets
        \t\t\t\t9: To List S3 Buckets
        \t\t\t\t10: To Create Cloud Front Distribution
        \t\t\t\t11: To Exit
        ''')
    os.system("tput setaf 7")
    global ch
    ch = int(input("What do you want to do:"))
#############################################

def run():
    global user
    global passwd
    n=1
    while n>0:
        menu()
        if ch==1:
            install_aws_cli()
        elif ch==2:
            
            config()
        elif ch==3:
            os.system("tput setaf 6")
            ami=input("Enter AMI (Eg):") 
            itype=input("Enter type  of Instance (Eg):")
            count=input("ENter number of instances:(Eg 1)")
            subnet=input("Enter Subnet ID:")
            sg=input("Enter Security group ID:")
            key=input("Enter your key Pair name:")
            launch_ec2(ami,itype,count,subnet,sg,key)
        elif ch==4:
            sg=input("Enter Security Group name:")
            create_sg(sg)
        elif ch==5:
            key=input("Enter key name:")
            create_key(key)
        elif ch==6:
            vt=input("Enter volume type:")
            size=input("Enter size of volume:")
            az=input("Enter availability zone:")
            launch_ebs(az,vt,count)
        elif ch==7:
            vi = input("Enter Your EBS Volume ID :")
            iid = input("Enter Your Instance ID :")
            device_name = input("Enter Your Device Name /dev/.. :")
            attach_ebs_to_ec2(vi,iid,device_name)
        elif ch==8:
            bn=input("Enter your bucket name:")
            launch_s3(bn)
        elif ch==9:
            bn=input("Enter your bucket name:")
            list_all_s3_bucket(bn)
        elif ch==10:
            bn=input("Enter your bucket name:")
            image = ("Enter Image Name :")
            create_cloudfront(bn,image)
        elif ch==11:
            os.system("clear")
            os.system("tput setaf 2")
            print("\t\t\t\t\t\t\tThank You ")
            print("\t\t\t\t\t\tExiting from AWS console")
            os.system("tput setaf 3")
            print("----------------------------------------------------------------------------------------------------------------------")
            credits()
            os.system("tput setaf 3")
            input("Press Enter to continue....")
            os.system("tput setaf 7")
            os.system("clear")
            break
        else:
            print("Please enter a valid choice")
        input("Press enter to continue...")
        os.system("clear")


