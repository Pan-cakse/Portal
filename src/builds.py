import requests
from versions import version

def download_build(build):
    url = f"https://github.com/IceCreamMC/IceCream/releases/download/{build}/IceCream-paperclip-{version}-R0.1-SNAPSHOT-mojmap.jar"

    response = requests.get(url, allow_redirects=True)

    if response.status_code == 200:
        file_name = f"IceCream-paperclip-{version}-R0.1-SNAPSHOT-mojmap.jar"
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Build {build} downloaded successfully as {file_name}")
    else:
        print(f"Failed to download build {build}. HTTP status code: {response.status_code}")

build_number = input("Enter the build number: ")

download_build(build)
