import subprocess
import csv
from settings import settings
import os


def execute_speedtest():
    results_csv = subprocess.check_output("%s --csv --server %s"
                                          % (settings["speedtest_path"], settings["server_id"]),
                                          shell=True)
    results_csv = results_csv.decode()
    results_csv = results_csv.replace("\n", "").split(",")

    results_dict = {"server_id": results_csv[0], "server_sponsor": results_csv[1], "server_name": results_csv[2],
                    "timestamp": results_csv[3], "server_distance": results_csv[4], "ping": results_csv[5],
                    "download": results_csv[6], "upload": results_csv[7]}
    write_to_file(results_dict)


def write_to_file(results_dict):
    if not os.path.exists("log.csv"):
        with open("log.csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=settings["fieldnames"])
            writer.writeheader()
    with open("log.csv", "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=settings["fieldnames"])
        writer.writerow(results_dict)


def main():
    execute_speedtest()


if __name__ == "__main__":
    main()
