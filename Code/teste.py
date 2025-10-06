characters = ['t','a','c','o']
output = ''
length = len(characters)
i = 0
while(i < length):
    output = output + characters[i]
    i= i+1
lenght = length * -1
i = -2
while(i >= lenght):
    output = output + characters[i]
    i= i-1
print(output)
