import os
import subprocess as sp
####################             Credits              ####################
def credits():
    os.system("sudo tput setaf 11")
    print("\t\t\t\t\t\t\t\t\t\t\t    Made by ARTH2020_03 Gr.17")
    print("\t\t\t\t\t\t\t\t\t\t\t Akshit Modi")
    os.system("sudo tput setaf 7")

##############################################################################################################
####################################         local                  ##########################################
##############################################################################################################

##################          services start -stop        ###################
#start
def start_docker():
    os.system("sudo tput setaf 3")
    print("Starting docker services...")
    cmd = "sudo systemctl start docker"
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        cmd2 = "sudo systemctl enable docker"
        ans2 = sp.getstatusoutput(cmd2)
        if ans2[0] == 0:
            print("Docker services are permanently started")
    else:
        os.system("sudo tput setaf 1")
        print("Some error occured... Can not start docker service")
    os.system("sudo tput setaf 7")
#stop
def stop_docker():
    os.system("sudo tput setaf 3")
    print("Stopping docker services...")
    cmd = "sudo systemctl stop docker"
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        cmd2 = "sudo systemctl disable docker"
        ans2 = sp.getstatusoutput(cmd2)
        if ans2[0] == 0:
            print("Docker services are permanently stopped")
    else:
        os.system("sudo tput setaf 1")
        print("Some error occured... Can not stop docker service")
    os.system("sudo tput setaf 7")


#################                 CONTAINER              ###################
#1
def new_con(name,image):
    os.system("sudo tput setaf 3")
    cmd = "sudo docker container run -dit --name {0} {1}".format(name,image)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        print(ans[1])
        print("New container {} launched successfully".format(name))
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
    os.system("sudo tput setaf 7")
#2
def start_con(name):
    os.system("sudo tput setaf 3")
    cmd = "sudo docker container start {}".format(name)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        print("Container {} started successfully".format(name))
        print(ans[1])
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
    os.system("sudo tput setaf 7")
#3
def list_run_con():
    cmd = "sudo docker container ls"
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("All running containers:")
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#4
def list_stop_con():
    cmd = "sudo docker container ls -a"
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("All containers:")
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#5
def inspect_con(name):
    cmd = "sudo docker container inspect {} ".format(name)
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
#6
def stop_con(name):
    cmd = "sudo docker container stop {}".format(name)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Container {} stopped successfully".format(name))
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
    os.system("sudo tput setaf 7")
#7
def rename_con(name,new):
    cmd = "sudo docker container rename {0} {1}".format(name,new)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Container {1} renamed to {0}".format(new,name))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#8
def rm_con(name):
    os.system("sudo tput setaf 1")
    cmd = "sudo docker container rm -f {}".format(name)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Container {} removed successfully".format(name))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#9
def rm_all_con():
    cmd = "sudo docker container rm -f $(docker ps -a -q)"
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("All containers are removed")
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#10
def img_con(name,img):
    cmd = "sudo docker commit {0} {1} ".format(name,img)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 2")
        print(ans[1])
        print("Image {} successfully created".format(img))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")


##################                IMAGES            #####################
#1
def pull_img(name):
    cmd = "sudo docker pull {}".format(name)
    os.system("tput setaf 2")
    print("Please wait...")
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Image {} pulled successfully".format(name))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#2
def list_img():
    cmd = "sudo docker image ls"
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("All images:")
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

#3
def rm_img(name):
    cmd = "sudo docker image rm {}".format(name)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Image {} removed".format(name))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#4
def inspect_img(name):
    cmd = "sudo docker image inspect {}".format(name)
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


###################                 NETWORK            ########################
#1
def new_network(network,driver):
    cmd = "sudo docker network create -d {0} {1} ".format(driver,network)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("New network {0} created with driver {1}".format(network,driver))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#2
def list_network():
    cmd = "sudo docker network ls"
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("All networks:")
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

#3
def inspect_network(name):
    cmd = "sudo docker network inspect {}".format(name)
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

#4
def disconnect_network(name,network):
    cmd = "sudo docker network disconnect -f {0} {1}".format(network,name)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Container {0} disconnected from network {1}".format(name,network))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#5
