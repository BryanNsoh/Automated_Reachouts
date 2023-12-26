import os


def copy_py_to_txt(output_file):
    with open(output_file, "w") as outfile:
        for filename in os.listdir("."):
            if filename.endswith(".py"):
                with open(filename, "r") as infile:
                    outfile.write(f"\n\n# Contents of {filename}\n")
                    outfile.write(infile.read())


def main():
    output_filename = "all_python_contents.txt"
    copy_py_to_txt(output_filename)
    print(f"All .py file contents copied to {output_filename}")


if __name__ == "__main__":
    main()
