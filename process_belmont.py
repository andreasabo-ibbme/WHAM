import subprocess, os
from icecream import ic
import glob

AMB_ID = "AB10"

INPUT_FOLDER = r"/home/saboa/mnt/n_drive/AMBIENT/AMBIENT_Belmont/" + AMB_ID
OUTPUT_FOLDER_BASE = r"/home/saboa/mnt/n_drive/AMBIENT/AMBIENT_Belmont_posetracked/WHAM/" + AMB_ID

if __name__ == "__main__":
    all_vids = glob.glob(os.path.join(INPUT_FOLDER, "*.h264"))
    ic(len(all_vids))
    ic(all_vids)
    for vid in all_vids:
        command_line = ['python', 'demo.py', '--video', vid, '--output', OUTPUT_FOLDER_BASE]
        p = subprocess.Popen(command_line)
        p.wait()
        quit()
    pass