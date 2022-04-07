import virtualbox
import os

vbox = virtualbox.VirtualBox()
session = virtualbox.Session()

def printSeparator():
    print("\n----------*****----------\n")

def listMachines():
    position = 0
    length = len(vbox.machines)
    if length != 0:
        print("Machines list : \n")
        for machine in vbox.machines:
            position += 1
            print( str(position) + " - " + machine.name)
    else:
        print("There aren't virtual machines created")

def createMachine():
    print("Provide OS box name: ", end="")
    boxName = input()
    newFolderName = boxName.replace('/','_')

    if (not os.path.exists(newFolderName)):
        newFolderName = boxName.replace('/','_')
        os.mkdir(newFolderName)
        os.chdir(newFolderName)
        os.system('vagrant init ' + boxName)
        os.system('vagrant up')
        os.system('vagrant halt')
        os.chdir('../')
        print('\nMachine succesfully created!')
    else:
        print('\nAn instance for that machine already exists')

def startMachine():
    listMachines()
    print("\nWhich one do you want to start ? ", end = "")
    machineNumber = int(input())
    machineName = vbox.machines[machineNumber - 1].name
    print("Starting " + machineName + " on VBox GUI")
    machine = vbox.find_machine(machineName)
    progress = machine.launch_vm_process(session, "gui", [])
    progress.wait_for_completion()

def powerOffMachine():
    listMachines()
    print("\nWhich one do you want to power off? ", end = "")
    machineNumber = int(input())
    machineName = vbox.machines[machineNumber - 1].name
    machine = vbox.machines[machineNumber - 1]
    try:
        session.console.power_down()
        print("Machine shutted down")
    except:
        print("That's not the currently running machine")

while True:

    print("What do you want to do ? \n")
    print("1 - List registered machines")
    print("2 - Create a new machine - Vagrant")
    print("3 - Start machine - VBox SDK")
    print("4 - Power off machine - VBox SDK")
    print("5 - Quit")
    print("\nOption: ", end = "")

    option = int(input())
    printSeparator()

    if( option == 1):
        listMachines() 
    if( option == 2):
        createMachine()
    if( option == 3):
        startMachine()
    if( option == 4):
        powerOffMachine()
    if( option == 5):
        break
    printSeparator()
    

