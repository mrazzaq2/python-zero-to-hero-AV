def file_server_config(file_path, key, value):
    updated = False
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if line.startswith(key + "="):
                file.write(f"{key}={value}\n")
                updated = True
            else:
                file.write(line)

        # If the key was not found, you might want to add it
        if not updated:
            file.write(f"{key}={value}\n")

file_server_config("server.config", "MAX_CONNECTIONS", "12312")
