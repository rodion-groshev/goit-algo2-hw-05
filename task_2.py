import json
import time

from datasketch import HyperLogLog

hll = HyperLogLog(p=14)


def read_logs():
    ip_lst = []
    with open("lms-stage-access.log") as file:
        for line in file:
            try:
                data = json.loads(line)
                ip = data.get("remote_addr")
                if ip:
                    update_hll(ip)
                    ip_lst.append(ip)
            except json.JSONDecodeError:
                continue
    return ip_lst


def update_hll(ip):
    hll.update(ip.encode("utf-8"))


def hll_count():
    return hll.count()


def set_count(ip_lst):
    return len(set(ip_lst))


def timer(func, *args):
    start_time = time.time()
    res = func(*args)
    time_diff = time.time() - start_time
    print(f"Unique elements: {res} | Time: {time_diff:.8f} | Method: {func.__name__}")


if __name__ == "__main__":
    ip_address = read_logs()
    timer(hll_count)
    timer(set_count, ip_address)
