import requests
import re
def sum (first,last):
    sum = 0
    for i in range(first, last+1):
        if i > 1:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                sum += i
    print("Sum of prime numbers in the range is:", sum)

def Unit_Conversion(value, direction):
    if direction == "M":
        result = value * 3.28
        return f"{round(result, 2)} F"
    elif direction == "F":
        result = value / 3.28
        return f"{round(result, 2)} M"
    else:
        print("Invalid ,either enter 'M' or 'F'.")
        return None

def Consonant_Counter(letter):
    consonant = "dcbfghjkmlnpqrstvwxyzBCDFGHJKLMNPQSQRTVWXZY"
    count = 0
    for char in letter:
        if char in consonant:
            count += 1
    print(f"The number of consonants in the string is: {count}")

def min_max():
    Data = []
    while True:
        value = input("Enter a number or ( type 'stop' to exit): ")
        if value.lower() == 'stop':  
            break
        try:
            num = float(value)  
            Data.append(num)  
        except ValueError:
            print(" enter a valid number, Please.")  
    if Data:  
        print("The smallest number you entered is:", min(Data))
        print("The greatest number you entered is:", max(Data))

def pali(p):
    new_name = p.replace(" ", "").lower()
    return new_name == new_name[::-1]

def word(https):
    try:
        reply = requests.get(https)
        reply.raise_for_status()  
        text = reply.text
        target_words = ["the", "was", "and"]  
        words = re.findall(r'\b\w+\b', text.lower())  
        counts = {word: words.count(word) for word in target_words}  
        print("Word counts:")
        for word, count in counts.items():
            print(f"{word}: {count}")
    except reply.exceptions.ReplyException as e:
        print(f"Error downloading the file: {e}")

# Display Menu and Handle User Input
def main():
    while True:
        print("\n--- Menu ---")
        print("1. Calculating the Sum of Prime Numbers")
        print("2. Converting the units of light")
        print("3. Count Consonants in String")
        print("4. Finding the Min-Max Numbers")
        print("5. Palindrome Checker")
        print("6. Word Counter (from URL)")
        print("0. Exit")
        
        choice = input("Select an option (1-6 or 0 to Exit): ")
        
        if choice == "1":
            first= int(input("Enter the starting range: "))
            last = int(input("Enter the ending range: "))
            sum(first, last)
        
        elif choice == "2":
            value = float(input("Enter the length value: "))
            direction = input("Enter the length direction ('M' for meters to feet, 'F' for feet to meters): ").upper()
            new_value = Unit_Conversion(value, direction)
            if new_value:
                print(f"Converted value: {new_value}")
        
        elif choice == "3":
            Alphabete = input("Enter a text string: ")
            Consonant_Counter(Alphabete)
        
        elif choice == "4":
            min_max()
        
        elif choice == "5":
            name = input("Enter the string: ")
            print("Is the string a palindrome?", pali(name))
        
        elif choice == "6":
            https = input("Enter the URL of the text file: ")
            word(https)
        
        elif choice == "0":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

        





               
          


