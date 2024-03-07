import subprocess

def get_changed_files():
    """Get a list of files changed in the last commit."""
    result = subprocess.run(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD'], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.splitlines()
    else:
        raise Exception("Failed to get changed files.")

def print_file_contents(file_path):
    """Print the contents of a file in chunks to handle large files."""
    try:
        with open(file_path, 'r') as file:
            print(f"Contents of {file_path}:")
            while True:
                # Read and print the file in chunks of 1024 bytes
                chunk = file.read(1024)
                if not chunk:
                    break
                print(chunk, end='')
    except FileNotFoundError:
        print(f"File {file_path} not found.")

def main():
    changed_files = get_changed_files()
    for file_path in changed_files:
        print_file_contents(file_path)

if __name__ == "__main__":
    main()
    

