y, p = raw_input().split()
l = y[-1:]
if y[-1:] == "e": print y + "x" + p
elif y[-1:] in ["a","i","o","u"]: print y[:-1] + "ex" + p
elif y[-2:] == "ex": print y + p
else: print y + "ex" + p
