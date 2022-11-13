import os

def getFileAsString(file):
    '''
    Returns the contents of a text file as a string, from the beginning of the
      file.
      
    The `file` parameter is an opened file object with write permissions. This
      function does *not* close the `file` when it is finished.
    '''
    file.seek(0)
    return file.read()


def printContentsOfFile(fileName):
       if os.access(fileName, os.R_OK):
        f = open(fileName, "r")
        string = getFileAsString(f)
        print(string, end='')
        f.close()

      


if __name__ == '__main__':
    # `os.getcwd()` returns the (C)urrent (W)orking (D)irectory as a string.
    # Synonymous to `pwd` in the shell
    cwd = os.getcwd()
    print(f"Please enter a file path relative to {cwd}")
    fileName = input("File Path: ")
    printContentsOfFile(fileName)
