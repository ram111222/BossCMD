# import sys
from PIL import Image
import subprocess


def run_powershell_script(script):
    try:
        result = subprocess.run(["powershell", "-File", script], capture_output=True, text=True, check=True)
        result = result.stdout
        return result
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None


def ping_url(url):
    try:
        # Execute the ping command
        ping_process = subprocess.Popen(["ping", "-n", "4", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        shell=True)

        # Get the output
        ping_output, _ = ping_process.communicate()

        # Decode the output from bytes to string
        ping_output = ping_output.decode("utf-8")

        return ping_output
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None


while True:
    print("BBBBB   OOOO    SSSSS   SSSSS          CCCCC   M   M   DDDDD  ")
    print("B    B  O    O  S        S            C        MM MM   D    D ")
    print("BBBBB   O    O   SSSSS    SSSSS       C        M M M   D    D")
    print("B    B  O    O       S        S       C        M   M   D    D ")
    print("BBBBB    OOOO    SSSSS   SSSSS         CCCCC   M   M   DDDDD")

    Cmd = input("C:/User/RAM: ")

    if Cmd == "Help":
        print("The commands are \n Help - List all commands \n Ping - pings a server")
        # To add more later, keep this here

    if Cmd == "Ping":
        url = input("Enter the URL to ping: ")
        output = ping_url(url)
        if output is not None:
            print("Ping result for", url)
            print(output)
    if Cmd == "Powershell":
        command = input("Enter the command to run (type 'powershell' to run PowerShell script): ")

        if command.lower() == 'powershell':
            script_path = input("Enter the path to the PowerShell script: ")
            output = run_powershell_script(script_path)
            if output is not None:
                print("PowerShell script output:")
                print(output)

    if Cmd == "Ram2026":
        url = input("Enter the URL to ping: ")
        output = ping_url(url)
        if output is not None:
            print("Ping result for", url)
            print(output)

        # if Cmd == "":Echo
        # print("Argument 1:", sys.argv[1])
