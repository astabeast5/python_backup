import subprocess

# Check system info 

commands = [
    ['whoami'],
    ['pwd'],
    ['df', '-h'],
    ['docker','--version']
]

for cmd in commands:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"  {' '.join(cmd)}:")
        print(f"  {result.stdout.strip()}")
    except subprocess.CalledProcessError as e:
        print(f"  {' '.join(cmd)} failed: {e.stderr.strip()}")
    except FileNotFoundError:
        print(f"  {cmd[0]} command not found")


"""
EXPECTED OUTPUT is as follows:
 whoami  
dev-user  

 pwd  
~/projects/devops-demos  

 df -h  
Filesystem      Size  Used Avail Use% Mounted on  
/dev/simdisk     50G   12G   36G  25% /  
tmpfs           2.0G  1.2M  2.0G   1% /run  
/dev/data       200G   30G  170G  15% /home  

 docker --version  
Docker version 24.x.x, build a1b2c3d  
"""
    
