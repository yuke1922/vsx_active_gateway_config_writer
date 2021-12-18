import os
import csv

#Clear screen for output
os.system('clear')
os.system('rm -rf *outfile*')

vsx1_outfile = "vsx1_outfile.txt"
vsx2_outfile = "vsx2_outfile.txt"

print("Importing CSV")

csvfile = 'vsx_ag_import.csv'

with open(csvfile) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        vlan = row['vlan']
        netmask = row['netmask']
        ag_ip = row['ag_ip']
        vsx1_ip = row['vsx1_ip']
        vsx2_ip = row['vsx2_ip']
        vmac = row['vmac']

        vsx1_writer = open(vsx1_outfile, 'a')
        vsx1_writer.write("interface vlan " + vlan + "\n ip address " + vsx1_ip + "/" + netmask + "\n active-gateway ip mac " + vmac + "\n active-gateway ip " + ag_ip + "\n no shutdown\n exit\n!\n")
        vsx1_writer.close()


        vsx2_writer = open(vsx2_outfile, 'a')
        vsx2_writer.write("interface vlan " + vlan + "\n ip address " + vsx2_ip + "/" + netmask + "\n active-gateway ip mac " + vmac + "\n active-gateway ip " + ag_ip + "\n no shutdown\n exit\n!\n")
        vsx2_writer.close()


print("Done!")
