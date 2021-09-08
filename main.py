import tkinter as tk
import subnetPro_Calc as sc

window = tk.Tk()
window.title("Subnet Calculator")
window.geometry("400x250")

ip_address = tk.StringVar(window)
sub_mask = tk.StringVar(window)
network_address = tk.StringVar(window)
broadcast_address = tk.StringVar(window)
hosts_count = tk.StringVar(window)
ip_range = tk.StringVar(window) 

def calculate():
	ip = ip_address.get()
	mask = int(sub_mask.get())
	sub_mask.set(sc.get_subnet_mask(ip, mask))
	network_address.set(sc.get_network_addr(ip, mask))
	broadcast_address.set(sc.get_broadcast_addr(ip, mask))
	hosts_count.set(sc.get_available_hosts_count(ip, mask))
	ip_range.set(sc.get_ip_address_range(ip, mask))

def clear():
	ip_address.set("")
	sub_mask.set("")
	network_address.set("")
	broadcast_address.set("")
	hosts_count.set("")
	ip_range.set("")

tk.Label(window,text = "IP Address").grid(row=3,column=0)
fr_ip_address = tk.Entry(window,textvariable=ip_address)
fr_ip_address.grid(row=3,column=1)

tk.Label(window,text = "Subnet Mask").grid(row=4,column=0)
fr_sub_mask = tk.Entry(window,textvariable=sub_mask)
fr_sub_mask.grid(row=4,column=1)

tk.Label(window,text = "Network Address").grid(row=5,column=0)
fr_network_address = tk.Entry(window,textvariable=network_address)
fr_network_address.grid(row=5,column=1)

tk.Label(window,text = "Broadcast Address").grid(row=6,column=0)
fr_broadcast_address = tk.Entry(window,textvariable=broadcast_address)
fr_broadcast_address.grid(row=6,column=1)

tk.Label(window,text = "Available Hosts").grid(row=7,column=0)
fr_hosts_count = tk.Entry(window,textvariable=hosts_count)
fr_hosts_count.grid(row=7,column=1)

tk.Label(window,text = "IP Range").grid(row=8,column=0)
fr_ip_range = tk.Entry(window,textvariable=ip_range)
fr_ip_range.grid(row=8,column=1)

tk.Button(window,text="Submit",command = calculate).grid(row=15,column=0)
tk.Button(window,text="Clear",command = clear).grid(row=15,column=1)

tk.Label(window,text = "IP Address format: 192.168.1.4").grid(row=20,column=0)
tk.Label(window,text = "Subnet Mask format: 21").grid(row=22,column=0)

window.mainloop()
