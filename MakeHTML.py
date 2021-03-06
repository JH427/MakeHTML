#REQUIRES PYTHON 3.5
import random
import time
from tqdm import tqdm
time.sleep(1)

def photo_gallery():
    '''Makes HTML for the SERA-6 photo gallery'''
    ALBUM_NAME = input("Album Name>>>")
    URL = input("URL>>")
    NUM = input("Number of images>>")
    OUTPUT = input("Output Filename>>>")
    f = open(OUTPUT+'.txt', 'w')
    #print("GENERATING h3 .page-header")
    f.write("<h3 class=\"page-header\">"+ALBUM_NAME+"</h3>\n")
    #print("GENERATING div .row")
    f.write("<div class=\"row\">\n")
    for i in tqdm(range(1,int(NUM)+1)):
        #print("GENERATING div .col-md-3 "+ str(i))
        f.write("  <div class=\"col-md-3\">\n")
        f.write("    <a href=\"" + URL + "/" + str(i) + ".jpg\" class=\"thumbnail\">\n")
        f.write("      <img src=\""+ URL + "/" + "tn_" + str(i) + ".jpg\"></img>\n")
        f.write("    </a>\n")
        f.write("  </div>\n")

    #print("CLOSING div .row")
    f.write("</div>\n")
    print("\n")
    print("Thank you for using MakeHTML alpha, please collect your HTML at "+OUTPUT+".txt")
    time.sleep(5)

def make_table():
    '''Makes a table'''
    NUM_ROWS = int(input('Number of rows>>>'))
    NUM_COLS = int(input('Number of columns>>>'))
    OUTPUT = input("Output Filename>>>")
    f = open(OUTPUT+'.txt', 'w')
    #print("GENERATING table")
    f.write("<table class=\"table\">\n")
    for tr in tqdm(range(NUM_ROWS)):
        #print("GENERATING table row "+str(tr))
        f.write("  <tr>\n")
        for td in range(NUM_COLS):
            #print("GENERATING table column "+str(td))
            f.write("    <td></td>\n")
        #print("CLOSING row "+str(tr))
        f.write("  </tr>\n")
    #print("CLOSING table")
    f.write("</table>\n")
    print("DING! table done: "+OUTPUT+".txt")
    time.sleep(5)

def make_default_sera6_page_with_iframe():
    '''Makes a blank page with the nav bar and an iframe for sera6'''
    SRC = input("Source URL>>>")
    OUTPUT = input("Output Filename>>>")
    f = open(OUTPUT+'.asp', 'w')
    f.write("<!DOCTYPE HTML>")
    f.write("<!-- This page was generated by MakeHTML.py, a script that generates HTML specifically for this website -->")
    f.write("<!--#include file=\"INCLUDE/head.inc\"-->")
    f.write("<body>")
    f.write("<!--#include file=\"INCLUDE/nav.inc\"-->")

    #Hello.. is it me you're looking for?
    f.write("<div class=\"embed-responsive\">")
    f.write("   <iframe class=\"embed-responsive-item\" src=\""+SRC+"\"></iframe>")
    f.write("</div>")

    f.write("<!--#include file=\"INCLUDE/footer.inc\"-->")
    f.write("</body")



slogan = ["The AESL standard in niche HTML generation.",
          "The best tool for generating HTML for a very specific website!",
          "Generating HTML for the SERA-6 website since yesterday!",
          "Completely undocumented!",
          "How website photo galleries are made.",
          "I think, therefore HTML.",
          "HTML makes dreams come true.",
          "HTML when you're out of time.",
          "HTML as far as the eye can see.",
          "I see HTML in your future.",
          "HTML for you!",
          "HTML wins again.",
          "First, solve the problem. Then, write the code.",
          "Copy and paste is a design error.",
          "Don't worry if it doesn't work right.",
          "In theory, theory and practice are the same. In practice, they're not.",
          "Beware of bugs in the code.",
          "To iterate is human, to recurse divine.",
          "What we think, we become.",
          "Strategy without tactics is the slowest route to victory. Tactics without strategy is the noise before defeat.",
          "If the mind is willing, the flesh could go on and on without many things.",
          "\n\"Three hundred men, all of-whom know one another, direct the economic destiny of Europe and choose their successors from among themselves\" -Walter Rathenau",
          "\n\"The individual is handicapped by coming face to face with a conspiracy so monstrous he cannot believe it exists.\" - J. Edgar Hoover"]
print( '''
  __  __      _       _  _ _____ __  __ _
 |  \/  |__ _| |_____| || |_   _|  \/  | |
 | |\/| / _` | / / -_) __ | | | | |\/| | |__
 |_|  |_\__,_|_\_\___|_||_| |_| |_|  |_|____|

Welcome to MakeHTML alpha!''')
print(slogan[random.randint(0,(len(slogan)-1))]+'\n')

print("What are you trying to generate HTML for anyways?")
print("1) SERA-6-IEG Photo Gallery")
print("2) Make a table")
print("3) Make a page with an iframe with your choice of sprinkles")
print("\n")

# OK I know I should be using argparse and I WILL ADD IT EVENTUALLY

CHOICE = input(">>>")

if CHOICE == str(1):
    photo_gallery()
elif CHOICE == str(2):
    make_table()
elif CHOICE == str(3):
    make_default_sera6_page_with_iframe()
elif CHOICE != str(1) and CHOICE != str(2) and CHOICE != str(3):
    print("GOODBYE")
    time.sleep(10)
