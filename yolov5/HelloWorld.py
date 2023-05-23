with open("C:\Users\manhc\yolov5\label.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())
        break