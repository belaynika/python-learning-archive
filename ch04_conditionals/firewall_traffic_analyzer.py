# DESCRIPTION:  program monitors data transfers to a network and the risk assessment is based on the port number

print("=== Network Traffic Security Analyzer ===")
print()
port_number = int(input("Enter the port number (e.g., 80, 22, 443, 3389): "))
transfer_size = int(input("Enter the data transfer size in megabytes (MB): "))
print()

if port_number == 22 or port_number == 3389 and transfer_size > 100:    # conditionals determine which output
    print("FIREWALL LOG:")
    print(f"Port: {port_number}, Transfer Size: {transfer_size} MB")
    print("Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!")
    print("------------------------")
elif port_number == 80 and transfer_size > 100:
    print("FIREWALL LOG:")
    print(f"Port: {port_number}, Transfer Size: {transfer_size} MB")
    print("Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.")
    print("------------------------")
elif port_number == 443:
    print("FIREWALL LOG:")
    print(f"Port: {port_number}, Transfer Size: {transfer_size} MB")
    print("Risk Assessment: LOW RISK: Secure encrypted transfer detected.")
    print("------------------------")
else:
    print("FIREWALL LOG:")
    print(f"Port: {port_number}, Transfer Size: {transfer_size} MB")
    print("Risk Assessment: UNKNOWN: Unrecognized traffic pattern.")
    print("------------------------")