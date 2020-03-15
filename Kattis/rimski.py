# 4,14,24,34,44,54,64,74,84,94
# 9,19,29,39,59,69,79,89
# 40,90

c = {
	"VI": "IV",
	"XVI": "XIV",
	"XXVI": "XXIV",
	"XXXVI": "XXXIV",
	"XLVI": "XLIV",
	"LVI": "LIV",
	"LXVI": "XLIV",
	"LXXVI": "LXXIV",
	"LXXXVI": "LXXXIV",
	"XCVI": "XCIV",

	"XI": "IX",
	"XXI": "XIX",
	"XXXI": "XXIX",
	"LXI": "XLI",
	"LXXI": "LXIX",
	"LXXXI": "LXXIX",

	"LX": "XL",
	"LXII": "XLII",
	"LXIII": "XLIII",
	"LXIV": "XLIV",
	"LXV": "XLV",
	"LXVII": "XLVII",
	"LXVIII": "XLVIII"
}
b = input()
print(b if b not in c else c[b])
