
import speedtest
from datetime import date, time, datetime

itWorked = 0


def speedTest():
    test = speedtest.Speedtest()

    ########## To measure download speed
    print("\nPerforming download speed test...")
    downloadSpeedTestRes = test.download()
    print(f"Download Speed = {downloadSpeedTestRes:.2f} bps = {downloadSpeedTestRes/pow(1024,2):.2f} Mbps")
    downloadSpeedTestRes = round(downloadSpeedTestRes/pow(1024, 2), 2)

    ########## To measure upload speed
    print("\nPerforming upload speed test...")
    uploadSpeedTestRes = test.upload()
    print(f"Upload Speed = {uploadSpeedTestRes:.2f} bps = {uploadSpeedTestRes/pow(1024,2):.2f} Mbps")
    uploadSpeedTestRes = round(uploadSpeedTestRes/pow(1024, 2), 2)

    ########## Pinging the network
    print("\nPerforming ping test...")
    pingRes = test.results.ping
    print(f"Ping (the response time of your connection) = {pingRes:.2f} ms\n")

    return downloadSpeedTestRes, uploadSpeedTestRes, pingRes



try:
    [downloadSpeedTestRes, uploadSpeedTestRes, pingRes] = speedTest()
    itWorked = 1
except:
    time.sleep(15)
    try:
        [downloadSpeedTestRes, uploadSpeedTestRes, pingRes] = speedTest()
        itWorked = 1
    except:
        print("SPEED TEST FAILED: Computer not connected to internet!")


updateLog = open("executionLog.txt", "a")
if(itWorked):
    updateLog.write(
                        f"\n\nInternet speed test succeeded at " + str(datetime.now().strftime("%H:%M:%S"))
                        + " on " + str(date.today())
                        + f"\n\tDownload Speed = {downloadSpeedTestRes} Mbps"
                        + f"\n\tUpload Speed = {uploadSpeedTestRes} Mbps"
                        + f"\n\tPing duration = {pingRes} Mbps"
                    )
else:
    updateLog.write(
                        # f"Internet speed test failed at " + time + " on " + date
                    )

updateLog.close()
print("\n###################### Execution log updated succesfully. ##############################\n")