# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0.0
sum = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    ini = line.find(" ")
    fim = line.find("\n")
    slice = (line[ini:fim])
    N_slice = float(slice)
    sum = N_slice + somatoria
    count = count + 1
media = sum/count
print("Average spam confidence: " + str(media))
