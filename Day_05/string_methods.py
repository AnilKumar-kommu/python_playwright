# string methods in python

s=" Hello, World! "
print(s.upper())          # ' HELLO, WORLD! '
print(s.lower())          # ' hello, world! '
print(s.strip())         # 'Hello, World!'
print(s.replace("World", "Python"))  # ' Hello, Python! '
print(s.split(","))      # [' Hello', ' World! ']
print(s.startswith(" Hello"))  # True
print(s.endswith("! "))      # True
print(s.find("World"))      # 8
print(s.count("o"))        # 2
print(s.capitalize())      # ' hello, world! '
print(s.title())          # ' Hello, World! '
print(s.swapcase())       # ' hELLO, wORLD! '
# Real-time example
user_input = "   Data Science with Python   "
cleaned_input = user_input.strip().title()
print(f"Cleaned Input: '{cleaned_input}'")  # 'Data Science With Python'
keywords = cleaned_input.split()
print(f"Keywords: {keywords}")  # ['Data', 'Science', 'With', 'Python']  # Output: Cleaned Input: 'Data Science With Python'

#find and rfind
text = "abracadabra"
print(text.find("b"))   # 0
print(text.rfind("b"))  # 7

# zfill - info padding with zeros
num_str = "42"
print(num_str.zfill(5))  # '00042'

# partition and rpartition
sentence = "I love Python programming"
print(sentence.partition("Python"))  # ('I love ', 'Python', ' programming')
print(sentence.rpartition("love"))   # ('I ', 'love', ' Python programming')

# encode and decode
original_str = "Hello, World!"
encoded_str = original_str.encode("utf-8")
print(encoded_str)  # b'Hello, World!'
decoded_str = encoded_str.decode("utf-8")
print(decoded_str)  # 'Hello, World!'

# format method
name = "Alice"
age = 30
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print(formatted_str)  # 'My name is Alice and I am 30 years old.'

# f-strings
formatted_str_f = f"My name is {name} and I am {age} years old"
print(formatted_str_f)  # 'My name is Alice and I am 30 years old.'

# Real-time example: URL manipulation
url = "   https://www.example.com/path/to/page   "
cleaned_url = url.strip().lower()
print(f"Cleaned URL: '{cleaned_url}'")  # 'https://www.example.com/path/to/page'
domain = cleaned_url.split("/")[2]
print(f"Domain: {domain}")  # 'www.example.com'
path = "/".join(cleaned_url.split("/")[3:])
print(f"Path: /{path}")  # '/path/to/page'

#real time example: Log parsing
log_entry = "  ERROR 2024-06-01 12:00:00 - User 'bob' failed to login  "
cleaned_log = log_entry.strip()
log_level, timestamp, message = cleaned_log.split(" - ", 2)
print(f"Log Level: {log_level}")      # 'ERROR 2024-06-01 12:00:00'
print(f"Timestamp: {timestamp}")      # 'User 'bob' failed to login'
print(f"Message: {message}")          # 'User 'bob' failed to login'

# Real-time example: Email validation
email = "anil@gmail.com"
cleaned_email = email.strip().lower()
if "@" in cleaned_email and cleaned_email.endswith(".com"):
    print(f"Valid email: {cleaned_email}")  # 'Valid email:
else:
    print(f"Invalid email: {cleaned_email} {cleaned_email}")
    print(f"Invalid email: {cleaned_email}")  # 'Invalid email:

# Real-time example: File name manipulation
file_name = "   Report_2024_Final.DOCX   "
cleaned_file_name = file_name.strip().lower()
base_name, extension = cleaned_file_name.rsplit(".", 1)
print(f"Base Name: {base_name}")      # 'report_2024_final'
print(f"Extension: {extension}")      # 'docx'
# Renaming file
new_file_name = f"{base_name}_v2.{extension}"
print(f"New File Name: {new_file_name}")  # 'report_2024_final_v2.docx'
print(f"Valid email: {cleaned_email}")  # 'Valid email:

# Real-time example: current automation script
file_path = "   /User/Documents/Project/Report.pdf   "
cleaned_path = file_path.strip()
directories = cleaned_path.split("/")
file_name = directories[-1]
print(f"File Name: {file_name}")  # 'Report.pdf'
file_base, file_ext = file_name.rsplit(".", 1)
print(f"File Base: {file_base}")  # 'Report'
print(f"File Extension: {file_ext}")  # 'pdf'
new_file_name = f"{file_base}_final.{file_ext}"
new_file_path = "/".join(directories[:-1] + [new_file_name])
print(f"New File Path: {new_file_path}")  # '/User/Documents/Project/Report_final.pdf'

# Real-time example: Data cleaning in CSV
csv_row = "  John Doe , 28 , New York , john.doe@EX AMPLE.com  "
cleaned_row = csv_row.strip()
fields = [field.strip().title() for field in cleaned_row.split(",")]
print(f"Cleaned Fields: {fields}")  # ['John Doe', '28', 'New York', 'John.Doe@Ex Ample.Com']
name, age, city, email = fields
print(f"Name: {name}")      # 'John Doe'
print(f"Age: {age}")        # '28'
print(f"City: {city}")      # 'New York'
print(f"Email: {email}")    # 'John.Doe@Ex Ample.Com'
standardized_email = email.replace(" ", "").lower()
print(f"Standardized Email: {standardized_email}")  # 'john.doe@example.com'

