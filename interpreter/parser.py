import tokenizer, math, time, os
variables = {}
def parse(line):
	command = line[0]
	match command:
		case "printf":
			if variables.get(line[1]):
				print(variables.get(line[1]))
			else:
				print(line[1])
		case "scanf":
			variables[line[2]] = input(line[1])
		case "sys":
			os.system(line[1])
		case  "wait":
			time.sleep(int(line[1]))
		case "fib":
			phi = (1 + math.sqrt(5)) / 2
			print(int(round((phi**content[1] - (1 - phi)**content[1]) / math.sqrt(5))))
		case "sqrt":
			print(math.sqrt(content[1]))
		case "sine":
			print(math.sin(content[1]))
		case "init":
			name = content[2]
			value = content[3]
			variables[name] = value