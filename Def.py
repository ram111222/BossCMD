import subprocess
from ftplib import FTP


def run_powershell_script(script):
    try:
        result = subprocess.run(["powershell", "-File", script], capture_output=True, text=True, check=True)
        result = result.stdout
        return result
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None


def ping_url(link):
    try:
        # Execute the ping command
        ping_process = subprocess.Popen(["ping", "-n", "4", link], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        shell=True)

        # Get the output
        ping_output, _ = ping_process.communicate()

        # Decode the output from bytes to string
        ping_output = ping_output.decode("utf-8")

        return ping_output
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None


def connect_ftp(server, username, password):
    try:
        # Connect to the FTP server
        ftp = FTP(server)
        ftp.login(username, password)
        print(f"Successfully connected to {server}")

        return ftp
    except Exception as e:
        print(f"Error connecting to FTP server: {e}")
        return None


def list_files(ftp):
    try:
        print("Listing files:")
        files = ftp.nlst()
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error listing files: {e}")


def download_file(ftp, filename, local_filename):
    try:
        with open(local_filename, 'wb') as local_file:
            ftp.retrbinary(f"RETR {filename}", local_file.write)
        print(f"Successfully downloaded {filename} to {local_filename}")
    except Exception as e:
        print(f"Error downloading file: {e}")


def main():
    # FTP server credentials
    server = 'ftp.example.com'  # Replace with your FTP server address
    username = 'your_username'  # Replace with your FTP username
    password = 'your_password'  # Replace with your FTP password

    ftp = connect_ftp(server, username, password)
    if ftp:
        list_files(ftp)

        # Example of downloading a file
        file_to_download = 'example.txt'  # Replace with the file you want to download
        local_file_name = 'local_example.txt'  # Local file name for saving

        download_file(ftp, file_to_download, local_file_name)

        # Close the FTP connection
        ftp.quit()
