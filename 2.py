import webbrowser

def download(urls):
    for k in urls:
        try:
            for i in range(3):
                if webbrowser.open(k):
                    break
        except:
            "Could not download!"
