import shutil
import os


# with open("test.txt", "w") as f:
#     f.write("New Text File\n")
#     f.write("Adding new Text\n")
#     f.write("Some more line\n")
#
# with open("test.txt", "r") as f:
#     print(f.read())
#     # print(f.readline())
#     # print(f.readline())
#     # print(f.readline())
#     # print(f.readline())
#
#
# with open("test.txt", "a") as f:
#     f.write("Some new lines!!!\n")
#
# with open("test.txt", "r") as f:
#     print(f.read())
#
# with open("test.txt", "w") as f:
#     f.writelines("Overwriting existing file ")
#
# with open("test.txt", "r") as f:
#     print(f.read())
# # ------------------------------
#
# print(os.environ)
print(os.getcwd())
# print(os.uname())
print("Creating New Directory...")
if not os.path.exists("NewDir"):
    os.mkdir("NewDir")

print(f"Directories :{os.listdir()}")
input()
print(f"Changing parent directory...")
os.chdir("NewDir")
print(f"{os.getcwd()}")
input()
print("Creating a file in the directory...")
with open("testFile.txt", "w") as f:
    f.writelines("Some Text")
print(f"Files in directory: {os.listdir()}")
input()

print("Renaming file...")
os.rename("testFile.txt", "RenamedFile.txt")
print(f"Renamed file: {os.listdir()}")
input()
os.chdir("..")
print("Removing created Directory...")
try:
    os.remove("NewDir")
except OSError as e:
    print(f"Error: {e}")

print("Using Shutil module...")
shutil.rmtree("NewDir")
print(os.listdir())
input()
os.system("cls")  # Linux
# OR
# os.system("clear") # Windows
