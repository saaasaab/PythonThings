from Trytes_All import TRYTES
import string
all_printable = string.printable

print(all_printable)


ascii_tryte={}
pattern = []
for index,i in enumerate(all_printable):

    #thisdict["color"] = TRYTES[index]
    pattern=[]
    for j in TRYTES[index]:
        num=int(j[0])
        for k in range(num):
            pattern.append(j[1])
    ascii_tryte[i] = pattern
    pattern = []



TEXT = "Hello World, My name is Scott Laughlin"

message_tryted = []
for i in TEXT:
    message_tryted.append(ascii_tryte[i])

flat_list = [item for sublist in message_tryted for item in sublist]

print(flat_list)