def connect_network(name,network):
    cmd = "sudo docker network connect {0} {1}".format(network,name)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Container {0} connected to {1} network".format(name,network))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

#6
def rm_network(network):
    cmd = "sudo docker network rm {}".format(network)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Network {} removed".format(network))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")



#################                 VOLUME               ######################
#1
def create_vol(vol):
    cmd = "sudo docker volume create {}".format(vol)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("New volume {} created".format(vol))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

#2
def list_vol():
    cmd = "sudo docker volume ls"
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("All volumes:")
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

#3
def inspect_vol(vol):
    cmd = "sudo docker volume inspect {}".format(vol)
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

#4
def rm_vol(vol):
    cmd = "sudo docker volume rm {}".format(vol)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Volume {} removed".format(vol))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")


################           MULTI-TIER Architecture         ##################

def multi_tier_architecture():
    cmd = "sudo docker-compose up -d"
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



##############            PUSH IMAGE TO DOCKER HUB         #################

def push_img(img,user_name):
    os.system("tput setaf 2")
    cmd = "sudo docker login"
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        print(ans[1])
        os.system("tput setaf 3")
        print("Creating a new image with tag for pushing to docker hub....")
        os.system("tput setaf 2")
        cmd2 = "sudo docker image tag {0} {1}/{0}".format(img,user_name)
        ans2 = sp.getstatusoutput(cmd2)
        if ans2[0] == 0:
            print(ans2[1])
            print("New image {1}/{0} created".format(img,user_name))
            cmd3 = "sudo docker push {1}/{0}".format(img,user_name)
            ans3 = sp.getstatusoutput(cmd3)
            if ans3[0] == 0:
                os.system("tput setaf 3")
                print("Image {1}/{0} pushed to docker hub".format(img,user_name))
                os.system("tput setaf 7")
            else:
                os.system("tput setaf 1")
                print("Some error occured...")
                print(ans3[1])
                os.system("tput setaf 7")
        else:
            os.system("tput setaf 1")
            print("Some error occured...")
            print(ans[1])
            os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")

##############################################################################################################
########################################           remote              #######################################
##############################################################################################################

