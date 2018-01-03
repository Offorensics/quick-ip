import subprocess

def make_choice():
	cmd = 'zenity --list --title "IPv4 Quick Change" --text "Select address below" --radiolist --column "Choice" --column "Address" \
	TRUE "192.168.1.2" FALSE "192.168.3.2" FALSE 192.168.4.2 FALSE "192.168.9.2" 2>/dev/null'
	choice = subprocess.check_output([cmd], shell=True).decode('utf-8').strip()
	return choice


def change_ip(addr):
	net_set_f = "/etc/network/interfaces"

	with open("zenity_ip_interface.cfg") as quick:
		interface = quick.read().strip()

	new_settings = ("# interfaces(5) file used by ifup(8) and ifdown(8)\n"
			"auto lo\n"
			"iface lo inet loopback\n\n"
			"auto " + interface + "\n"
			"iface " + interface + " inet static\n\n"
			"address " + addr + "\n"
			"netmask 255.255.255.0\n")

	with open(net_set_f, "w") as f:
		f.write(new_settings)

	cmd = "sudo ifdown " + interface + " && sudo ifup " + interface
	subprocess.Popen([cmd], shell=True)

change_ip(make_choice())
