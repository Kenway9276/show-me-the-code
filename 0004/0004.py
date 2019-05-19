import re

f = open('0004.txt', 'r')
txt = f.read()


line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
reObj = re.compile("\b?([a-zA-Z]+)\b?", re.I)
words = reObj.findall(txt)

count_words = {}
for word in words:
    word.lower()
    if word in count_words:
        count_words[word] += 1
    else:
        count_words[word] = 1
print(count_words)
