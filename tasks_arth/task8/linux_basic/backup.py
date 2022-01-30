import os
####################             Credits              ####################

def credits():
    os.system("tput setaf 11")
    print("\t\t\t\t\t\t\t\t\t\t\t    Made by ARTH2020_03 Gr.17")
    print("\t\t\t\t\t\t\t\t\t\t\t Akshit Modi, kodgire Ashutosh")
    print("\t\t\t\t\t\t\t\t\t  Janhavi Jain,Gursimar Singh, Sourav Pattnaik")
    os.system("tput setaf 7")

#######################        functions          #######################
#######################        local           ########################
###########################    disk detail         #############
#1
def disk_detail():
    cmd = "sudo fisk -l"
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

##################             create vg         ##################
#2
def create_vg(device_name,vname):
    cmd = "sudo vgcreate {1} /dev/{0}".format(device_name,vname)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Volume group {} created successfully".format(vname))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

##################          Extend  vg        #####################
#3
def extend_vg(device_name,vname):
    cmd = "sudo vgextend {1} /dev/{0}".format(device_name,vname)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

#################      display vg       ################
#4
def display_vg(vname):
    cmd = "sudo vgdisplay {}".format(vname)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("Volume group {}:".format(vname))
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

#################      display all vg       ################
#5
def display_all_vg():
    cmd = "sudo vgdisplay"
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("All volume group:")
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

################          remove  vg        #####################
#6
def remove_vg(vname):
    cmd = "sudo vgremove {} ".format(vname)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Volume group {} removed".format(vname))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

###################         create logical volume   ####################
#7
def create_lvm(size,vname,lname):
    cmd = "sudo lvcreate --size {2} --name {1} {0}".format(vname,lname,size)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("LVM {} created successfully".format(lname))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

