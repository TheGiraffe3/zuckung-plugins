
def set_globals():
	global names
	global fields
	global locations
	global races
	global sexes
	global images
	global money
	global stat1
	global stat2
	global prefield
	global postfield
	global fsource
	global listfile
	global foutfits
	global fmissions
	global percent
	global saveedit1
	global saveedit2
	global saveedit3
	fsource = 'experts.txt' # input
	listfile = 'crew.list.txt' # overview
	foutfits = 'outfits.txt' # output
	fmissions = 'missions.txt' # output
	percent = 3 # mission chance
	names, fields, locations, races, sexes, images, money, stat1, stat2, saveedit1, saveedit2, saveedit3 = [], [], [], [], [], [], [], [], [], [], [], []


def find_symbol(string, start, symbol):
	quote1 = string.find(symbol, start)
	quote2 = string.find(symbol, quote1 + 1)
	output = string[quote1 + 1:quote2]
	return output, quote2


def read_experts():
	with open(fsource) as source_file:
		with open(listfile, 'w') as list_file:
			lines = source_file.readlines()
			for line in lines:
				list_file.writelines(line)
				if line.startswith('\n'):
					continue
				elif line.startswith('amount'):
					continue
				elif line.startswith('\t'):
					continue
				elif line.startswith('"'):
					# create lists
					x, pos = find_symbol(line,0, '"')
					pos2 = x.find(' ', 0)
					fields.append(x[0:pos2])
					names.append(x[pos2+1:])
					x, pos = find_symbol(line,pos + 1, '"')
					locations.append(x)
					x, pos = find_symbol(line,pos + 1, '"')
					money.append(x)
					x, pos = find_symbol(line,pos + 1, '"')
					sexes.append(x)
					x, pos = find_symbol(line,pos + 1, '"')
					images.append(x)
					if x.startswith('human'):
						races.append('human')
					elif x.startswith('arachi'): 
						races.append('arach')
					else:
						races.append(x[:len(x)-2])
					x, pos = find_symbol(line,pos + 1, '"')
					xlist = x.split(' ')
					xlen = len(xlist)
					x = '"'
					for i in range(0, xlen):
						if i == xlen -1:
							x += '" '
						x += xlist[i]
						if i != xlen-2:
							x += ' '
					stat1.append(x)
					x, pos = find_symbol(line,pos + 1, '"')
					xlist = x.split(' ')
					xlen = len(xlist)
					x = '"'
					for i in range(0, xlen):
						if i == xlen -1:
							x += '" '
						x += xlist[i]
						if i != xlen-2:
							x += ' '
					stat2.append(x)

			
