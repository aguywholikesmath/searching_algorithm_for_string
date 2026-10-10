import time as t
charset = [chr(i) for i in range(0, 255)]
correctset = list("Lopado­temacho­selacho­galeo­kranio­leipsano­drim­hypo­trimmato­silphio­karabo­melito­katakechy­meno­kichl­epi­kossypho­phatto­perister­alektryon­opte­kephallio­kigklo­peleio­lagoio­siraio­baphe­tragano­pterygon")

def iteration(prefix,txt,set):
    for char in set:
        print(f"{prefix}{char}")
        if char == txt:
            break
        t.sleep(0.001)

def bruteforce(txt,set):
    txt_split = list(txt)
    for i in range(len(txt_split)):
        iteration("".join(txt_split[0:i]),txt_split[i],set)

bruteforce(correctset,charset)