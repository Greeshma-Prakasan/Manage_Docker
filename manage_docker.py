import os
from rich.console import Console

console = Console()

def stat_container():
    os.system("docker container stats")

def download_new_image():
    img = input("\tEnter the name of Image : ")
    os.system(f'docker pull {img}')

def run_container():
    img = input("\tEnter the image name : ")
    container = input("\tEnter the container name : ")
    os.system(f'docker run --name {container} {img}')
    console.print("\tContainer is running.........",style="bold blue")

def del_container():
    container = input("\tEnter the container name : ")
    os.system(f'docker rm {container}')
    console.print("\tContainer successfully deleted.........",style="bold blue")

def nw_details():
    res = os.popen("docker network inspect bridge").read()
    console.print(res,style="bold blue")

def modify_nw():
    res = os.popen("docker network ls").read()
    console.print(f"Available networks\n\n{res}",style="bold blue")
    container = input("Enter the container name : ")
    os.system(f"docker network disconnect bridge {container}")
    console.print(f"{container} disconnected...........",style="bold blue")
    nw = input("Enter the new network name : ")
    ip = input("Enter the ip : ")
    os.system(f"sudo docker network create -d bridge --subnet={ip}  {nw}")
    console.print("Network Created...................")
    os.system(f"docker network connect {nw} {container}")
    console.print(f"Container connected to new network {nw}")


def menu():
    console.print("1. Status of containers\n2. Download new Image\n3. Run container\n4. Delete Container\n5. Network details of container\n6. Modify Network details of contaniner\n7. Exit",style="bold yellow")
    
while True:
    menu()
    c = int(input("Enter the choice : "))
    if c==1:
        stat_container()
    elif c==2:
        download_new_image()
    elif c==3:
        run_container()
    elif c==4:
        del_container()
    elif c==5:
        nw_details()
    elif c==6:
        modify_nw()
    elif c==7:
        break
    else:
        console.print("\tInvalid Choice",style="bold blue")