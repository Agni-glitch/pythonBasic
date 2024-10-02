import re
# pattern="This was a milestone in"
# pattern="[A-z]+sia"
pattern="(mil)...()one"
text='''His initial voyage to India by way of Cape of Good Hope[4] (1497–1499) was the first to link Europe and Asia by an ocean route, connecting the Atlantic and the Indian oceans. This was a milestone in Portuguese maritime exploration as and marked the beginning of a sea-based phase of globalization.[5] Da Gama's discovery of the sea route to India opened the way for an age of global imperialism and enabled the Portuguese to establish a long-lasting colonial empire along the way from Africa to cssia.'''

# match=re.search(pattern,text)
# print(match.span()) #(175, 198)
# if match:
#     print("Match found")
# else:
    # print("no match")

matches=re.finditer(pattern,text)
for match in matches:
    print(match.span(),type(match.span()))
    print(text[match.span()[0]:match.span()[1]])