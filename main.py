from selenium import webdriver
import os
import click
import requests
import subprocess
from sys import exit
import threading
from queue import Queue

@click.group()
def cli():
    pass

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
PURPLE = "\033[0;35m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"


banner=f"""
$$$$$$$\                      $$\                  $$$$$$\  $$\           $$\        $$\            $$$$$$\      $$$$$$\  
$$  __$$\                     $$ |                $$  __$$\ \__|          $$ |       $$ |          $$  __$$\    $$$ __$$\ 
$$ |  $$ | $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$ /  \__|$$\  $$$$$$\  $$$$$$$\ $$$$$$\         \__/  $$ |   $$$$\ $$ |
$$$$$$$  |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ \$$$$$$\  $$ |$$  __$$\ $$  __$$\\_$$  _|         $$$$$$  |   $$\$$\$$ |
$$  ____/ $$ |  \__|$$ /  $$ |$$ |  $$ |$$$$$$$$ | \____$$\ $$ |$$ /  $$ |$$ |  $$ | $$ |          $$  ____/    $$ \$$$$ |
$$ |      $$ |      $$ |  $$ |$$ |  $$ |$$   ____|$$\   $$ |$$ |$$ |  $$ |$$ |  $$ | $$ |$$\       $$ |         $$ |\$$$ |
$$ |      $$ |      \$$$$$$  |$$$$$$$  |\$$$$$$$\ \$$$$$$  |$$ |\$$$$$$$ |$$ |  $$ | \$$$$  |      $$$$$$$$\ $$\\$$$$$$  /
\__|      \__|       \______/ \_______/  \_______| \______/ \__| \____$$ |\__|  \__|  \____/       \________|\__|\______/ 
                                                                $$\   $$ |                                                
                                                                \$$$$$$  |                                                
                                                                 \______/           
                                                                                                       
                                                                                                                                             
                                                      {GREEN}   - by lowkey
                                                                - github:https://github.com/lowkeycrack/
                                                                - to collab DM insta: @kriis._.x05
                                                                - youtube comming soon!!!                              {END}        """

def check_sudo():
    return 'SUDP_USER' in os.environ


