text = input()
start_index = text.index("a") if "a" in text else 0
end_index = text.index("z")+1 if "z" in text else len(text)
print(text[start_index:end_index])