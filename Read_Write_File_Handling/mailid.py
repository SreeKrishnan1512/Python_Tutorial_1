sentence = "Please email us at mentor@rahulshettyacademy.com with your queries."

words=sentence.split()

print(words)
email=" "

for i in words:

    if "@" in i:
        email=i.strip(".,")
        break

print(email)

    