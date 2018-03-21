import pyautogui
from PIL import Image, ImageEnhance
import os
import time
import pytesseract
import crayons
import wikipedia
import nltk

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

filePath = '/Users/Abhay/Desktop/TriviaGameBot/screenshot.png'

screenshot = pyautogui.screenshot(filePath)

def processImage(img):
    
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(1)

    sharper = ImageEnhance.Sharpness(img)
    img = sharper.enhance(5)    

    brighter = ImageEnhance.Brightness(img)
    img = brighter.enhance(1)

    img = img.convert("L")

    img = img.crop((685,174,1150,658))

    #img.show()

    return img


stop = set(nltk.corpus.stopwords.words("english"))

while True:
    
    croppedScreen = processImage(Image.open(filePath))
    croppedScreen.save('/Users/Abhay/Desktop/TriviaGameBot/croppedScreen.png')

    txt = pytesseract.image_to_string(croppedScreen, lang='eng')

    parts = txt.split("\n\n")

    question = parts.pop(0).replace("\n", " ")
    q_terms = question.split(" ")
    q_terms = list(filter(lambda t: t not in stop, q_terms))
    q_terms = set(q_terms)

    parts = "\n".join(parts)
    parts = parts.split("\n")

    answers = list(filter(lambda p: len(p) > 0, parts))

    # question = "In Mexico, a saladito is always known as what?"
    # answers = ["Taco salad", "Salted plum", "Guava roll"]

    for i, a in enumerate(answers):
        answers[i] = a.replace("ﬁ", "ti")

    print("\n\n{}\n\n{}\n\n".format(
        crayons.blue(question),
        crayons.blue(", ".join(answers))
    ))

    answer_results = {}

    for answer in answers:
        records = wikipedia.search(answer)
        r = records[0] if len(records) else None

        if r is not None:
            p = wikipedia.page(r)
            answer_results[answer] = {
                "content": p.content,
                "words": p.content.split(" ")
            }

    for a in answer_results:
        term_count = 0

        for t in q_terms:
            term_count += answer_results[a]["words"].count(t)

        tc = term_count / len(answer_results[a]["words"])
        tcp = round(tc * 10000, 2)

        answer_results[a]["score"] = tcp

    max_a = 0
    max_a_key = None

    # Maximize
    for a in answer_results:
        if answer_results[a]["score"] > max_a:
            max_a_key = a
            max_a = max(answer_results[a]["score"], max_a)

    print(crayons.green(max_a_key))

   

time.sleep(0.1)
os.system("clear")

    
    

