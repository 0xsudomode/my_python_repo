File and Directory Operations

    os.getcwd(): Get the current working directory.
    os.chdir(path): Change the current working directory to the specified path.
    os.listdir(path='.'): List all files and directories in the specified path (defaults to the current directory).
    os.mkdir(path): Create a directory at the specified path.
    os.makedirs(path): Create intermediate directories if they don't exist.
    os.rmdir(path): Remove an empty directory.
    os.remove(path): Remove a file.
    os.rename(src, dst): Rename or move a file or directory from src to dst.
    os.removedirs(path): Remove a directory and any empty parent directories.

2\. Path Operations

    os.path.join(path, *paths): Join one or more path components.
    os.path.exists(path): Check if a path exists (file or directory).
    os.path.isfile(path): Check if a path is a file.
    os.path.isdir(path): Check if a path is a directory.
    os.path.abspath(path): Get the absolute path of a file.
    os.path.split(path): Split the path into a tuple (head, tail).
    os.path.basename(path): Get the base name (last component) of the path.
    os.path.dirname(path): Get the directory name of the path.
    os.path.getsize(path): Get the size of the file at the specified path.

3\. Environment Variables

    os.getenv(key): Get the value of the environment variable key.
    os.environ: Dictionary representing the string environment, which can be used to access and modify environment variables.

4\. Process Management

    os.system(command): Run the command (a string) in the system shell.
    os.spawn(): Spawn a new process (less commonly used than subprocess module).
    os.getpid(): Get the process ID of the current process.
    os.getppid(): Get the parent process ID.

5\. Temporary Files and Directories

    os.tempnam(): Generate a unique name for a temporary file.
    os.tmpfile(): Return a file object for a temporary file opened in binary mode.

6\. Working with Permissions

    os.chmod(path, mode): Change the mode of the file at path (file permissions).
    os.chown(path, uid, gid): Change the owner and group of a file.

7\. File Descriptors

    os.open(): Open a file and return a file descriptor.
    os.close(fd): Close a file descriptor.
    os.read(fd, n): Read n bytes from the file descriptor fd.
    os.write(fd, str): Write to a file descriptor.

8\. Platform-specific Functions

    os.name: Get the name of the operating system dependent module imported (e.g., posix, nt, os2, ce, java).
    os.uname(): (Unix-specific) Return information about the current operating system.