##################          services start -stop        ###################
#start
def ssh_start_docker(ip):
    os.system("sudo tput setaf 3")
    print("Starting docker services in remote host...")
    cmd ="sshpass -p {2} ssh {1}@{0} sudo systemctl start docker".format(ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        cmd2 = "sshpass -p {2} ssh {1}@{0} sudo systemctl enable docker".format(ip,user,passwd)
        ans2 = sp.getstatusoutput(cmd2)
        if ans2[0] == 0:
            print("Docker services are permanently started in remote host")
            os.system("sudo tput setaf 7")
    else:
        os.system("sudo tput setaf 1")
        print("Some error occured... Can not start docker service in remote host")
        os.system("sudo tput setaf 7")
#stop
def ssh_stop_docker(ip):
    os.system("sudo tput setaf 3")
    print("Stopping docker services in remote host...")
    cmd = "sshpass -p {2} ssh {1}@{0} sudo systemctl stop docker".format(ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        cmd2 = "sshpass -p {2} ssh {1}@{0} sudo systemcyl disable docker".format(ip,user,passwd)
        ans2 = sp.getstatusoutput(cmd2)
        if ans2[0] == 0:
            print("Docker services are permanently stopped in remote host")
            os.system("sudo tput setaf 7")
    else:
        os.system("sudo tput setaf 1")
        print("Some error occured... Can not stop docker service in remote host")
        os.system("sudo tput setaf 7")


#################                 CONTAINER              ###################
#1
def ssh_new_con(name,image,ip):
    os.system("sudo tput setaf 3")
    cmd = "sshpass -p {4} ssh {3}@{2} sudo docker container run -dit --name {0} {1}".format(name,image,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        print(ans[1])
        print("New container {} launched successfully in remote host".format(name))
        os.system("sudo tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("sudo tput setaf 7")
#2
def ssh_start_con(name,ip):
    os.system("sudo tput setaf 3")
    cmd = "sshpass -p {3} ssh {2}@{1} sudo docker container start {0}".format(name,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        print("Container {} started successfully in remote host".format(name))
        print(ans[1])
        os.system("sudo tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("sudo tput setaf 7")
#3
def ssh_list_run_con(ip):
    cmd = "sshpass -p {2} ssh {1}@{0} sudo docker container ls".format(ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("All running containers:")
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#4
def ssh_list_stop_con(ip):
    cmd = "sshpass -p {2} ssh {1}@{0} sudo docker container ls -a".format(ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("All containers:")
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#5
def ssh_inspect_con(name,ip):
    cmd = "sshpass -p {3} ssh {2}@{1} sudo docker container inspect {0} ".format(name,ip,user,passwd)
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
#6
def ssh_stop_con(name,ip):
    cmd = "sshpass -p {3} ssh {2}@{1} sudo docker container stop {0}".format(name,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Container {} stopped successfully".format(name))
        os.system("sudo tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("sudo tput setaf 7")
#7
def ssh_rename_con(name,new,ip):
    cmd = "sshpass -p {4} ssh {3}@{2} sudo docker container rename {0} {1}".format(name,new,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Container {1} renamed to {0}".format(new,name))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#8
def ssh_rm_con(name,ip):
    cmd = "sshpass -p {3} ssh {2}@{1} sudo docker container rm -f {0}".format(name,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Container {} removed successfully".format(name))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#9
def ssh_rm_all_con(ip):
    cmd = "sshpass -p {2} ssh {1}@{0} sudo docker container rm -f $(sshpass -p {2} ssh {1}@{0} docker ps -a -q)".format(ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("All containers are removed")
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#10
def ssh_img_con(name,img,ip):
    cmd = "sshpass -p {4} ssh {3}@{2} sudo docker commit {0} {1} ".format(name,img,ip,userpasswd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 2")
        print(ans[1])
        print("Image {} successfully created".format(img))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")


##################                IMAGES            #####################
#1
def ssh_pull_img(name,ip):
    cmd = "sshpass -p {3} ssh {2}@{1} sudo docker pull {0}".format(name,ip,user,passwd)
    os.system("tput setaf 2")
    print("Please wait...")
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Image {} pulled successfully".format(name))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#2
def ssh_list_img(ip):
    cmd = "sshpass -p {2} ssh {1}@{0} sudo docker image ls".format(ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("All images:")
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#3
def ssh_rm_img(name,ip):
    cmd = "sshpass -p {3} ssh {2}@{1} sudo docker image rm {0}".format(name,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Image {} removed".format(name))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#4
def ssh_inspect_img(name,ip):
    cmd = "sshpass -p {3} ssh {2}@{1} sudo docker image inspect {0}".format(name,ip,user,passwd)
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


###################                 NETWORK            ########################
#1
def ssh_new_network(network,driver,ip):
    cmd = "sshpass -p {4} ssh {3}@{2} sudo docker network create -d {0} {1} ".format(driver,network,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("New network {0} created with driver {1}".format(network,driver))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#2                
def ssh_list_network(ip):
    cmd = "sshpass -p {2} ssh {1}@{0} sudo docker network ls".format(ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("All networks:")
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#3
def ssh_inspect_network(name,ip):
    cmd = "sshpass -p {3} ssh {2}@{1} sudo docker network inspect {0}".format(name,ip,user,passwd)
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
#4              
def ssh_disconnect_network(name,network,ip):
    cmd = "sshpass -p {4} ssh {3}@{2} sudo docker network disconnect -f {0} {1}".format(network,name,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Container {0} disconnected from network {1}".format(name,network))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#5                
def ssh_connect_network(name,network,ip):
    cmd = "sshpass -p {4} ssh {3}@{2} sudo docker network connect {0} {1}".format(network,name,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Container {0} connected to {1} network".format(name,network))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#6
def ssh_rm_network(network,ip):
    cmd = "sshpass -p {3} ssh {2}@{1} sudo docker network rm {0}".format(network,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Network {} removed".format(network))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")


#################                 VOLUME               ######################
#1
def ssh_create_vol(vol,ip):
    cmd = "sshpass -p {3} ssh {2}@{1} sudo docker volume create {0}".format(vol,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("New volume {} created".format(vol))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#2
def ssh_list_vol(ip):
    cmd = "sshpass -p {2} ssh {1}@{0} sudo docker volume ls".format(ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print("All volumes:")
        os.system("tput setaf 2")
        print(ans[1])
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")
#3
def ssh_inspect_vol(vol,ip):
    cmd = "sshpass -p {3} ssh {2}@{1} sudo docker volume inspect {0}".format(vol,ip,user,passwd)
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
#4
def ssh_rm_vol(vol,ip):
    cmd = "sshpass -p {3} ssh {2}@{1} sudo docker volume rm {0}".format(vol,ip,user,passwd)
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        os.system("tput setaf 3")
        print(ans[1])
        print("Volume {} removed".format(vol))
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")


################           MULTI-TIER Architecture         ##################

def ssh_multi_tier_architecture(ip):
    cmd = "sshpass -p {2} ssh {1}@{0} sudo docker-compose up -d".format(ip,user,passwd)
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


##############            PUSH IMAGE TO DOCKER HUB         #################

def ssh_push_img(img,user_name,ip):
    os.system("sudo tput setaf 2")
    cmd = "sudo docker login"
    ans = sp.getstatusoutput(cmd)
    if ans[0] == 0:
        print(ans[1])
        os.system("tput setaf 3")
        print("Creating a new image with tag for pushing to docker hub....")
        os.system("tput setaf 2")
        cmd2 = "sshpass -p {4} ssh {3}@{2} sudo docker image tag {0} {1}/{0}".format(img,user_name,ip,user,passwd)
        ans2 = sp.getstatusoutput(cmd2)
        if ans2[0] == 0:
            print(ans2[1])
            print("New image {1}/{0} created".format(img,user_name))
            cmd3 = "sshpass -p {4} ssh {3}@{2} sudo docker push {1}/{0}".format(img,user_name,ip,user,passwd)
            ans3 = sp.getstatusoutput(cmd3)
            if ans3[0] == 0:
                os.system("tput setaf 3")
                print("Image {1}/{0} pushed to docker hub".format(img,user_name))
                os.system("tput setaf 7")
            else:
                os.system("tput setaf 1")
                print("Some error occured...")
                print(ans3[1])
                os.system("tput setaf 7")
        else:
            os.system("tput setaf 1")
            print("Some error occured...")
            print(ans[1])
            os.system("tput setaf 7")
    else:
        os.system("tput setaf 1")
        print("Some error occured...")
        print(ans[1])
        os.system("tput setaf 7")



#############################################################################

def menu_style():
    os.system("clear")
    print("\n")
    os.system("tput setaf 2")
    print("\t\t\t\t\t\tWelcome to docker console")
    os.system("tput setaf 7") 
    print("----------------------------------------------------------------------------------------------------------------------")

#######################

def exited():
    os.system("clear")
    os.system("tput setaf 2")
    print("\t\t\t\t\t\t\tThank You ")
    print("\t\t\t\t\t\tExiting from Docker console")
    os.system("tput setaf 3")
    print("----------------------------------------------------------------------------------------------------------------------")

    credits()
    os.system("tput setaf 3")
    input("Press Enter to continue....")
    os.system("tput setaf 7")
    os.system("clear")

##############

def menu():
    menu_style()
    os.system("tput setaf 3")
    print('''
        \t\t\t\t1.Start docker service
        \t\t\t\t2.Stop docker service
        \t\t\t\t3.Container
        \t\t\t\t4.Images
        \t\t\t\t5.Networking
        \t\t\t\t6.Volume
        \t\t\t\t7.Create a multi-tier architecture
        \t\t\t\t8.Pull image to docker Hub
        \t\t\t\t9.push image to docker hub
        \t\t\t\t10.Exit
        ''')
    os.system("tput setaf 7")
    global ch
    ch = int(input("What do you want to do:"))

#############

def con_menu():
    menu_style()
    os.system("tput setaf 3")
    print('''
        \t\t\t\t1.Create a new container
        \t\t\t\t2.Start a conatainer
        \t\t\t\t3.List all running containers
        \t\t\t\t4.List all stopped containers
        \t\t\t\t5.Inspect container
        \t\t\t\t6.Stop running container
        \t\t\t\t7.Rename container
        \t\t\t\t8.Remove a container
        \t\t\t\t9.Remove all containers
        \t\t\t\t10.Create a new image from a container
        \t\t\t\t11.back
        ''')
    os.system("tput setaf 7")
    global op
    op=int(input("Enter your choice:"))
###############
def images_menu():
    menu_style()
    os.system("tput setaf 3")
    print('''
        \t\t\t\t1.Pull image from docker hub
        \t\t\t\t2.List all images
        \t\t\t\t3.Remove image
        \t\t\t\t4.Inspect image
        \t\t\t\t5.Create a new image from a container
        \t\t\t\t6.Push image to docker Hub
        \t\t\t\t7.back
        ''')
    os.system("tput setaf 7")
    global op
    op=int(input("Enter your choice:"))

############
def network_menu():
    menu_style()
    os.system("tput setaf 3")
    print('''
        \t\t\t\t1.Create a new network
        \t\t\t\t2.List all networks
        \t\t\t\t3.Inspect a network
        \t\t\t\t4.disconnect from a network
        \t\t\t\t5.Connect to a network
        \t\t\t\t6.Remove a network
        \t\t\t\t7.back
        ''')
    os.system("tput setaf 7")
    global op
    op=int(input("Enter your choice:"))
############
def volume_menu():
    menu_style()
    os.system("tput setaf 3")
    print('''
        \t\t\t\t1.Create a new volume
        \t\t\t\t2.List all volumes
        \t\t\t\t3.Inspect a volume
        \t\t\t\t4.Remove a volume
        \t\t\t\t5.back''')
    os.system("tput setaf 7")
    global op
    op=int(input("Enter your choice:"))

#############################################################################

def run(loc,ip,user12,passwd12):
    global user
    global passwd
    user=user12
    passwd=passwd12
    n=1
    while n>0:
        if loc=="l":
            menu()
            if ch==1:
                start_docker()
            elif ch==2:
                stop_docker()
###################                CONTAINER             ####################

            elif ch==3:
                con_menu()
                if op==1:
                    name=input("Enter name of container\nEg aks\n:") 
                    image=input("Enter name of image \nEg.centos:latest\n:")
                    new_con(name,image)
                elif op==2:
                    name=input("Enter a name of container you want to start:")
                    start_con(name)
                elif op==3:
                    list_run_con()
                elif op==4:
                    list_stop_con()
                elif op==5:
                    name=input("Enter a container name you want to inspect:")
                    inspect_con(name)
                elif op==6:
                    name=input("Enter a name of container you want to stop:")
                    stop_con(name)
                elif op==7:
                    name=input("Enter a name of container you want to rename:")
                    new=input("Enter a new name:")
                    rename_con(name,new)
                elif op==8:
                    name=input("Enter a name of container you want to remove:")
                    rm_con(name)
                elif op==9:
                    rm_all_con()
                elif op==10:
                    name=input("Enter container name:")
                    img=input("Enter a name of image you want to make:\nEg.myimage:v1\n:")
                    img_con(name,img)
                elif op==11:
                    continue
                else:
                    os.system("sudo tput setaf 1")
                    print("Please enter a valid option")
                    os.system("sudo tput setaf 3")
                    input("Press enter to show menu again")
                    con_menu()

######################             IMAGES             #######################


            elif ch==4:
                images_menu()
                if op==1:
                    name=input("Enter a image name you want to pull from docker hub:\nEg.centos:latest\n:")
                    pull_img(name)
                elif op==2:
                    list_img()
                elif op==3:
                    name=input("Enter a name of image you want to remove:")
                    rm_img(name)
                elif op==4:
                    name=input("Enter a name of image you want to inspect:")
                    inspect_img(name)
                elif op==5:
                    name=input("Enter container name:")
                    img=input("Enter a name of image you want to make:\nEg.myimage:v1\n:")
                    img_con(name,img)
                elif op==6:
                    menu_style()
                    img=input("Enter a name of image you want to push:")
                    user_name=input("Enter your docker repostory username:")
                    push_img(img,user_name)
                elif op==7:
                    continue
                else:
                    os.system("sudo tput setaf 1")
                    print("Please enter a valid option")
                    os.system("sudo tput setaf 3")
                    input("Press enter to show menu again")
                    images_menu()


####################                NETWORK          ########################


            elif ch==5:    
                network_menu()
                if op==1:
                    network=input("Enter a name of a network you want to create:")
                    driver=input("Enter a name of driver\nEg bridge\n:")
                    new_network(network,driver)
                elif op==2:
                    list_network()
                elif op==3:
                    name=input("Enter a name of network you want to inspect:")
                    inspect_network(name)
                elif op==4:
                    name=input("Enter name of container you want to disconnect:")
                    network=input("Enter network of {} container\nEg.bridge\n:".format(name))
                    disconnect_network(name,network)
                elif op==5:
                    name=input("Enter name of container you want to connect:")
                    network=input("Which network you want to connet\nEg.bridge\n:")
                    connect_network(name,network)
                elif op==6:
                    network=input("Enter a name of network you want to remove:")
                    rm_network(network)
                elif op==7:
                    continue
                else:
                    os.system("sudo tput setaf 1")
                    print("Please enter a valid option")
                    os.system("sudo tput setaf 3")
                    input("Press enter to show menu again")
                    network_menu()



#################                 VOLUME               ######################


             
            elif ch==6:
                volume_menu()
                if op==1:
                    vol=input("Enter a name of volume you want to create:")
                    create_vol(vol)
                elif op==2:
                    list_vol()
                elif op==3:
                    vol=input("Enter a name of volume you want to inspect:")
                    inspect_vol(vol)
                elif op==4:
                    vol=input("Enter a name of volume you want to remove:")
                    rm_vol(vol)
                elif op==5:
                    continue
                else:
                    os.system("sudo tput setaf 1")
                    print("Please enter a valid option")
                    os.system("sudo tput setaf 3")
                    input("Press enter to show menu again")
                    volume_menu()



################           MULTI-TIER Architecture         ##################

            
            elif ch==7:
                menu_style()
                os.system("sudo tput setaf 3")
                print('''
                    1.Create a Multi-tier architecure of phpmyadmin-mysql
                    ''')
                os.system("sudo tput setaf 3")
                multi_tier_architecture()
                os.system("sudo tput setaf 7")


###################     Pull image from DOCKER HUB        ######################



            elif ch==8:
                name=input("Enter a image name you want to pull from docker hub:\nEg.centos:latest\n:")
                pull_img(name)



##############            PUSH IMAGE TO DOCKER HUB         ################


            elif ch==9:
                menu_style()
                img=input("Enter a name of image you want to push:")
                user_name=input("Enter your docker repostory username:")
                push_img(img,user_name)


###################                EXIT              #######################


            elif ch==10:
                exited()
                break
            else:
                os.system("sudo tput setaf 1")
                print("Please enter a valid option")
                os.system("sudo tput setaf 3")
                input("Press enter to show menu again")
                menu()
            input("Press Enter to continue....")
            os.system("clear")


###################         remote access           ###############

        else:
            menu()
            if ch==1:
                ssh_start_docker(ip,)
            elif ch==2:
                ssh_stop_docker(ip)
###################                CONTAINER             ####################
            elif ch==3:
                con_menu()
                if op==1:
                    name=input("Enter name of container\nEg aks\n:") 
                    image=input("Enter name of image \nEg.centos:latest\n:")
                    ssh_new_con(name,image,ip)
                elif op==2:
                    name=input("Enter a name of container you want to start:")
                    ssh_start_con(name,ip)
                elif op==3:
                    ssh_list_run_con(ip)
                elif op==4:
                    ssh_list_stop_con(ip)
                elif op==5:
                    name=input("Enter a container name you want to inspect:")
                    ssh_inspect_con(name,ip)
                elif op==6:
                    name=input("Enter a name of container you want to stop:")
                    ssh_stop_con(name,ip)
                elif op==7:
                    name=input("Enter a name of container you want to rename:")
                    new=input("Enter a new name:")
                    ssh_rename_con(name,new,ip)
                elif op==8:
                    name=input("Enter a name of container you want to remove:")
                    ssh_rm_con(name,ip)
                elif op==9:
                    ssh_rm_all_con(ip)
                elif op==10:
                    name=input("Enter container name:")
                    img=input("Enter a name of image you want to make:\nEg.myimage:v1\n:")
                    ssh_img_con(name,img,ip)
                elif op==11:
                    continue
                else:
                    os.system("sudo tput setaf 1")
                    print("Please enter a valid option")
                    os.system("sudo tput setaf 3")
                    input("Press enter to show menu again")
                    con_menu()
                    

######################             IMAGES             #######################


            elif ch==4:
                images_menu()
                if op==1:
                    name=input("Enter a image name you want to pull from docker hub:\nEg.centos:latest\n:")
                    ssh_pull_img(name,ip)
                elif op==2:
                    ssh_list_img(ip)
                elif op==3:
                    name=input("Enter a name of image you want to remove:")
                    ssh_rm_img(name,ip)
                elif op==4:
                    name=input("Enter a name of image you want to inspect:")
                    ssh_inspect_img(name,ip)
                elif op==5:
                    name=input("Enter container name:")
                    img=input("Enter a name of image you want to make:\nEg.myimage:v1\n:")
                    ssh_img_con(name,img,ip)
                elif op==6:
                    menu_style()
                    img=input("Enter a name of image you want to push:")
                    user_name=input("Enter your docker repostory username:")
                    ssh_push_img(img,user_name,ip)
                elif op==7:
                    continue
                else:
                    os.system("sudo tput setaf 1")
                    print("Please enter a valid option")
                    os.system("sudo tput setaf 3")
                    input("Press enter to show menu again")
                    images_menu()


####################                NETWORK          ########################


            elif ch==5:    
                network_menu()
                if op==1:
                    network=input("Enter a name of a network you want to create:")
                    driver=input("Enter a name of driver\nEg bridge\n:")
                    ssh_new_network(network,driver,ip)
                elif op==2:
                    ssh_list_network(ip)
                elif op==3:
                    name=input("Enter a name of network you want to inspect:")
                    ssh_inspect_network(name,ip)
                elif op==4:
                    name=input("Enter name of container you want to disconnect:")
                    network=input("Enter network of {} container\nEg.bridge\n:".format(name))
                    ssh_disconnect_network(name,network,ip)
                elif op==5:
                    name=input("Enter name of container you want to connect:")
                    network=input("Which network you want to connet\nEg.bridge\n:")
                    ssh_connect_network(name,network,ip)
                elif op==6:
                    network=input("Enter a name of network you want to remove:")
                    ssh_rm_network(network,ip)
                elif op==7:
                    continue
                else:
                    os.system("sudo tput setaf 1")
                    print("Please enter a valid option")
                    os.system("sudo tput setaf 3")
                    input("Press enter to show menu again")
                    network_menu()


#################                 VOLUME               ######################


             
            elif ch==6:
                volume_menu()
                if op==1:
                    vol=input("Enter a name of volume you want to create:")
                    ssh_create_vol(vol,ip)
                elif op==2:
                    ssh_list_vol(ip)
                elif op==3:
                    vol=input("Enter a name of volume you want to inspect:")
                    ssh_inspect_vol(vol,ip)
                elif op==4:
                    vol=input("Enter a name of volume you want to remove:")
                    ssh_rm_vol(vol,ip)
                elif op==5:
                    continue
                else:
                    os.system("sudo tput setaf 1")
                    print("Please enter a valid option")
                    os.system("sudo tput setaf 3")
                    input("Press enter to show menu again")
                    volume_menu()



################           MULTI-TIER Architecture         ##################

            
            elif ch==7:
                menu_style()
                os.system("sudo tput setaf 3")
                print('''
                    1.Create a Multi-tier architecure of phpmyadmin-mysql
                    ''')
                os.system("sudo tput setaf 3")
                ssh_multi_tier_architecture(ip)
                os.system("sudo tput setaf 7")


###################     Pull image from DOCKER HUB        ######################



            elif ch==8:
                name=input("Enter a image name you want to pull from docker hub:\nEg.centos:latest\n:")
                ssh_pull_img(name,ip)



##############            PUSH IMAGE TO DOCKER HUB         ################


            elif ch==9:
                menu_style()
                img=input("Enter a name of image you want to push:")
                user_name=input("Enter your docker repostory username:")
                ssh_push_img(img,user_name,ip)


###################                EXIT              #######################


            elif ch==10:
                exited()
                break
            else:
                os.system("sudo tput setaf 1")
                print("Please enter a valid option")
                os.system("sudo tput setaf 3")
                input("Press enter to show menu again")
                menu()
            input("Press Enter to continue....")
            os.system("clear")

