import nltk
import re
from django.http import HttpResponse

out_progressive = []
out_perfect = []
out_past = []
out_regular_past = []
out_u_verb_group = []

# Aspect: find all instances of progressive aspect
def F_progressive_aspect(rist):
    # input sentence list and its 1 zigen
    # output list
    for rist1 in rist:
        for rist2 in rist1:
            if rist2[1] in ["VBG"]:
                out_progressive.append(rist2[0])
                # VBG Gerund, present participle (taking)
    return out_progressive


# Aspect: find all instances of perfect aspect
def F_perfect_aspect(rist):
    # input list
    # output list
    for rist1 in rist:
        for rist2 in rist1:
            if rist2[1] in ["VBP", "VBZ"]:
                out_perfect.append(rist2[0])
                # VBP Present tense (take)
                # VBZ Present 3rd person singular (takes)
    return out_perfect


# Tense: find all instances of past tense
def F_past_tense(rist):
    # input list
    # output list
    for rist1 in rist:
        for rist2 in rist1:
            if rist2[1] in ["VBD", "VBN"]:
                out_past.append(rist2[0])
                # VBD Past tense (took)
                # VBN Past participle (taken)
    return out_past


# Tense: find all instances of regular past tense
def F_regular_past_tense(rist):
    # input list
    # output list
    for rist1 in rist:
        for rist2 in rist1:
            if "VBD" in rist2:
                out_regular_past.append(rist2[0])
                # VBD Past tense (took)
    return out_regular_past


# Visualize: underline each verb group
def U_verb_group(rist):
    # input list
    # output list
    for rist1 in rist:
        for rist2 in rist1:
            if rist2[1] in ["VGC", "VBF", "VBP", "VBZ", "VBD", "VBN", "VB", "VBC"]:
                out_u_verb_group.append(rist2[0])
                # VB  Base verb (take)
                # VBC Future tense, conditional
                # VBD Past tense (took)
                # VBF Future tense
                # VBG Gerund, present participle (taking)
                # VBN Past participle (taken)
                # VBP Present tense (take)
                # VBZ Present 3rd person singular (takes)
    return out_u_verb_group


def display_instances(rist):
    # input list
    # output list
    out = []
    out = rist.sort()


def joinList(t2):
    sentence = ["", "", "", "", "", "", "", "", "", ""]
    sentence[0] = "Instances of progressive: \n" + " ".join(F_progressive_aspect(t2))
    sentence[1] = "Instances of perfect aspect: \n" + " ".join(F_perfect_aspect(t2))
    sentence[2] = "Instances of past tense: \n" + " ".join(F_past_tense(t2))
    sentence[3] = "Instances of regular past tense: \n" + " ".join(
        F_regular_past_tense(t2)
    )
    sentence[4] = "underline each verb group: " + " ".join(U_verb_group(t2))
    display_instances(out_progressive)
    display_instances(out_perfect)
    display_instances(out_past)
    display_instances(out_regular_past)
    display_instances(out_u_verb_group)
    sentence[5] = "Instances of progressive in alphabet: \n " + " ".join(
        out_progressive
    )
    sentence[6] = "Instances of perfect aspect in alphabet: \n" + " ".join(out_perfect)
    sentence[7] = "Instances of past tense in alphabet: \n" + " ".join(out_past)
    sentence[8] = "Instances of regular past tense in alphabet: \n" + " ".join(
        out_regular_past
    )
    sentence[9] = "underline each verb group in alphabet: \n" + " ".join(
        out_u_verb_group
    )

    return sentence

    """
    print("Instances of progressive :")
    print(F_progressive_aspect(t2))
    print("Instances of perfect aspect :")
    print(F_perfect_aspect(t2))
    print("Instances of past tense :")
    print(F_past_tense(t2))
    print("Instances of regular past tense :")
    print(F_regular_past_tense(t2))
    print("underline each verb group:")
    print(U_verb_group(t2))
    print("Instances of progressive in alphabet:")
    display_instances(out_progressive)
    print(out_progressive)
    print("Instances of perfect aspect in alphabet:")
    display_instances(out_perfect)
    print(out_perfect)
    print("Instances of past tense in alphabet:")
    display_instances(out_past)
    print(out_past)
    print("Instances of regular past tense in alphabet:")
    display_instances(out_regular_past)
    print(out_regular_past)
    print("underline each verb group in alphabet:")
    display_instances(out_u_verb_group)
    print(out_u_verb_group)
    """


def showtense(response):

    # print("Input your text :")
    t = "Two frogs, a father and his son, accidently fell into a bucket of milk. They started swimming for their lives. They swam for a long time, but there seemed no hope of their getting out. The father soon gave up and drowned. The son carried on swimming. During this time, the milk had begun to form a ball of butter. Using this island of butter as a platform, he managed to hop out of the bucket."

    # split with "."
    t1 = re.findall("[^.]+.?", response)

    t2 = []
    for t11 in t1:
        # split with word and attach tag
        t2.append(nltk.pos_tag(nltk.word_tokenize(t11)))

    idendified_tense = joinList(t2)

    return idendified_tense
