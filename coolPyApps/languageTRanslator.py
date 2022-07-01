from googletrans import Translator
translater = Translator()
out = translater.translate("Do you like football? I know Belarusian teams that have played in champions league)",dest="be")
print(out.text)