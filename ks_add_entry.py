# EXAMPLE:
# add_entry("head, pos, ipa, g, dv, [.. defs ..])

# 0. Start tag
# Added by the build_word definition

# 1. Language
templ_lang = "===Kashmiri===\n"

# 2. IPA
def templ_ipa(ipa):
		if ipa:
			return "\n===Pronunciation===\n* {{IPA|/" + ipa + "/|lang=ks}}\n"
		else:
			return ""

# 3. Body
def templ_body(head, pos, g, dv, defs):
	body = "\n===" + pos.title() + "===\n"
	body += "{ks-" + pos
	gender = "|g=" + g if g else ""
	deva = "|dv=" + dv if dv else ""
	body += gender + deva + "}}\n"
	for dfn in defs:
		body += "# " + dfn + "\n"
	return body + "\n"

# 4. Create the format/entry
def build_word(head, pos, ipa, g, dv, defs):
	entry = "\n{{-start-}}\n'''" + head + "'''\n" + templ_lang + templ_ipa(ipa) + templ_body(head, pos, g, dv, defs) + "{{-stop-}}\n"
	return entry

# 5. Stop tag added by the build_word definition

# 6. Add to the file
def new_entry(entry):
	f = open("dict.txt", "a+")
	f.write(entry+"\n")
	f.close()

def add_entry(head, pos, ipa, g, dv, defs):
	new_entry(build_word(head, pos, ipa, g, dv, defs))