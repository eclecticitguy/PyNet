from ex1_ip_addr_class import IPAddress


class IPAddressWithNetmask(IPAddress):

    def __init__(self, ip_addr):

        (ip_addr, netmask) = ip_addr.split("/")
        self.netmask = "/" + netmask

        IPAddress.__init__(self, ip_addr)

    def netmask_in_dotdecimal(self):

        netmask = int(self.netmask.strip("/"))

        # For every bit in the netmask, set string to 1
        one_string = '1' * netmask

        # For every bit outside of netmask, set string to 0
        zero_string = '0' * (32 - netmask)

        # Concatenate 1's and 0's to form a 32-bit binary representation of netmask
        netmask_str = one_string + zero_string

        # Strip parts of netmask to obtain octets
        octet1 = netmask_str[:8]
        octet2 = netmask_str[8:16]
        octet3 = netmask_str[16:24]
        octet4 = netmask_str[24:32]

        netmask_tmp = [octet1, octet2, octet3, octet4]

        for i, octet in enumerate(netmask_tmp):
            netmask_tmp[i] = str(int(octet, 2))

        return '.'.join(netmask_tmp)


def main():

    test2_ip = IPAddressWithNetmask('192.168.1.1/24')

    print
    print "%15s: %-40s" % ("IP", test2_ip.ip_addr)
    print "%15s: %-40s" % ("Netmask", test2_ip.netmask)
    print "%15s: %-40s" % ("Binary IP", test2_ip.display_in_binary())
    print "%15s: %-40s" % ("Hex IP", test2_ip.display_in_hex())
    print "%15s: %-40s" % ("IP Valid", test2_ip.is_valid())
    print "%15s: %-40s" % ("Netmask dot dec", test2_ip.netmask_in_dotdecimal())
    print


if __name__ == "__main__":
    main()
