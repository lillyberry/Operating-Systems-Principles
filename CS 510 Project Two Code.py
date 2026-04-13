"""
    Class:   CS-510
    Author:  Lillian Berry
    Date:    04/01/26

    Description:  Each function that needs to be completed has a comment at the top with
                  TODO written in it with instructions.

                  Within the function is a section with the comment #TODO where you will
                  insert your code as per the instructions.
"""  
import os
import psutil  # requires pip install
import sys
import threading

"""
  Three provided Utility functions to use
"""
def printBlankLines(lines: int):
    for i in range(lines):
        print("")

def printMsg1(num):
    print("Thread 1 cubed: {}" .format(num * num * num))


def printMsg2(num):
    print("Thread 2 squared: {}" .format(num * num))


"""
   TODO This function will display information about a file, size and file information.
   You can provide your own or use the projecttwo.txt file.

   Use psutil to get initial file information.
"""
def getFileDiskUsageStatistics() -> None:
    print("Getting Disk Statistics")
    file_name = "./projecttwo.txt"

    #TODO INSERT YOUR CODE HERE
    try:
        # File size
        size = os.path.getsize(file_name)
        print(f"File Name: {file_name}")
        print(f"File Size: {size} bytes")

        # Disk usage
        disk = psutil.disk_usage('/')
        print(f"Total Disk Space: {disk.total}")
        print(f"Used Disk Space: {disk.used}")
        print(f"Free Disk Space: {disk.free}")
        print(f"Disk Usage Percentage: {disk.percent}%")

    except FileNotFoundError:
        print("File not found.")

    printBlankLines(2)

"""
   TODO This should use psutil to retrieve standard and 
   virtual memory statistics
"""
def getMemoryStatistics() -> None:
    print("Getting Memory Statistics")

    #TODO INSERT YOUR CODE HERE
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()

    print(f"Total Memory: {mem.total}")
    print(f"Available Memory: {mem.available}")
    print(f"Used Memory: {mem.used}")
    print(f"Memory Usage: {mem.percent}%")

    print(f"Swap Total: {swap.total}")
    print(f"Swap Used: {swap.used}")
    print(f"Swap Free: {swap.free}")

    printBlankLines(2)

"""
   TODO This should use psutil to retrieve CPU statistics, including
   information on processes.
"""
def getCpuStatistics() -> None:
    print("Getting CPU Statistics")
    
    #TODO INSERT YOUR CODE HERE
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"CPU Cores: {psutil.cpu_count(logical=True)}")

    # Show top processes
    print("Top Processes:")
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            print(proc.info)
        except:
            pass

    printBlankLines(2)


"""
   TODO This function will show multi threading capabilities.

   Two threads should be created.
    
   One used to call the function "printMsg1" provided above.

   A second thread should call the function "printMsg2" provided above.
"""
def showThreadingExample() -> None:
    print("Demonstrating Threading")
   
    #TODO INSERT YOUR CODE HERE
    t1 = threading.Thread(target=printMsg1, args=(5,))
    t2 = threading.Thread(target=printMsg2, args=(5,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done With Threading!")

    printBlankLines(2)

"""
   TODO This function shows system error handling.

   Since out of memory, or out of disk space errors are difficult to create,
   we will use a divide by zero error and show the error handling being executed.
"""
def showErrorHandling() -> None:
    print("Demonstrating Error Handling")
    try:

       #TODO Insert your code here to cause a divide by zero error
       res = 10 / 0  # intentional error
    
    except ZeroDivisionError:
        print("You can't divide by zero!")
        
    except MemoryError:
        print("Memory Error!")
        
    else:
        print("Result is", res)
        
    finally:
        print("Execution complete.")

    printBlankLines(2)

"""
   Main function, does not require modification.

   This calls the specific functions.
"""
def main() -> int:
    print("Starting Program")
    print("=============================")
   
    getFileDiskUsageStatistics()   
    
    getCpuStatistics()
    
    getMemoryStatistics()

    showThreadingExample()

    showErrorHandling()


if __name__ == '__main__':
    sys.exit(main()) 