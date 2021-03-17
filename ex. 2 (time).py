sec = int(input("Enter q. of seconds: "))
hours = int(sec // 3600)
minutes = int((sec - (hours * 3600)) // 60)

if sec % 3600 == 0:
    print(f"{hours}:00:00")
elif sec % 60 == 0:
    print(f"{hours}:{minutes}:00")
else:
    print(f"{hours}: {minutes}: {sec - (minutes * 60) - (hours * 3600)}")


