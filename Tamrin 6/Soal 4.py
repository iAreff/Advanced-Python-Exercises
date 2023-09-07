import re

text = """
Today, Richard Rael and Tony Riggs tell the story of American astronomer edwin hubble. 
He changed our ideas about the universe and how it developed.
Edwin hubble made his most important discoveries in the nineteen twenties. Today, other 
astronomers continue the work he began. Many of them are using the Hubble space 
telescope that is named after him.
Edwin Hubble was born in eighteen eighty-nine in Marshfield, Missouri. He spent his early 
years in the state of Kentucky. Then he moved with his family to Chicago, Illinois. He 
attended the University of Chicago. He studied mathematics and astronomy.
"""

splited_text = text.split('.')
new_text = []
for i in splited_text:
    i = i.replace('\n',' ').replace('  ',' ').strip()
    if 'edwin hubble' in i.lower():
        new_text.append(i.replace('edwin hubble','Edwin Hubble'))
    else:
        new_text.append(i)
print('.'.join(new_text).replace('.','. '))



# a = re.split(r"[\n.]",text)
# for i in a:
#     print(i)
#     print('------')