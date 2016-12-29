import subprocess
import csv


def execute_speedtest():

    results_csv = subprocess.check_output("/home/dominik/.anaconda3/bin/speedtest --csv --server 3313" , shell=True)
    results_csv = results_csv.decode()
    results_csv = results_csv.replace("\n","").split(",")

    results_dict = {"server_id": results_csv[0], "server_sponsor": results_csv[1], "server_name": results_csv[2],
                    "timestamp": results_csv[3], "server_distance": results_csv[4], "ping": results_csv[5],
                    "download": results_csv[6], "upload": results_csv[7]}
    print(results_dict)

def main():
    execute_speedtest()


if __name__ == "__main__":
    main()
