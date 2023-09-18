from flask import request


def base64_decode(base64_string):
    import base64
    return base64.b64decode(base64_string.split(",")[1])




def file_save_as(file_name, file_content):
    print("executed : file_save_as")
    import os

    if not os.path.exists("./uploadFiles/"):
        os.makedirs("./uploadFiles/")
    if not os.path.exists("./uploadFiles/"):
        os.makedirs("./uploadFiles/")
    file_path = "./uploadFiles/"+file_name
    try:
        with open(file_path, "wb") as f:
            f.write(file_content)
        return True
    except Exception as e:
        print(e)
        return False


def upload_file():
    f = request.form
    file_name = f['name']
    total = f['total']
    try:
        for i in range(0, int(total)):
            file_content = base64_decode(f['base64' + str(i)])
            file_name = f['name' + str(i)]
            file_save_as(file_name, file_content)

        return {
            "status": "success",
            "message": "File uploaded successfully",
        }
    except Exception as e:
        print(e)
        return {
            "status": "error",
            "message": str(e)
        }
