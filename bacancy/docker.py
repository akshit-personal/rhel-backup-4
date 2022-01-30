import os


#################                 CONTAINER              ###################
def new_con(name,image):
    os.system("tput setaf 2")
    os.system("docker container run -dit --name {0} {1}".format(name,image)) 
    os.system("tput setaf 7")

def attach_con(name):
    os.system("tput setaf 2")
    os.system("docker container start {}".format(name))
    os.system("docker container attach {}".format(name))
    os.system("tput setaf 7")

def list_run_con():
    os.system("docker container ls")

def list_stop_con():
    os.system("docker container ls -a")

def inspect_con(name):
    os.system("docker container inspect {} ".format(name))

def stop_con(name):
    os.system("tput setaf 1")
    os.system("docker container stop {}".format(name))
    os.system("tput setaf 7")

def rename_con(name,new):
    os.system("docker container rename {0} {1}".format(name,new))

def rm_con(name):
    os.system("tput setaf 1")
    os.system("docker container rm -f {}".format(name))
    os.system("tput setaf 7")

def rm_all_con():
    os.system("tput setaf 1")
    os.system("docker container rm -f $(docker ps -a -q)")
    os.system("tput setaf 7")

def img_con(name,img):
    os.system("docker commit {0} {1} ".format(name,img))

##################                IMAGES            #####################

def pull_img(name):
    os.system("docker pull {}".format(name))
def list_img():
    os.system("docker image ls")
def rm_img(name):
    os.system("tput setaf 1")
    os.system("docker image rm {}".format(name))
    os.system("tput setaf 7")
def inspect_img(name):
    os.system("docker image inspect {}".format(name))
#def push_img(name):
    #os.system("docker image ls")

###################                 NETWORK            ########################

def new_network(network,driver):
    os.system("tput setaf 2")
    os.system("docker network create -d {0} {1} ".format(driver,network))
    os.system("tput setaf 7")
                
def list_network():
    os.system("docker network ls")

def inspect_network(name):
    os.system("docker network inspect {}".format(name))
                
def disconnect_network(name,network):
    os.system("tput setaf 1")
    os.system("docker network disconnect -f {0} {1}".format(network,name))
    os.system("tput setaf 7")
                
def connect_network(name,network):
    os.system("tput setaf 2")
    os.system("docker network connect {0} {1}".format(network,name))
    os.system("tput setaf 7")

def rm_network(network):
    os.system("tput setaf 1")
    os.system("docker network rm {}".format(network))
    os.system("tput setaf 7")



#################                 VOLUME               ######################

def create_vol(vol):
    os.system("tput setaf 2")
    os.system("docker volume create {}".format(vol))
    os.system("tput setaf 7")

def list_vol():
    os.system("docker volume ls")

def inspect_vol(vol):
    os.system("docker volume inspect {}".format(vol))

def rm_vol(vol):
    os.system("tput setaf 1")
    os.system("docker volume rm {}".format(vol))
    os.system("tput setaf 7")




################           MULTI-TIER Architecture         ##################

def multi_tier_architecture():
    os.system("tput setaf 3")
    os.system("docker-compose up -d")



##############            PUSH IMAGE TO DOCKER HUB         #################
def  push_img(img,user_name):
    os.system("tput setaf 2")
    os.system("docker login")
    print("Creating a new image with tag for pushing to docker hub....")
    os.system("docker image tag {0} {1}/{0}".format(img,user_name))
    os.system("docker push {1}/{0}".format(img,user_name))
    os.system("tput setaf 7")




#############################################################################

def menu_style():
        os.system("clear")
        print("\n\n")
        os.system("tput setaf 1")
        print("\t\t\tHey! Welcome to the Docker World")
        os.system("tput setaf 7")



        print("--------------------------------------------------------------------------------")







#############################################################################


n=1
while n>0:
    menu_style()
    os.system("tput setaf 3")
    print('''
        \t\t1.Container
        \t\t2.Images
        \t\t3.Networking
        \t\t4.Volume
        \t\t5.create a multi-tier architecture
        \t\t6.Pull image to docker Hub
        \t\t7.push image to docker hub
        \t\t8.Exit
        ''')
    os.system("tput setaf 7")
###################                CONTAINER             ####################
    ch = input("What do you want to do:")
    if int(ch)==1:
            menu_style()
            os.system("tput setaf 3")
            print('''
                \t1.Create a new container
                \t2.Attach conatainer
                \t3.List all running containers
                \t4.List all stopped containers
                \t5.Inspect container
                \t6.Stop running container
                \t7.Rename container
                \t8.Remove a container
                \t9.Remove all containers
                \t10.Create a new image from a container
                ''')
            os.system("tput setaf 7")
            op=input("Enter your choice:")
            if int(op)==1:
               name=input("Enter name of container\nEg aks\n:") 
               image=input("Enter name of image \nEg.centos:latest\n:")
               new_con(name,image)
            elif int(op)==2:
               name=input("Enter a name of container you want to attach:")
               attach_con(name)
               break
            elif int(op)==3:
                list_run_con()
            elif int(op)==4:
                list_stop_con()
            elif int(op)==5:
                name=input("Enter a container name you want to inspect:")
                inspect_con(name)
            elif int(op)==6:
                name=input("Enter a name of container you want to stop:")
                stop_con(name)
            elif int(op)==7:
                name=input("Enter a name of container you want to rename:")
                new=input("Enter a new name:")
                rename_con(name,new)
            elif int(op)==8:
                name=input("Enter a name of container you want to remove:")
                rm_con(name)
            elif int(op)==9:
                rm_all_con()
            elif int(op)==10:
                name=input("Enter container name:")
                img=input("Enter a name of image you want to make:\nEg.myimage:v1\n:")
                img_con(name,img)
            else:
                print("Please enter a valid option")