###################          format - mount lvm              #################
#8
def format_lvm(lname,vname):
    cmd = "sudo mkfs.ext4 /dev/{1}/{0}".format(lname,vname)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 2")
        print("LVM formated to mkfs.ext4 format, mounting to the folder...")
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
##
def mount_lvm(lname,vname,fname):
    cmd = "sudo mkdir /{}".format(fname)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 2")
        print("Folder already exists, mounting there...")
        os.system("tput setaf 7")


    cmd2 = "sudo mount /dev/{2}/{1} /{0}".format(fname,lname,vname)
    ans2 = sp.getstatusoutput(cmd2)
    if ans2[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 2")
        print("LVM mounted to {} folder".format(fname))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

##################                  display lvm        ###############
#9
def display_lvm(lname,vname):
    cmd = "sudo lvdisplay /dev/{1}/{0}".format(lname,vname)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("LVM {}:".format(lname))
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

##################                  display all lvm        ###############
#10
def display_all_lvm(lname,vname):
    cmd = "sudo lvdisplay"
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("All LVM:")
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

####################              Extend lvm             #################
#11
def extend_lvm(lname,vname,size):
    cmd = "sudo lvextend --size {2} /dev/{1}/{0}".format(lname,vname,size)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("{0} added to the {1} LVM".format(size,lname))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

###########################################################################
######################             remote           #####################
#######################################################################

###########################    disk detail         #############
#1
def ssh_disk_detail():
    cmd = "sshpass -p {2} ssh {1}@{0} sudo fdisk -l".format(ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

##################             create vg         #################
#2
def ssh_create_vg(device_name,vname):
    cmd = "sshpass -p {4} ssh {3}@{2} sudo vgcreate {1} /dev/{0}".format(device_name,vname,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Volume group {} created successfully".format(vname))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")


##################          Extend  vg        #####################
#3
def ssh_extend_vg(device_name,vname):
    cmd = "sshpass -p {4} ssh {3}@{2} sudo vgextend {1} /dev/{0}".format(device_name,vname,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

#################      display vg       ################
#4
def ssh_display_vg(vname):
    cmd = "sshpass -p {3} ssh {2}@{1} sudo vgdisplay {0}".format(vname,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("Volume group {}:".format(vname))
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

#################      display all vg       ################
#5
def ssh_display_all_vg():
    cmd = "sshpass -p {2} ssh {1}@{0} sudo vgdisplay".format(ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("All volume group:")
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

##################          remove  vg        #####################
#6
def ssh_remove_vg(vname):
    cmd = "sshpass -p {3} ssh {2}@{1} sudo vgextend {0}".format(vname,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Volume group {} removed".format(vname))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

###################         create logical volume   ####################
#7
def ssh_create_lvm(size,vname,lname):
    cmd = "sshpass -p {5} ssh {4}@{3} sudo lvcreate --size {2} --name {1} {0}".format(vname,lname,size,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("LVM {} created successfully".format(lname))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")


###################           format -mount lvm              #################
#8
def ssh_format_lvm(lname,vname):
    cmd = "sshpass -p {4} ssh {3}@{2} sudo mkfs.ext4 /dev/{1}/{0}".format(lname,vname,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 2")
        print("LVM formated to mkfs.ext4 format, mounting to the folder...")
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
##
def ssh_mount_lvm(lname,vname,fname):
    cmd = "sshpass -p {3} ssh {2}@{1} sudo mkdir /{0}".format(fname,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 2")
        print("Folder already exists, mounting there...")
        os.system("tput setaf 7")

    cmd2 = "sshpass -p {5} ssh {4}@{3} sudo mount /dev/{2}/{1} /{0}".format(fname,lname,vname,ip,user,passwd)
    ans2 = sp.getstatusoutput(cmd2)
    if ans2[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        os.system("tput setaf 2")
        print("LVM mounted to {} folder".format(fname))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
##################                  display lvm        ###############
#9
def ssh_display_lvm(lname,vname):
    cmd = "sshpass -p {4} ssh {3}@{2} sudo lvdisplay /dev/{1}/{0}".format(lname,vname,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("LVM {}:".format(lname))
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

##################                  display all lvm        ###############
#10
def ssh_display_all_lvm(lname,vname):
    cmd = "sshpass -p {2} ssh {1}@{0} sudo lvdisplay".format(ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("All LVM:")
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

####################              Extend lvm             #################
#11
def ssh_extend_lvm(lname,vname,size):
    cmd = "sshpass -p {5} ssh {4}@{3} sudo lvextend --size {2} /dev/{1}/{0}".format(lname,vname,size,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("{0} added to the {1} LVM".format(size,lname))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

############################
def menu_style():
        os.system("clear")
        print("\n")
        os.system("tput setaf 2")
        print("\t\t\t\t\t\tWelcome to LVM console")
        os.system("tput setaf 7")
        print("----------------------------------------------------------------------------------------------------------------------")
#######################

def menu():
    menu_style()
    os.system("tput setaf 3")
    print('''
        \t\t\t\t1.See all disk details
        \t\t\t\t2.Create Volume Group(VG)
        \t\t\t\t3.Add more space to VG
        \t\t\t\t4.Display VG
        \t\t\t\t5.Display all VG
        \t\t\t\t6.Remove VG
        \t\t\t\t7.Crete logical volume
        \t\t\t\t8.Format and Mount partition
        \t\t\t\t9.Diplay lvm
        \t\t\t\t10.Display all lvm
        \t\t\t\t11.Extend lvm size
        \t\t\t\t12.Exit
        ''')
    os.system("tput setaf 7")
    global ch
    ch = int(input("What do you want to do:"))

################################################
def exited():
    os.system("clear")
    os.system("tput setaf 2")
    print("\t\t\t\t\t\t\tThank You ")
    print("\t\t\t\t\t\tExiting from LVM console")
    os.system("tput setaf 3")
    print("----------------------------------------------------------------------------------------------------------------------")
    credits()
    os.system("tput setaf 3")
    input("Press Enter to continue....")
    os.system("tput setaf 7")
    os.system("clear")


#############################
def run(loc,ip12,user12,passwd12):
    global user
    global passwd
    global ip
    user=user12
    passwd=passwd12
    ip=ip12
    n=1
    if loc=="l":
        os.system("tput setaf 2")
        print("Installing lvm dependencies...")
        os.system("dnf install lvm2-8:2.03.02-6.el8.x86_64")
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 2")
        print("Installing lvm dependencies...")
        os.system("sshpass -p {2} ssh {1}@{0} dnf install lvm2-8:2.03.02-6.el8.x86_64".format(ip,user,passwd))
        os.system("tput setaf 7")
    while n>0:
        if loc=="l":
            menu()
            if ch==1:
                disk_detail()
            elif ch==2:
                vname=input("Enter new Volume Group name:")
                device_name=input("Enter device name (Eg. xvdh):")
                create_vg(device_name,vname)
            elif ch==3:
                vname=input("Enter VG name:")
                device_name=input("Enter device name - space you want to add (Eg. xvdh):")
                extend_vg(device_name,vname)
            elif ch==4:
                vname=input("Enter name of your VG:")
                display_vg(vname)
            elif ch==5:
                display_all_vg()
            elif ch==6:
                vname=input("Enter VG name:")
                remove_vg(vname)
            elif ch==7:
                lname=input("Enter name of lvm you want to give:")
                size=input("How much size of lvm you want to add? (Eg. 50MB):")
                vname=input("From which vg you want to get space:")
                create_lvm(size,vname,lname)
            elif ch==8:
                lname=input("Enter name of lvm:")
                vname=input("Which VG lvm belongs to:")
                fname=input("Enter folder name where you want to mount:")
                format_lvm(lname,vname)
                mount_lvm(lname,vname,fname)
            elif ch==9:
                lname=input("Enter name of lvm:")
                vname=input("Which VG lvm belongs to:")
                display_lvm(lname,vname)
            elif ch==10:
                display_all_lvm()
            elif ch==11:
                size=input("How much size you want to add:")
                lname=input("Enter name of lvm:")
                vname=input("Which VG lvm belongs to:")
                extend_lvm(lname,vname,size)
            elif ch==12:
                exited()
                break
            else:
                os.system("tput setaf 1")
                print("Please enter a valid option")
                os.system("tput setaf 3")
                input("Press enter to show menu again")
                menu()
            input("Press Enter to continue....")
            os.system("clear")

        else:
            menu()
            if ch==1:
                ssh_disk_detail()
            elif ch==2:
                vname=input("Enter new Volume Group name:")
                device_name=input("Enter device name (Eg. xvdh)")
            elif ch==3:
                vname=input("Enter VG name:")
                device_name=input("Enter device name - space you want to add (Eg. xvdh):")
                ssh_extend_vg(device_name,vname)
            elif ch==4:
                vname=input("Enter name of VG:")
                display_vg(vname)
            elif ch==5:
                ssh_display_all_vg()
            elif ch==6:
                vname=input("Enter VG name:")
                ssh_remove_vg(vname)
            elif ch==7:
                lname=input("Enter name of lvm you want to give:")
                size=input("How much size of lvm you want to add? (Eg. 50MB):")
                vname=input("From which vg you want to get space:")
                ssh_create_lvm(size,vname,lname)
            elif ch==8:
                lname=input("Enter name of lvm:")
                vname=input("Which VG lvm belongs to:")
                fname=input("Enter folder name where you want to mount:")
                ssh_format_lvm(lname,vname)
                ssh_mount_lvm(lname,vname,fname)
            elif ch==9:
                lname=input("Enter name of lvm:")
                vname=input("Which VG lvm belongs to:")
                ssh_display_lvm(lname,vname)
            elif ch==10:
                ssh_display_all_lvm()
            elif ch==11:
                size=input("How much size you want to add:")
                lname=input("Enter name of lvm:")
                vname=input("Which VG lvm belongs to:")
                ssh_extend_lvm(lname,vname,size)
            elif ch==12:
                exited()
                break
            else:
                os.system("tput setaf 1")
                print("Please enter a valid option")
                os.system("tput setaf 3")
                input("Press enter to show menu again")
                menu()
            input("Press Enter to continue....")
            os.system("clear")

