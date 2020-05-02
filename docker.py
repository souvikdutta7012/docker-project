import os
print("\t\t\t\t----------A GRAPHICAL WAY TO DOCKER----------")
password=input("Enter password:")
if password!="redhat":
    print("Permission Denied.\n")
    exit()
def savechanges(name):
    myo= input("Enter the os name you want to keep along with its version {eg=myos:7}")
    os.system("docker commit {0} {1}".format(name,myo))
while True:
    print("Please enter your choice:-\n")
    print("0->Take a break."
          "\n1->Install Docker."
          "\n2->Download images."
          "\n3->Configure my own network."
          "\n4->Create my own persistent storage in docker."
          "\n5->Create my own web server"
          "\n6->Create environment for wordpress"
          "\n7->Start from scratch")
    ch=int(input())
    if ch==0:
        print("\nBYE !!!!!! SEE YOU LATER")
        exit()
    elif ch==1:
        os.system("dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
        os.system("dnf repolist -v")
        os.system("dnf install docker-ce --nobest -y")
    elif ch==2:
        os.system("systemctl start docker")
        os.system("docker images")
        sd=input("\nEnter the os you want to install along with its version {eg=centos:7}:")
        os.system("docker pull {0} ".format(sd))
        os.system("docker images")
    elif ch==3:
        os.system("systemctl start docker")
        name = input("\nEnter your network name:")
        os.system("docker network ls")
        rout = input("\nChoose the driver:-")
        os.system("docker network create --driver {0} {1}".format(rout,name))
        os.system("docker network ls")
    elif ch==4:
        os.system("systemctl start docker")
        os.system("docker volume ls")
        name = input("\nEnter your persistent storage name:")
        os.system("docker volume create  {0}".format(name))
        os.system("docker volume ls")
    elif ch==5:
        os.system("systemctl start docker")
        os.system("systemctl start firewalld")
        os.system("docker rm -f $(docker ps -q -a)")
        name=input("\nEnter the name of the server you want to keep:")
        os.system("iptables -P FORWARD ACCEPT")
        os.system("docker network ls")
        rout=input("\nChoose the nerwork:-")
        port=int(input("\nEnter a port of the base os for ip forwarding:-"))
        os.system("docker volume ls")
        vol=input("\nChoose the volume to make your server persistent:-")
        os.system("gedit /var/lib/docker/volumes/{0}/_data/index.html".format(vol))
        if input("\nIs this your first time creating your custom image for web server?(y/n):")=="y":
            os.system("docker images")
            sd = input("\nEnter the os in which you want to run along you web server {eg=centos:7}:")
            if input("Do you have {0} with you (y/n)?".format(sd)) == "n":
                os.system("docker pull {0} ".format(sd))
            os.system("docker container run -dit --name {0}  --network host {1}  ".format(name,sd))
            os.system("docker container exec {0} yum install httpd -y".format(name))
            savechanges(name)
            os.system("docker stop {0}".format(name))
            os.system("docker rm -f $(docker ps -q -a)")
        os.system("docker images")
        server=input("\nChoose the server along with its version {eg=webserver:v1}:")
        os.system("docker container run -dit -p {2}:80 --name {0} -v {3}:/var/www/html --network {4} {1}  ".format(name,server,port,vol,rout))
        os.system("docker container exec {0} rm -rf  /var/run/httpd/*".format(name))
        os.system("docker container exec {0} /usr/sbin/httpd".format(name))
        os.system("systemctl stop firewalld")
    elif ch==6:
        os.system("systemctl start docker")
        os.system("systemctl start firewalld")
        os.system("docker rm -f $(docker ps -q -a)")
        if input("\nDo you have wordpress:5.1.1-php7.3-apache(y/n)?") == "n":
            os.system("docker pull wordpress:5.1.1-php7.3-apache ")
        if input("\nDo you have mysql:5.7(y/n)?") == "n":
            os.system("docker pull mysql:5.7 ")
        user=input("\nEnter user name:")
        pas=input("\nEnter user password:")
        dbname=input("\nEnter name of the database you want to create:")
        os.system("docker volume ls")
        vol=input("\nChoose the volume you want to use for your mysql:")
        dname=input("\nChoose name for your mysql:")
        os.system("docker run  -dit -e MYSQL_ROOT_PASSWORD=redhat  -e MYSQL_USER={0} -e MYSQL_PASSWORD={1} -e MYSQL_DATABASE={2}  -v {3}:/var/lib/mysql  --name {4} mysql:5.7".format(user,pas,dbname,vol,dname))
        name2=input("\nEnter name for wordpress:")
        vol2= input("\nChoose the volume you want to use for your wordpress:")
        port = int(input("\nEnter a port of the base os for ip forwarding:"))
        os.system("docker run -dit -e WORDPRESS_DB_HOST={0} -e WORDPRESS_DB_USER={6} -e WORDPRESS_DB_PASSWORD={1} -e WORDPRESS_DB_NAME={2} -v {3}:/var/www/html -p {4}:80 --link {0}  --name {5} wordpress:5.1.1-php7.3-apache".format(dname,pas,dbname,vol2,port,name2,user))
        os.system("iptables -P FORWARD ACCEPT")
        if input("\nDo you want to save your web server(y/n)?")=="y":
            savechanges(name)
    elif ch==7:
        if input("Remove running instances:")=="y":
            os.system("docker rm -f $(docker ps -q -a)")
        if input("Remove pulled images:")=="y":
            os.system("docker image ls")
            name3=input("\nEnter the os you want to rempove along with its version {eg=centos:7}:")
            os.system("docker image rm {0}".format(name3))
            os.system("docker image ls")
        if input("Remove created networks:")=="y":
            os.system("docker network ls")
            name3=input("\nEnter the network you want to remove:")
            os.system("docker network rm {0}".format(name3))
            os.system("docker network ls")
        if input("Remove created volumes:")=="y":
            os.system("docker volume ls")
            name3=input("\nEnter the volume you want to remove:")
            os.system("docker volume rm {0}".format(name3))
            os.system("docker volume ls")

    else :
        print("Sorry !!!!!! Wrong input ....")