######################             IMAGES             #######################


    elif int(ch)==2:
            menu_style()
            os.system("tput setaf 3")
            print('''
                \t1.Pull image from docker hub
                \t2.List all images
                \t3.Remove image
                \t4.Inspect image
                \t5.Create a new image from a container
                \t6.Push image to docker Hub
                ''')
            os.system("tput setaf 7")
            op=input("Enter your choice:")
            if int(op)==1:
                name=input("Enter a image name you want to pull from docker hub:\nEg.centos:latest\n:")
                pull_img(name)
            elif int(op)==2:
                list_img()
            elif int(op)==3:
                name=input("Enter a name of image you want to remove:")
                rm_img(name)
            elif int(op)==4:
                name=input("Enter a name of image you want to inspect:")
                inspect_img(name)
            elif int(op)==5:
                name=input("Enter container name:")
                img=input("Enter a name of image you want to make:\nEg.myimage:v1\n:")
                img_con(name,img)

            elif int(op)==6:
                menu_style()
                img=input("Enter a name of image you want to push:")
                user_name=input("Enter your docker repostory username:")
                push_img(img,user_name)

            else:
                print("Please enter a valid option")


####################                NETWORK          ########################


    elif int(ch)==3:    
            menu_style()
            os.system("tput setaf 3")
            print('''
                \t1.Create a new network
                \t2.List all networks
                \t3.Inspect a network
                \t4.disconnect from a network
                \t5.Connect to a network
                \t6.Remove a network''')
            os.system("tput setaf 7")
            op=input("Enter your choice:")
            if int(op)==1:
                network=input("Enter a name of a network you want to create:")
                driver=input("Enter a name of driver\nEg bridge\n:")
                new_network(network,driver)
            elif int(op)==2:
                list_network()
            elif int(op)==3:
                name=input("Enter a name of network you want to inspect:")
                inspect_network(name)
            elif int(op)==4:
                name=input("Enter name of container you want to disconnect:")
                network=input("Enter network of {} container\nEg.bridge\n:".format(name))
                disconnect_network(name,network)
            elif int(op)==5:
                name=input("Enter name of container you want to connect:")
                network=input("Which network you want to connet\nEg.bridge\n:")
                connect_network(name,network)
            elif int(op)==6:
                network=input("Enter a name of network you want to remove:")
                rm_network(network)
            else:
                print("Please enter a valid choice")


#################                 VOLUME               ######################


             
    elif int(ch)==4:
            menu_style()
            os.system("tput setaf 3")

            print('''
                \t1.Create a new volume
                \t2.List all volumes
                \t3.Inspect a volume
                \t4.Remove a volume''')
            os.system("tput setaf 7")
            op=input("Enter your choice:")
            if int(op)==1:
                vol=input("Enter a name of volume you want to create:")
                create_vol(vol)
            elif int(op)==2:
                list_vol()
            elif int(op)==3:
                vol=input("Enter a name of volume you want to inspect:")
                inspect_vol(vol)
            elif int(op)==4:
                vol=input("Enter a name of volume you want to remove:")
                rm_vol(vol)
            else:
                print("Please enter a valid choice")



################           MULTI-TIER Architecture         ##################

            
    elif int(ch)==5:
            menu_style()
            os.system("tput setaf 3")
            print('''
                1.Create a Multi-tier architecure of phpmyadmin-mysql
                ''')
            os.system("tput setaf 3")
            multi_tier_architecture()
            os.system("tput setaf 7")


###################     Pull image from DOCKER HUB        ######################



    elif int(ch)==6:
        name=input("Enter a image name you want to pull from docker hub:\nEg.centos:latest\n:")
        pull_img(name)



##############            PUSH IMAGE TO DOCKER HUB         ################


    elif int(ch)==7:
        menu_style()
        img=input("Enter a name of image you want to push:")
        user_name=input("Enter your docker repostory username:")
        push_img(img,user_name)


###################                EXIT              #######################


    elif int(ch)==8:
        os.system("clear")
        os.system("tput setaf 2")
        print("\t\t\t\tThank You ")
        print("\t\t\tExiting from Docker World")
        os.system("tput setaf 3")
        print("--------------------------------------------------------------------------------")

        input("Press Enter to continue....")
        os.system("tput setaf 7")
        os.system("clear")
        break
    else:
        print("Please enter a valid choice")
    input("Press Enter to continue....")
    os.system("clear")
