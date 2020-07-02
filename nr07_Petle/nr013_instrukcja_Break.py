for candidate in range(1,31):



    for divider in range(2,candidate):
        if candidate % divider == 0:


            print('%2d is not a prime number - divider is %2d' % (candidate,divider))
            break
    else: #w przypadku nie użycia break to wykona się funkcja else
        print('%2d is prime'%candidate)