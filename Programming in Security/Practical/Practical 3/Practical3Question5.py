def swap(ports):
    value = int(input("Enter port: "))
    temp = {p:s for s,p in ports.items()}
    if value in temp:
        print(f'{temp[value]} service is running on port {value}')
    else:
        print(f'{value} not found!')

ports = {}
port_open = input("Please enter service:port that were found to be open, separated by '|'\n").upper()
pairs = port_open.split(sep="|")

for pair in pairs:
    svc = pair.split(":")
    ports[svc[0].strip()]=int(svc[1].strip())

print(f'\nThese are the open ports found and their corresponding services.')
for port,services in ports.items():
    print(f'{port}:{services}')

request = " "
while request != "":
    print(f'1) Search for open port\n2) Search for service running\n3. Update dictionary')
    request = input("Please enter request: ")
    if request == "1":
        swap(ports)
    elif request == "2":
        service = input("Enter service: ").upper()
        if service in ports:
            print(f'{service} is running on port {ports[service]}.')
        else:
            print(f'{service} is not found.')
    elif request == "3":
        service_entered = input("Please enter service: ").upper()
        port_entered = int(input("Please enter port: "))
        new_entry = {service_entered:port_entered}
        ports.update(new_entry)
        print(ports)
        
