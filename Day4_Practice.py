print("python")

# To add a tab in the string we can use forwardslash and t
print("\tpython")

#
print('//python')


# To add a new line into the sting we can use forwardslash and n

print("Languages:\nPython\nC\nJavascript")


# We can also combine tabs and newlines in a single string. The string "\n\t" tells python to move to a new line,land start the next line with a tab.

print("Languages:\n\tpython\n\tC\n\tJavascript")


# Stripping whitespace

favorite_language = 'python '

# rstrip() method removes any whitespace at the end of the string
favorite_language.rstrip()
print(favorite_language)


favorite_language = ' python '
# strip() method removes whitespace at the beginning and end of the string
favorite_language.strip()


print(favorite_language)

# Here we have a url and we want to remove the http:// from the beginning of the url.
#  We can use the removeprefix() method to remove a prefix from a string.
nostarch_url = 'http://nostarch.com'
nostarch_url = nostarch_url.removeprefix('http://')
print(nostarch_url)
