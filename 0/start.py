import json
import subprocess
import urllib.request
import webbrowser

class ju:
    pass
    pretext = "https://raw.githubusercontent.com/jesusjorge/docs/main/0/"
    def ci(imp,install):
        try:
            exec(imp,globals())
        except:
            try:
                result = subprocess.check_output("pip3 install " + install,shell=True,stderr=subprocess.STDOUT)
                exec(imp,globals())
            except Exception as e:
                error = e.output.decode()
                print(error)
                webbrowser.open("https://visualstudio.microsoft.com/es/visual-cpp-build-tools/")
                raise Exception(error)
    def go(url):
        return urllib.request.urlopen(url).read()
    def son(s):
        return json.loads(s)

menu = ju.son(ju.go(ju.pretext + "menu.json"))
while True:
    print("\nChoose an option:")
    c = 0
    for it in menu:
        print("[" + str(c) + "] " + it[0])
        c = c + 1
    option = input("Option: ")
    try:
        code = menu[int(option)][1]
        exec(code,globals())
    except Exception as e:
        print(str(e))
        print("Invalid Option!")

