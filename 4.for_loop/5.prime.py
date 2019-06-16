no=int(input('Enter ur no:'))
srt= int(no**0.5)
for i in range(2,srt+1):
    if no%i==0:
        print('no is not prime')
        break
else:
    print('no is prime')