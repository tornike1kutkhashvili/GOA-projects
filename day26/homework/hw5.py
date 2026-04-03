# 5) დაწერე ფუნქცია რომელიც იღებს სიტყვების სიას და აბრუნებს ყველაზე გრძელ სიტყვას.

def longest_word(words):
    longest = words[0]
    for word in words:
        if len(word) > len(words):
            print(longest)

longest_word(['qqqqqqqqqq','qq','q'])