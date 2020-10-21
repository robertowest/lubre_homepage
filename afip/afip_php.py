import subprocess

def simple_caller():
    subprocess.call(["php", "afip.php"])

def output_caller():
    proc = subprocess.Popen("php afip.php", shell=True, stdout=subprocess.PIPE)
    print( proc.stdout.read() )


if __name__ == '__main__':
    # simple_caller()
    output_caller()
