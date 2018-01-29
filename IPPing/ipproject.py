import subprocess
import re


def ping_ips():
    user_ip_input = input("Input comma separated ip addresses: ")
    # user_ip_input = '172.217.003.163'
    # process the user input (string separated by commas) into list
    user_ip_list = user_ip_input.split(",")

    # check if each item in list is a valid ip (0.0.0.0 - 256.256.256.256)
    stripped_ip_list = []
    for ip in user_ip_list:
        triplet = ip.split(".")
        # to cover cases like 1.1.1.1.1 or 123
        if len(triplet) != 4:
            print("%s is an invalid ip address, please re-enter only valid ip addresses." % ip)
            return
        modified_ip = []
        for i in range(0, 4):
            triplet_check = triplet[i].lstrip("0")
            # needed if all digits in the triplet is 0
            if not triplet_check:
                triplet_check = 0
            if int(triplet_check) > 256 or int(triplet_check) < 0:
                print("%s is an invalid ip address, please re-enter only valid ip addresses." % ip)
                return
            modified_ip.append(str(triplet_check))
        stripped_ip = '.'.join(modified_ip)
        stripped_ip_list.append(stripped_ip)

    # for each ip, open cmd line and call ping/tracert
    print("Pinging user provided ip addresses...")
    for ip in stripped_ip_list:
        try:
            ping_command_output = subprocess.check_output(["ping", ip]).decode('utf-8')
            # put the regular expression in compile (like the search terms)
            ping_regex = re.compile(r'Reply from \d*.\d*.\d*.\d*: bytes=\d* time=\d*ms TTL=\d*')
            # actually does the searching for you
            digits = ping_regex.search(ping_command_output)
            print("%s pinged, >> request successful" % ip)
            print("This was the first reply: %s" % digits.group())

        except subprocess.CalledProcessError:
            print(f"{ip} pinged, >> request timed out")
            # print("{ip} pinged, >> request timed out".format(ip=ip))


if __name__ == "__main__":
    ping_ips()
    # timeit.timeit('ping_ips()','from __main__ import ping_ips')