import json
book={
    'name':'Wings of fire',
    'pages':200,
    'author':'APJ Kalam',
}

# write opration
f=open('out.json','w')
s=json.dumps(book)
f.write(s)
f.close()

# read opration

f=open('out.json','r')
ld=json.load(f)
print(ld)