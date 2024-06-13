
import subprocess



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
