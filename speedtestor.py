import speedtest
import datetime
import time
import csv

INTERVAL = 1800  # sec
SAMPLE_NUM = 10

threads = None

if __name__ == "__main__":
    servers = []
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()

    with open("results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "download", "upload"])

    while True:
        base_time = time.time()
        date = datetime.datetime.now()
        d_speed = 0.0
        u_speed = 0.0
        for i in range(SAMPLE_NUM):
            d_speed += s.download(threads=threads)
            u_speed += s.upload(threads=threads)
        d_speed /= SAMPLE_NUM
        u_speed /= SAMPLE_NUM

        with open("results.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date.strftime("%Y年%m月%d日 %H:%M:%S"), d_speed, u_speed])
        next_time = INTERVAL - abs(base_time - time.time())
        time.sleep(next_time)