def write_files():
	with open(listfile, 'a') as list_file:
		with open(foutfits, 'w') as outfits_file:
			with open(fmissions, 'w') as missions_file:
				# writing the category block
				outfits_file.writelines('category "outfit"\n')
				outfits_file.writelines('\t"Crew"\n')
				outfits_file.writelines('\n')
				# start loop
				for name in names:
					source2 = ''
					index = names.index(name)
					# capitalizing both names
					name1 = names[index].split(' ') [0].capitalize()
					if len(names[index].split(' ')) == 2:
						name2 = names[index].split(' ')[1].capitalize()
					else:
						name2 = ''
					if name2 == '':
						fullname = name1
					else:
						fullname = name1 + ' ' + name2
					# setting pronouns
					if sexes[index] == 'm':
						pronoun = 'he'
						pronoun2 = 'him'
						pronoun3 = 'his'
					else:
						pronoun = 'she'
						pronoun2 = 'her'
						pronoun3 =  'her'
					# setting articles
					if races[index] == 'arach':
						article = 'an'
					else:
						article = 'a'
					# setting fields
					if fields[index] == 'combat':
						prefield = 'hand to hand '
						postfield = ''
					elif fields[index] == 'cooling':
						prefield = ''
						postfield = ' technologies'
					elif fields[index] == 'energy':
						prefield = ''
						postfield = ' technologies'
					elif fields[index] == 'engine':
						prefield = ''
						postfield = ' technologies'
					elif fields[index] == 'fuel':
						prefield = ''
						postfield = ' technologies'
					elif fields[index] == 'hull':
						prefield = ''
						postfield = ' effektivity'
					elif fields[index] == 'jamming':
						prefield = ''
						postfield = ' technologies'
					elif fields[index] == 'scanner':
						prefield = ''
						postfield = ' technologies'
					elif fields[index] =='shield':
						prefield = ''
						postfield = ' effektivity'
					elif fields[index] =='storage':
						prefield = ''
						postfield = ' management'
					# setting location
					if races[index] == 'human':
						locphrase = ', grown up in "' + locations[index] + '"'
					else:
						locphrase = ''
					# setting source	
					if races[index] == 'human':
						source = '\t\tgovernment "Republic" "Free Worlds" "Syndicate" "Neutral" "Pirate"\n'
						source2 = '\t\tattributes "' + locations[index] + '"\n'
						tooffer = ''
					elif races[index] == 'hai':
						source = '\t\tgovernment "Hai"\n'
						source2 = ''
						tooffer = ''
					elif races[index] == 'remnant':
						source = '\t\tgovernment "Remnant"\n'
						source2 = ''
						tooffer = ''
					elif races[index] == 'korath':
						source = '\t\tgovernment "Kor Efret"\n'
						source2 = ''
						tooffer = '\t\thas "Wanderers: Rek To Kor Efret: done"\n'
					elif races[index] == 'bunrodea':
						source = '\t\tgovernment "Bunrodea" "Bunrodea (Guard)"\n'
						source2 = ''
						tooffer = ''
					elif races[index] == 'wanderer':
						source = '\t\tgovernment "Wanderer"\n'
						source2 = ''
						tooffer = '\t\thas "language: Wanderer"\n'
					elif races[index] == 'arach':
						source = '\t\tgovernment "Coalition"\n'
						source2 = '\t\tattributes "' + races[index] + '"\n'
						tooffer = '\t\thas "Coalition: First Contact: done"\n'
					elif races[index] == 'kimek':
						source = '\t\tgovernment "Coalition"\n'
						source2 = '\t\tattributes "' + races[index] + '"\n'
						tooffer = '\t\thas "Coalition: First Contact: done"\n'
					elif races[index] == 'saryd':
						source = '\t\tgovernment "Coalition"\n'
						source2 = '\t\tattributes "' + races[index] + '"\n'
						tooffer = '\t\thas "Coalition: First Contact: done"\n'
				
					# writing the outfit
					outfits_file.writelines('outfit "' + fields[index] + ' '  + names[index] + '"\n')
					saveedit3.append('\t\t"' + fields[index] + ' '  + names[index] + '"\n')
					if names[index][len(names[index])-1:] == 's':
						outfits_file.writelines('\tplural "(' + fields[index].capitalize() + ') ' + fullname + '"\n')
					outfits_file.writelines('\tcategory "Crew"\n')
					outfits_file.writelines('\t"display name" "(' + fields[index].capitalize() + ') ' + fullname + '"\n')
					outfits_file.writelines('\tthumbnail "portrait/' + images[index] + '"\n')
					outfits_file.writelines('\t"operating costs" ' + money[index] + '\n')
					outfits_file.writelines('\tbunks -1\n')
					outfits_file.writelines('\t"unplunderable" 1\n')
					outfits_file.writelines('\t"unique" 1\n')
					outfits_file.writelines('\t' + stat1[index] + '\n')
					outfits_file.writelines('\t' + stat2[index] + '\n')
					outfits_file.writelines('\tdescription `This is a highly educated employee focused on '+ prefield + fields[index] + postfield + '. ' + pronoun.capitalize() + ' is ' + article + ' ' + races[index].capitalize() + locphrase + '.`\n')
					outfits_file.writelines('\n')	
					# writing the mission
					missions_file.writelines('mission "hire ' + fields[index] + ' ' + names[index] + '"\n')
					saveedit1.append('\t"hire ' + fields[index] + ' ' + names[index] + ': declined"\n')
					saveedit2.append('\t"hire ' + fields[index] + ' ' + names[index] + ': offered"\n')
					missions_file.writelines('\tminor\n')
					missions_file.writelines('\tinvisible\n')
					missions_file.writelines('\tsource\n')
					missions_file.writelines(source)
					if source2 != '':
						missions_file.writelines(source2)
					missions_file.writelines('\t\tattributes "outfitter"\n')
					missions_file.writelines('\tto offer\n')
					if tooffer != '':
						missions_file.writelines(tooffer)
					missions_file.writelines('\t\trandom < ' + str(percent) + '\n')
					missions_file.writelines('\ton offer\n')
					missions_file.writelines('\t\toutfit "' + fields[index] + ' ' + names[index] + '" 1\n')
					missions_file.writelines('\t\tconversation\n')
					missions_file.writelines('\t\t\tscene "portrait/' + images[index] + '"\n')
					missions_file.writelines('\t\t\t`In a spaceport bar you get to know a highly qualified expert in ' + prefield + fields[index] + postfield + '. ' + pronoun.capitalize() + ' is looking for work and you decide to hire ' + pronoun2 + '. ' + pronoun3.capitalize() + ' name is ' + fullname + ', ' + pronoun + ' is ' + article + ' ' + races[index].capitalize() + ', and ' + pronoun + ' demands a daily wage of ' + money[index] + ' credits.`\n')
					missions_file.writelines('\t\t\t\tdecline\n')
					missions_file.writelines('\n')

		list_file.writelines('savegame editing:\n')
		list_file.writelines('\n')
		list_file.writelines('outfits:\n')
		list_file.writelines('\n')
		for each in saveedit3:
			list_file.writelines(each)
		list_file.writelines('\n')
		list_file.writelines('missions:\n')
		list_file.writelines('\n')
		for each in saveedit1:
			index = saveedit1.index(each)
			list_file.writelines(each)
			list_file.writelines(saveedit2[index])


# run
set_globals()
read_experts()
write_files()