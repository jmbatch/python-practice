def ext():
    invalid_input = True
    while invalid_input == True:
        file_name = input("Please enter the filename with its extension: ")
        ext_index = file_name.rfind(".")
        if len(file_name) == 0 or ext_index == 0:
            print("Filename cannot be blank!")
        elif ext_index == -1 or (len(file_name.strip()) - ext_index) == 1:
            print("Extension of the filename is required!")
        else:
            invalid_input = False
        break
    ext = file_name[(ext_index):]
    print("The extension is {}".format(ext))

ext()
