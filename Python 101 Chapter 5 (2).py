downloadedapps = {}

def check_downloadedapps (name):
    if downloadedapps.get(name):
        print ("Downloaded on device")
    else:
        downloadedapps[name] = True
        print ("App not downloaded")

check_downloadedapps ("Maps")
