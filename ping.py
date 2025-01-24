# Prompt the user to input a network address
network = input("Enter a network address in CIDR format(ex.192.168.1.0/24): ")

# Create the network
ip_net = ipaddress.ip_network(network)

# Get all hosts on that network
all_hosts = list(ip_net.hosts())

# Create output file in preset directory
os.chdir("C:\\Python364\\Output")
onlineHosts = "Online_Hosts.txt"
offlineHosts = "Offline_Hosts.txt"
on  = open(onlineHosts, 'a') # File object 'on' is created with append mode
off = open(offlineHosts, 'a') # File object 'off' is created with append mode

# Configure subprocess to hide the console window
info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

# For each IP address in the subnet, 
# run the ping command with subprocess.popen interface
for i in range(len(all_hosts)):
    output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]

    if "Destination host unreachable" in output.decode('utf-8'):
        print(str(all_hosts[i]), "is Offline")
        result = str(all_hosts[i])
        off.write(result)

    elif "Request timed out" in output.decode('utf-8'):
        print(str(all_hosts[i]), "is Offline")
        result = str(all_hosts[i])
        off.write(result)
    else:
        print(str(all_hosts[i]), "is Online")
        result = str(all_hosts[i])
        on.write(result