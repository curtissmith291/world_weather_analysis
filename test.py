import os

body_Str="Body of Dialog"

title_Str="Title"

os.system("""osascript -e \'Tell application \"System Events\" \\to display dialog \""+body_Str+"\" with title \""+title_Str+"\"\'""")
