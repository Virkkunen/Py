from rich import print
from rich.markdown import Markdown


def tarot(x):
    if x == 0:
        print(Markdown("\n# 0: The Fool\n\n- innocence\n- new beginnings\n- free spirit\n- spontaneity\n---"))
    elif x == 1:
        print(Markdown("\n# I: The Magician\n\n- willpower\n- resourcefulness\n- creation\n- manifestation\n---"))
    elif x == 2:
        print(Markdown("\n# II: The High Priestess\n\n- intuition\n- sacred knowledge\n- divine feminine\n- subconscious mind\n---"))
    elif x == 3:
        print(Markdown("\n# III: The Empress\n\n- femininity\n- beauty\n- nature\n- nurturin\n- abundance\n---"))
    elif x == 4:
        print(Markdown("\n# IV: The Emperor\n\n- authority\n- estabilishment\n- structure\n---"))
    elif x == 5:
        print(Markdown("\n# V: The Hierophant\n\n- spiritual wisom\n- religious beliefs\n- conformity\n- tradition\n---"))
    elif x == 6:
        print(Markdown("\n# VI: Lovers\n\n- love\n- harmony\n- relationships\n- values alignment\n- choices\n---"))
    elif x == 7:
        print(Markdown("\n# VII: The Chariot\n\n- control\n- willpower\n- success\n- action\n- determination\n---"))
    elif x == 8:
        print(Markdown("\n# VIII: Strength\n\n- strength\n- courage\n- persuasion\n- influence\n- compassion\n---"))
    elif x == 9:
        print(Markdown("\n# IX: Hermit\n\n- soul-searching\n- introspection\n- being alone\n- inner guidance\n---"))
    elif x == 10:
        print(Markdown("\n# X: Wheel of Fortune\n\n- good luck\n- karma\n- life cycles\n- destiny\n- a turning point\n---"))
    elif x == 11:
        print(Markdown("\n# XI: Justice\n\n- justice\n- fairness\n- truth\n- cause and effect\n- law\n---"))
    elif x == 12:
        print(Markdown("\n# XII: The Hanged Man\n\n- pause\n- surrender\n- letting go\n- new perspectives\n---"))
    elif x == 13:
        print(Markdown("\n# XIII: Death\n\n- endings\n- change\n- transformation\n- transition\n---"))
    elif x == 14:
        print(Markdown("\n# XIV: Temperance\n\n- balance\n- moderation\n- patience\n- purpose\n---"))
    elif x == 15:
        print(Markdown("\n# XV: Devil\n\n- shadow self\n- attachment\n- addiction\n- restriction\n---"))
    elif x == 16:
        print(Markdown("\n# XVI: Tower\n\n- sudden change\n- upheaval\n- chaos\n- revelation\n- awakening\n---"))
    elif x == 17:
        print(Markdown("\n# XVII: Star\n\n- hope\n- faith\n- purpose\n- renewal\n- spirituality\n---"))
    elif x == 18:
        print(Markdown("\n# XVIII: The Moon\n\n- illusion\n- fear\n- anxiety\n- subconscious\n- intuition\n---"))
    elif x == 19:
        print(Markdown("\n# XIX: The Sun\n\n- positivity\n- fun\n- warmth\n- success\n- vitality\n---"))
    elif x == 20:
        print(Markdown("\n# XX: Judgement\n\n- judgement\n- rebirth\n- inner calling\n- absolution\n---"))
    elif x == 21:
        print(Markdown("\n# XXI: The World\n\n- completion\n- integration\n- accomplishment\n- travel\n---"))
    else:
        print("Not found.")

while True:
    x = int(input("\n\nCard #: "))
    if x >= 0 and x <= 21: tarot(x)
    else: break
