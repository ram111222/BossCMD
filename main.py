import math
import matplotlib.pyplot as plt
from os import system
from Def import *
from elevate import elevate
# from ftplib import FTP

blue = '\033[34m'
reset_color = "\033[0m"

system("title " + "BOSS CMD")

print(blue + "BBBBB   OOOO    SSSSS   SSSSS          CCCCC   M   M   DDDDD  ")
print(blue + "B    B  O    O  S        S            C        MM MM   D    D ")
print(blue + "BBBBB   O    O   SSSSS    SSSSS       C        M M M   D    D")
print(blue + "B    B  O    O       S        S       C        M   M   D    D ")
print(blue + "BBBBB    OOOO    SSSSS   SSSSS         CCCCC   M   M   DDDDD")

while True:
    Cmd = input(reset_color + "C:/User/RAM: ")

    if Cmd.lower() == "help":
        print("The commands are \n Help - List all commands \n Ping - pings a server \n Powershell - Run any "
              "powershell script \n Plot - Plot 2 points on a graph with a incline \n Calculator - Standard "
              "calculator with addition sub mult and divide \n FTP - Interact with an FTP server")
        # To add more later, keep this here

    if Cmd.lower() == "ping":
        x = input("In order to run we need higher perms. Do you allow us to run as a admin?: ")
        if x.lower() == "yes":
            elevate()
            url = input("Enter the URL to ping: ")
            output = ping_url(url)
            if output is not None:
                print("Ping result for", url)
                print(output)
        else:
            print("terminated due to insufficient perms")

    if Cmd.lower() == "powershell":
        command = input("Enter the command to run (type 'powershell' to run PowerShell script): ")
        if command.lower() == 'powershell':
            script_path = input("Enter the path to the PowerShell script: ")
            output = run_powershell_script(script_path)
            if output is not None:
                print("PowerShell script output:")
                print(output)

    if Cmd.lower() == "plot":
        try:
            timeframe = input(
                "What is your timeframe (Separate your points. So like 5min 10min. keep in mind this has to be "
                "values): ")
            values = input("What are the corresponding values (comma-separated list of values): ")
            rate_of_change = float(input("What is the rate of change: "))
            timeframe = [float(x) for x in timeframe.split(',')]
            values = [float(y) for y in values.split(',')]
            if len(timeframe) < 2 or len(values) < 2:
                print("You need at least two points to plot a graph.")
            else:
                new_values = [val + rate_of_change * time for time, val in zip(timeframe, values)]
                plt.plot(timeframe, values, label='Original Values')
                plt.plot(timeframe, new_values, label=f'Values with Rate of Change {rate_of_change}')
                plt.xlabel('Time')
                plt.ylabel('Value')
                plt.title('Graph with Rate of Change')
                plt.legend()
                plt.show()
        except ValueError as err:
            print(
                "There was an error that occurred when checking your values are numbers. "
                f"Double check you did not add any text into your values. Below is the error. \n {err}")

    if Cmd.lower() == "calculator":
        try:
            num = float(input("What is your 1 number: "))
            num2 = float(input("What is your second number: "))
            Sgn = input("What operation are you doing:")
            if Sgn == '+':
                print(num + num2)
            elif Sgn == "-":
                print(num - num2)
            elif Sgn == "*":
                print(num * num2)
            elif Sgn == "/":
                try:
                    print(num / num2)
                except ZeroDivisionError:
                    print("Dividing by zero is not possible")
            elif Sgn.lower() == "square root":
                print(math.sqrt(num))
            else:
                print("That is not a valid sign at this time. If you believe this to be a mistake please post an issue"
                      f"\n https://github.com/ram111222/BossCMD  ")
        except ValueError as err2:
            print("An error has occurred while running this math. Make sure all your numbers have no other characters"
                  f"\n Here is the error {err2} ")

    if Cmd.lower() == "ftp":
        server = input("Enter the FTP server address: ")
        username = input("Enter the FTP username: ")
        password = input("Enter the FTP password: ")

        ftp = connect_ftp(server, username, password)
        if ftp:
            while True:
                ftp_cmd = input("Enter FTP command (list/download/quit): ")
                if ftp_cmd.lower() == "list":
                    list_files(ftp)
                elif ftp_cmd.lower() == "download":
                    filename = input("Enter the filename to download: ")
                    local_filename = input("Enter the local filename to save as: ")
                    download_file(ftp, filename, local_filename)
                elif ftp_cmd.lower() == "quit":
                    ftp.quit()
                    print("FTP connection closed.")
                    break
                else:
                    print("Invalid FTP command. Use 'list', 'download', or 'quit'.")
