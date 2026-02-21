import tokenizer, math, time, os, stdlib
variables = {
	"__euler__": 2.71828,
	"__pi__": 3.14159,
	"__file__": __file__,
	"null": "None",
	"__version__": 0.5
}
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
			print(int(round((phi**line[1] - (1 - phi)**line[1]) / math.sqrt(5))))
		case "sqrt":
			print(math.sqrt(line[1]))
		case "sine":
			print(math.sin(line[1]))
		case "init":
			name = line[2]
			value = line[3]
			variables[name] = value
		case "stdlib":
			function = line[1]
			function = function.strip()
			value = line[2]
			print(exec(f"stdlib.{function}({value})"))