# Real-time example: Social media post processing
post = "   Loving the new features in Python 3.10! #Python #Programming   "
cleaned_post = post.strip()
print(f"Cleaned Post: '{cleaned_post}'")  # 'Loving the new features in Python 3.10! #Python #Programming'
hashtags = [word for word in cleaned_post.split() if word.startswith("#")]
print(f"Hashtags: {hashtags}")  # ['#Python', '#Programming']
content = " ".join([word for word in cleaned_post.split() if not word.startswith("#")])
print(f"Content: '{content}'")  # 'Loving the new features in Python 3.10!'

# Censoring inappropriate words
inappropriate_words = ["badword1", "badword2"]
post_with_censorship = cleaned_post
for word in inappropriate_words:
    post_with_censorship = post_with_censorship.replace(word, "*" * len(word))
print(f"Censored Post: '{post_with_censorship}'")  # Censored post

# Real-time example: Generating usernames
full_name = "   Emily Blunt   "
cleaned_name = full_name.strip().lower()
first_name, last_name = cleaned_name.split()
username = f"{first_name}.{last_name}"
print(f"Generated Username: {username}")  # 'emily.blunt'

# Real-time example: Formatting product codes
product_code = "  abC123xyZ  "
cleaned_code = product_code.strip().upper()
formatted_code = f"PROD-{cleaned_code}"
print(f"Formatted Product Code: {formatted_code}")  # 'PROD-ABC123XYZ'

# Real-time example: Chat message processing
chat_message = "   Hey there!!! How's it going???   "
cleaned_message = chat_message.strip()
print(f"Cleaned Message: '{cleaned_message}'")  # 'Hey there!!! How's it going???'
standardized_message = cleaned_message.replace("!!!", "!").replace("???", "?")
print(f"Standardized Message: '{standardized_message}'")  # 'Hey there! How's it going?'
words = standardized_message.split()
print(f"Words in Message: {words}")  # ['Hey', 'there!', "How's', 'it', 'going?']

# Real-time example: most common uses in python string methods
product_description = "   This is an amazing product! Buy now!!!   "
cleaned_description = product_description.strip().capitalize()
print(f"Cleaned Description: '{cleaned_description}'")  # 'This is an amazing product! buy now!!!'
highlighted_description = cleaned_description.replace("amazing", "incredible")
print(f"Highlighted Description: '{highlighted_description}'")  # 'This is an incredible product! buy now!!!'
words_in_description = highlighted_description.split()
print(f"Words in Description: {words_in_description}")  # ['This', 'is', 'an', 'incredible', 'product!', 'buy', 'now!!!']

# Real-time example: Formatting addresses
address = "   123 main st., springfield, il 62704   "
cleaned_address = address.strip().title()
print(f"Cleaned Address: '{cleaned_address}'")  # '123 Main St., Springfield, Il 62704'
street, city_state_zip = cleaned_address.split(",", 1)
city, state_zip = city_state_zip.strip().rsplit(" ", 1)
state, zip_code = state_zip.split(" ", 1)
print(f"Street: {street}")        # '123 Main St.'
print(f"City: {city}")          # 'Springfield'
print(f"State: {state}")        # 'Il'
print(f"Zip Code: {zip_code}")    # '62704'
standardized_address = f"{street}, {city}, {state.upper()} {zip_code}"
print(f"Standardized Address: '{standardized_address}'")  # '123 Main St., Springfield, IL 62704'

# Real-time example: Formatting phone numbers
phone_number = "   (123) 456-7890   "
cleaned_number = phone_number.strip()
digits_only = "".join(filter(str.isdigit, cleaned_number))
formatted_number = f"+1-{digits_only[:3]}-{digits_only[3:6]}-{digits_only[6:]}"
print(f"Formatted Phone Number: {formatted_number}")  # '+1-123-456-7890'

# Real-time example: Processing survey responses
survey_response = "   Yes, I love programming in Python!   "
cleaned_response = survey_response.strip().capitalize()
print(f"Cleaned Response: '{cleaned_response}'")  # 'Yes, i love programming in python!'
keywords = cleaned_response.split()
print(f"Keywords: {keywords}")  # ['Yes,', 'i', 'love', 'programming', 'in', 'python!']
positive_words = ["love", "like", "enjoy"]
is_positive = any(word.lower().strip(".,!") in positive_words for word in keywords)
print(f"Is Positive Response: {is_positive}")  # True

# Real-time example: in travel booking system
destination = "   paris, france   "
cleaned_destination = destination.strip().title()
print(f"Cleaned Destination: '{cleaned_destination}'")  # 'Paris, France'
city, country = cleaned_destination.split(",", 1)
standardized_destination = f"{city.strip()}, {country.strip().upper()}"
print(f"Standardized Destination: '{standardized_destination}'")  # 'Paris, FRANCE'

# Real-time example: isdigit and isnumeric
input_str = "  12345  "
cleaned_input = input_str.strip()
if cleaned_input.isdigit():
    print(f"Input is a valid integer: {cleaned_input}")  # 'Input is a valid integer: 12345'
else:
    print(f"Input is not a valid integer: {cleaned_input}")  # 'Input is not a valid integer: 12345'

# Real-time example: isnumaeric
numeric_str = "  Ⅻ  "  # Roman numeral for 12
cleaned_numeric = numeric_str.strip()
if cleaned_numeric.isnumeric():
    print(f"Input is a valid numeric: {cleaned_numeric}")  # 'Input is a valid numeric: Ⅻ'
else:
    print(f"Input is not a valid numeric: {cleaned_numeric}")  # 'Input is not a valid numeric: Ⅻ'

# Real-time example: text normalization for NLP





