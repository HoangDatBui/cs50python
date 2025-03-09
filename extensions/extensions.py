extension = input("File name: ").strip()
if extension.endswith(".jpeg") or extension.endswith(".jpg"):
    print("image/jpeg")
elif extension.endswith(".gif"):
    print("image/gif")
elif extension.endswith(".png"):
    print("image/png")
elif extension.endswith(".pdf") or extension.endswith(".PDF"):
    print("application/pdf")
elif extension.endswith(".txt"):
    print("text/plain")
elif extension.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
