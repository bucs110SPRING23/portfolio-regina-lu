import json

def main():
    text = open("news.txt", "r").read()
    sub_fptr = open("subs,json")
                    
for k, v in subs.items():
    text = text.replace(k, v)