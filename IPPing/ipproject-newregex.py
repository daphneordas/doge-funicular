import subprocess
import re


def ping_ips():
    user_ip_input = input("Input comma separated ip addresses: ")
    # process the user input (string separated by commas) into list
    user_ip_list = user_ip_input.split(",")

    for ip in user_ip_list:
        triplet = ip.split(".")
        # to cover cases like 1.1.1.1.1 or 123
        if len(triplet) != 4:
            print("%s is an invalid ip address, please re-enter only valid ip addresses." % ip)
            return
        # check if each item in list is a valid ip (0.0.0.0 - 256.256.256.256)
        for i in range(0, 4):
            if int(triplet[i]) > 256 or int(triplet[i]) < 0:
                print("%s is an invalid ip address, please re-enter only valid ip addresses." % ip)
                return

        # for each ip, open cmd line and call ping/tracert
        print("Pinging user provided ip addresses...")
        modified_ip = re.sub('\.[0]*', '.', ip)
        try:
            ping_command_output = subprocess.check_output(["ping", modified_ip]).decode('utf-8')
            # put the regular expression in compile (like the search terms)
            ping_regex = re.compile(r'Reply from \d*.\d*.\d*.\d*: bytes=\d* time=\d*ms TTL=\d*')
            # actually does the searching for you
            digits = ping_regex.search(ping_command_output)
            print("%s pinged, >> request successful" % modified_ip)
            print("This was the first reply: %s" % digits.group())

        except subprocess.CalledProcessError:
            print("%s pinged, >> request timed out" % ip)
            # print(f"{modified_ip} pinged, >> request timed out")
            # print("{ip} pinged, >> request timed out".format(ip=ip))


if __name__ == "__main__":
    ping_ips()
