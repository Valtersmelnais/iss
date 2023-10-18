day = input("Kāda šodien diena?: ")
music_volume = int(input("Kāds ir mūzikas skaļums?: "))

loud = music_volume > 40

if day == "pirmdiena" or day == "svētdiena" and not loud:
    print("Skaļums ir pieņemams")
elif day == "pirmdiena" or day == "svētdiena" and loud:
    print("Baigi skaļi")
elif day != "pirmdiena" or day != "svētdiena" and loud or not loud:
    print("Skaļums ir pieņemams")