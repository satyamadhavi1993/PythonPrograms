import array

text = "Hi I'm Satya Madhavi"
reverse_letters = text[::-1]
print(f'Text with letters reversed: {reverse_letters}')

reverse_words = " ".join(text.split( )[::-1])
print(f'Text with words reversed: {reverse_words}')
