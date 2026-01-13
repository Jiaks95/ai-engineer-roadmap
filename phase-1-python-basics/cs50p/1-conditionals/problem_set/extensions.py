"""
File: extensions.py
Author: Oscar Jia
Assignment: CS50P Problem Set 1: File Extensions
Description: 
    Prompts the user for a file name and outputs the corresponding 
    media type (MIME type). Handles case-insensitivity and files 
    without extensions.
"""

def main():
    file_name = input("File name: ").strip().lower()

    if "." not in file_name:
        print("application/octet-stream")
        return

    _, file_extension = file_name.rsplit(".", maxsplit=1)

    match file_extension:
        case "gif":
            print("image/gif")

        case "jpg" | "jpeg":
            print("image/jpeg")

        case "png":
            print("image/png")

        case "pdf":
            print("application/pdf")

        case "txt":
            print("text/plain")

        case "zip":
            print("application/zip")

        case _:
            print("application/octet-stream")

main()