def get_fingerprint(command):
    result=subprocess.Popen(command,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    stdout,stderr=result.communicate()
    if result.returncode==0:
        fp=stdout.decode('utf-8')
        return fp
    else:
        pass

def get_urls(command):
    result=subprocess.Popen(command,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    stdout,stderr=result.communicate()
    if result.returncode==0:
        fp=stdout.decode('utf-8')
        return fp
    else:
        pass

def get_response(url,method):

    if method=='GET':
        response=requests.get(url=f'http://{url}')
    elif method=='POST':
        response=requests.post(url=f'http://{url}')

        if response.status_code==200:
            return response.text
    else:
        return "NOT FOUND"


def get_ss(driver,sub):

    page=driver.get('http://'+sub)
    try:
        alert=driver.switch_to.alert
        alert.accept()
    except:
        pass
    driver.save_screenshot(sub+'.png')

def get_ports(command):
    try:
        print(command)
        process=subprocess.Popen(command,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        process.wait()
        stdout,stderror=process.communicate()

        if process.returncode==0:
            result=stdout.decode('utf-8')
            return result
        else:
            print(f"couldn't run command : {command}")

    except subprocess.CalledProcessError :
        print("couldn't run command")



def get_probe(subx,result):
    alive=[]
    while not subx.empty():
        subdomain=subx.get()
        try:
            res=requests.get(f"https://{subdomain}")
            if res.status_code == 404:
                pass
            else:
                print(f"{BLUE}{subdomain}{END}---{BLINK}>>{END}{GREEN}[{res.status_code}]{GREEN} {YELLOW}[{res.headers.get('server','N/A')}]{END}")
                result.put(subdomain)
        except:
            pass

def probe_domain(domain):
    res=requests.get(f"http://{domain}")

    if res.status_code==404:
        pass

    else:
        print(f"{BLUE}{domain}{END}---{BLINK}>>{END}{GREEN}[{res.status_code}]{GREEN} {YELLOW}[{res.headers.get('server','N/A')}]{END}")
            
@cli.command(help="Take ss of the list of subdomains")
@click.option('-fn','--filename',help="filename containing subdomains")
@click.option('-d','--domain',help="Name of a subdomain format:[-d subdomain.example.com]")
@click.option('-t','--threads',help="Number of threads",default=3,type=int)
def ss(filename,domain,threads):
    try:
        if filename:
            with open(filename,'r') as sub_file:
                subdomains=sub_file.read().splitlines()
            subs=Queue()
            drivers=[]

            for sub in subdomains:
                subs.put(sub)
            def start(queue,drivers):
                options=webdriver.FirefoxOptions()
                options.headless=True
                driver=webdriver.Firefox(options=options,)

                while not queue.empty():
                    sub=queue.get()
                    get_ss(driver,sub)
                    drivers.append(driver)
                driver.close()

            for _ in range(threads):
                ss_thread=threading.Thread(target=start,args=(subs,drivers,))
                ss_thread.start()

        elif domain:
            options=webdriver.FirefoxOptions()
            options.headless=True
            driver=webdriver.Firefox(options=options)
            get_ss(driver,domain)

        else:
            print("Neither a filename of domain specified [^] \nsuch an imbecile ")

    except:
        print("""Usage: main.py ss [OPTIONS]

couldn't start the function parameters were missing[*]
              
Options:
  -fn, --filename TEXT  filename containing subdomains
  --help                Show this message and exit.
               
  Make sure all the required parameters have been provided succesflly
  try:'python main.py fingerprint --filename test.txt'    """)



@cli.command(help="probe a list of subdomains for alive and the server running")
@click.option('-fn','--filename',help="filename containing subdomains")
@click.option('-t','--threads',help="Number of threads",default=10,type=int)
@click.option('-o','--output',help="Name of the output file")
@click.option('-d','--domain',help="Name of a subdomain format:[-d subdomain.example.com]")
def probe(filename,threads,domain,output):
    try:
        if filename:
            with open(filename,'r') as subs:
                subdomains=subs.read().splitlines()
            subx=Queue()
            result=Queue()
            for sub in subdomains:
                subx.put(sub)
            for _ in range(threads):
                probe_thread=threading.Thread(target=get_probe,args=(subx,result,))
                probe_thread.start()
                probe_thread.join()
            if output:
                with open(output,'w') as output_file:
                    while not result.empty():
                        output_file.write(result.get()+'\n')
        elif domain:
            flag=False
            if probe_domain(domain):
                flag=True
            if output:
                if flag:
                    with open(output,'w') as o:
                        o.write(domain)

        else:
            print("Filename was not specified make sure to use '-fn' to add a filename or -d fot domain \nuse --help for more information...")


    except:
        print("")



@cli.command(help="Fingerprint a list of subdomains")
@click.option('-fn','--filename',help="filename containing subdomains")
@click.option('-o','--output',help="output file")
@click.option('-d','--domain',help="Name of a subdomain format:[-d subdomain.example.com]")
@click.option('-ag','--aggression',type=int,help="The level of aggression [1.stealthy, 2.aggressive, 3.heavy] (e.g '-ag 1') default=1",default=1)
def fingerprint(filename,output,domain,aggression):
    try:
        if filename:
            result={}
            with open(filename,'r') as sub_file:
                subdomains=sub_file.read().splitlines()

            for sub in subdomains:
                command=f"whatweb --aggression {aggression} {sub}"
                fp=get_fingerprint(command)

                if fp:
                    result[sub]=fp
                else:
                    result[sub]="Couldn't find anything"

            for sub, fp in result.items():
                print(f"------------------------------------{BLUE}scan results for{RED}{BLINK} {sub}{END}------------------------------------")
                print(fp)

            if output:
                with open(output,'w') as op:
                    for sub, fp in result.items():
                        op.write(f"------------------------------------scan results for {sub}------------------------------------")
                        op.write(fp)

        elif domain:
            command=f"whatweb --aggression {aggression} {domain}"
            result=get_fingerprint(command)
            print(result)
            if output:
                with open(output,'w') as o:
                    o.write(result)
        else:
            pass
    except:
        print("""Usage: main.py fingerprint [OPTIONS]

couldn't start the function parameters were missing[*]

Options:
  -fn, --filename TEXT       filename containing subdomains
  -o, --output TEXT          output file
  -ag, --aggression INTEGER  The level of aggression [1.stealthy,
                             2.aggressive, 3.heavy] (e.g '-ag 1')
                             default=1
  --help                     Show this message and exit.
              
  Make sure all the required parameters have been provided succesflly
  try:'python main.py fingerprint --filename test.txt'""")



@cli.command(help="Find the active ports using nmap")
@click.option('-fn','--filename',help="filename containing subdomains")
@click.option('-o','--output',help="output file")
@click.option('-d','--domain',help="Name of a subdomain format:[-d subdomain.example.com]")
@click.option('-st','--scantype',help='change the scan type from nmap[default ="sS"="stealth-scan"]',default="-sS")
def ports(filename,output,scantype,domain):
    if check_sudo:
        if filename:
            scan_result={}
            with open(filename,'r') as subs:
                subdomains=subs.read().splitlines()

            for subdomain in subdomains:
                print(f"------------------------------------{BLUE}scan results for {RED}{BOLD}{BLINK}{subdomain}{END} ------------------------------------")
                command=f"nmap {scantype} -p0-65535 {subdomain}"
                result=get_ports(command)

                if result:
                    print(result)
                    scan_result[subdomain]=result

            if output:
                with open(output,'w') as op:
                    for sub,scan in scan_result.items():
                        op.write(f"------------------------------------scan results for {sub}------------------------------------"+scan +"\n")      
        
        elif domain:
            command=f"nmap {scantype} -p0-65535 {domain}"
            print(f"------------------------------------{BLUE}scan results for {RED}{BOLD}{BLINK}{domain}{END} ------------------------------------")
            result=get_ports(command)
            print(result)

            if output:
                with open(output, 'w') as o:
                    o.write(result)

    else:
        print("The scan requires root previleges\nrun using [sudo] you dummy!!!")   
        exit(0)



@cli.command(help="Get the page data of a list of subdomains")
@click.option('-fn','--filename',help="filename containing subdomains")
@click.option('-o','--output',help="output file")
@click.option('-d','--domain',help="Name of a subdomain format:[-d subdomain.example.com]")
@click.option('-m','--method',help='the method of the request',default='GET')
def request(filename,output,method,domain):
    if filename:

        with open(filename,'r') as ofile:
            urls=ofile.read().splitlines()
        result={}

        for url in urls:
            result[url]=get_response(url,method)

        for sub,res in result.items():
            print(f"------------------------------------{BLUE}scan results for {RED}{BOLD}{BLINK}{sub}{END} ------------------------------------")
            print(f"{res}")

        if output:
            with open(output,'w') as out:
                for sub,res in result:
                    out.write(f"------------------------------------{BLUE}scan results for {RED}{BOLD}{BLINK}{sub}{END} ------------------------------------ \n {res}")

    if domain:
        print(f"------------------------------------{BLUE}scan results for {RED}{BOLD}{BLINK}{domain}{END} ------------------------------------")
        res=get_response(domain,method)
        print(res)

        if output:  
            with open(output,'w') as o:
                o.write(res)

        
@cli.command(help="Find a list of opensource urls available of a list of subdomains")
@click.option('-fn','--filename',help="filename containing the subdomains")
@click.option('-o','--output',help="output file")
@click.option('-d','--domain',help="Name of a subdomain format:[-d subdomain.example.com]")
def urls(filename,output,domain):
    if filename:
        with open(filename, 'r') as ofile:
            subs=ofile.read().splitlines()
        results={}
        print("This may take a while")

        for sub in subs:
            command= f"waybackurls {sub}"
            result=get_urls(command)
            results[sub]=result
            print(f"------------------------------------{BLUE}URLs for {RED}{BOLD}{BLINK}{sub}{END} ------------------------------------")
            print(f"\n{result}")

        if output:
            with open(output,'w') as ofile:
                for sub,result in results.items():
                    ofile.write(f"------------------------------------{BLUE}URLs for {RED}{BOLD}{BLINK}{sub}{END} ------------------------------------")
                    ofile.write(f"\n{result}")

    elif domain:
        command=f"waybackurls {domain}"
        result=get_urls(command)
        print(result)
        if output:
            with open(output,'w') as o:
                o.write(result)


@cli.command(help="run all the scans and put every single subdomain in a single directory")
@click.option('-fn','--filename',help="Name of the file containing subdomains")
@click.option('-st','--scantype',help="The scantyp to be used in nmap default = '-sT','stealthscan'",default="-sS")
@click.option('-m','--method',help="method to be used default = [GET]",default="GET")
@click.option('-ag','--aggression',type=int,help="The level of aggression [1.stealthy, 2.aggressive, 3.heavy] (e.g '-ag 1') default=1",default=1)
def run(filename,scantype,method,aggression):
    if check_sudo():
        with open(filename,'r') as sfile:
            subs=sfile.read().splitlines()
        path=os.getcwd()

        for sub in subs:
            sub_path=os.path.join(path,sub)
            os.makedirs(sub_path)
            os.chdir(sub_path)

            url_command=f"waybackurls {sub}"
            result=get_urls(url_command)
            with open("urls.txt",'w') as ufile:
                ufile.write(result)

            port_command=f"nmap {scantype} -p0-65535 {sub}"
            result=get_ports(port_command)
            with open('ports.txt','w') as ports:
                ports.write(get_ports(port_command))

            result=get_response(sub,method)
            with open('response.txt','w') as rfile:
                rfile.write(result)

            fin_command=f"whatweb -aggressive {aggression},{sub}"
            result=get_fingerprint(fin_command)
            with open('fingerprint.txt','w') as ffile:
                ffile.write(result)
            os.chdir('../')
        
    else:
        print("Run the program through sudo dummy")


if __name__ == "__main__":
    print(banner)
    cli()



