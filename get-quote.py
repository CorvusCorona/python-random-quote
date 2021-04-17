from random import sample

def main():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  # print out more than one random quote from array
  # print(sample(quotes, 2))

  # print the quotes without extra characters
  print(''.join([str(i) for i in quotes]))

  # for i in quotes:
  #   print(i)

if __name__== "__main__":
  main()
