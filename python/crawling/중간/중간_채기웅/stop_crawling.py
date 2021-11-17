import os

def kill_thread():
    f = open("./dontouch/process_option.txt","w")
    f.write("False")
    f.close()
    print("stopped!")

if __name__ == "__main__":
    kill_thread()