def b_string_to_ipv4(b_str):
	new_str = ""
	for i in range(0,32,8):
		new_str = new_str + str(int(b_str[i:i+8],2))
		if i != 24:
			new_str += "."
	return new_str

def get_binary_ip_submask_network_broadcast(ip, sub_mask):
	ip_lst = ip.strip().split(".")
	b_ip = "".join(["{:0>8b}".format(int(x)) for x in ip_lst])
	b_sub_mask = "".join(['1' if i < sub_mask else '0' for i in range(32)])
	b_net_addr = int(b_ip,2) & int(b_sub_mask,2)
	b_net_addr = "{:0>32b}".format(int(b_net_addr))
	b_broad_addr = "".join([b_net_addr[i] if i < sub_mask else '1' for i in range(32)])
	return b_ip, b_sub_mask, b_net_addr, b_broad_addr


def get_subnet_mask(ip,sub_mask):
	b_sub_mask = "".join(['1' if i < sub_mask else '0' for i in range(32)])
	return b_string_to_ipv4(b_sub_mask)


def get_network_addr(ip, sub_mask):
	b_ip, b_sub_mask, b_net_addr, b_broad_addr = (get_binary_ip_submask_network_broadcast(ip, sub_mask))
	net_addr = b_string_to_ipv4(b_net_addr)
	return net_addr


def get_broadcast_addr(ip, sub_mask):
	b_ip, b_sub_mask, b_net_addr, b_broad_addr = (get_binary_ip_submask_network_broadcast(ip, sub_mask))
	b_broad_addr = "".join([b_net_addr[i] if i < sub_mask else '1' for i in range(32)])
	return b_string_to_ipv4(b_broad_addr)


def get_available_hosts_count(ip,sub_mask):
	hosts_count = 2**(32-sub_mask) - 2
	return hosts_count


def get_ip_addr_range(ip,sub_mask):
	b_ip, b_sub_mask, b_net_addr, b_broad_addr = (get_binary_ip_submask_network_broadcast(ip, sub_mask))
	b_ip_addr_start = "{:0>32b}".format(int(b_net_addr,2) + int("1"))
	b_ip_addr_end = "{:0>32b}".format(int(b_broad_addr,2) - int("1"))
	ip_addr_range = f"{b_string_to_ipv4(b_ip_addr_start)} - {b_string_to_ipv4(b_ip_addr_end)}"
	return ip_addr_range


if __name__ == "__main__":
	ip = input("Please enter the ip: ")
	ip_lst = ip.strip().split(".")
	sub_mask = int(input("Please enter the subnet mask: "))
	print(f"IP address: {ip}")
	print(f"Subnet mask: {get_subnet_mask(ip, sub_mask)}")
	print(f"Network address: {get_network_addr(ip, sub_mask)}")
	print(f"Broadcast address: {get_broadcast_addr(ip, sub_mask)}")
	print(f"Available hosts: {get_available_hosts_count(ip, sub_mask)}")
	print(f"Ip address range: {get_ip_addr_range(ip, sub_mask)}")


