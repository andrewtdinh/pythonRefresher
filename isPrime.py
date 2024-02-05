def prime_checker(number):
  check_limit = number
  current_divisor = 2
  is_prime = True
  
  if number < 2:
    print("It's not a prime number.")
  elif number == 2 or number == 3:
    print("It's a prime number")
  else:
    while check_limit >= current_divisor:
      if number % current_divisor == 0:
        is_prime = False
        print("It's not a prime number.")
        break
      check_limit = number / current_divisor
      current_divisor += 1

    if is_prime:
      print("It's a prime number")