import subprocess

def internet_on():
    try:
        subprocess.check_output(
            ["ping", "c", "1", "google.com"], stderr=subprocess.DEVNULL
            )
        return True
    except subprocess.CalledProcessError:
        return False
    
def play_alert():
    subprocess.run(
        ["aplay", "/usr/share/sounds/alsa/Front_Center.wav"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def monitor():
    was down = Falseqw  az