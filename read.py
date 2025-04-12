def process_file():
    try:
        # Ask user for input filename
        input_filename = input("myfile.txt: ")
        
        # Try to open and read the input file
        with open('myfile.txt', 'r') as input_file:
            content = input_file.read()
            
        # Modify the content (capitalize everything)
        modified_content = content.upper()
        
        # Create output filename by adding '_modified' before the extension
        output_filename = input_filename.rsplit('.', 1)
        output_filename = f"{output_filename[0]}_modified.{output_filename[1]}"
        
        # Write modified content to new file
        with open('myfile_modified.txt', 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"Successfully processed file. Modified content saved to: myfile_modified.txt")
        
    except FileNotFoundError:
        print(f"Error: The file 'myfile.txt' was not found.")
    except PermissionError:
        print(f"Error: Permission denied. Cannot access the file 'myfile.txt'.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {str(e)}")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    process_file()
