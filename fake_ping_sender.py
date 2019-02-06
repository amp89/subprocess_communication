import subprocess
"""
Pretend this is the server or something
"""

def main():
    fake_color_change_program_subproccess = subprocess.Popen(['python', 'fake_color_change_program.py'], stdin = subprocess.PIPE , stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

    while 1:
        color_selection = input("Color? >") # This would be what the ping returns, using input instead cause i'm too lazy for that
        color_selection = str(color_selection) + "\n"
        b = bytearray()
        b.extend(map(ord,color_selection))
        fake_color_change_program_subproccess.stdin.write(b)
        fake_color_change_program_subproccess.stdin.flush()
        print(f"OUTPUT from fccp: {fake_color_change_program_subproccess.stdout.readline()}")

if __name__ == '__main__':
    main()

