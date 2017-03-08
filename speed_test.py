
# Required Python Packages
import pyspeedtest


def speed_in_units(speed):
    """
    Convert internet speed in proper units
    :param speed:
    :return:
    """
    units = ['bps', 'Kbps', 'Mbps', 'Gbps']
    unit = 0
    while speed >= 1024:
        speed /= 1024
        unit += 1
    return '%0.2f %s' % (speed, units[unit])


def get_internet_speed():
    """
    To get the internet speed
    :return:
    """

    st = pyspeedtest.SpeedTest()
    st.ping()
    download_speed = st.download()
    upload_speed = st.upload()

    print "\nDownload Speed :: {}".format(download_speed)
    print "Upload Speed :: {}".format(upload_speed)

    print "\n>>>> Download ans Upload Speed in proper units <<<<\n"
    print "Download Speed :: {}".format(speed_in_units(download_speed))
    print "Upload Speed :: {}".format(speed_in_units(upload_speed))

if __name__ == "__main__":
    get_internet_speed()
