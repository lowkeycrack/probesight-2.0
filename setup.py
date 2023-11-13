import subprocess

def install_dependencies(packages):
    if not isinstance(packages,dict):
        raise TypeError('Expected dictionary argument[*]')
    else:
        for pr,vr in packages.items():
            try:
                subprocess.check_call(['pip','install',f"{pr}=={vr}"])
            except subprocess.CalledProcessError:
                print("couldn't install the specifid version \ntrying a different one")
                subprocess.check_call(['pip','install',f"{pr}"])

if __name__ =='__main__':
    packages={
    'attrs': '23.1.0',
    'certifi': '2023.7.22',
    'charset-normalizer': '3.3.2',
    'click': '8.1.7',
    'h11': '0.14.0',
    'idna': '3.4',
    'outcome': '1.3.0.post0',
    'pip': '23.2',
    'PySocks': '1.7.1',
    'requests': '2.31.0',
    'selenium': '4.15.2',
    'setuptools': '67.8.0',
    'sniffio': '1.3.0',
    'sortedcontainers': '2.4.0',
    'trio': '0.23.1',
    'trio-websocket': '0.11.1',
    'urllib3': '2.0.7',
    'wheel': '0.38.4',
    'wsproto': '1.2.0'
}
    install_dependencies(packages)