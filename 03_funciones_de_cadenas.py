
def modifica_cadena(param):
	# Todas mayusculas
	print('Texto original:\r{}'.format(param))
	text = param.upper()
	print(text)
	# Todas minusculas
	text = param.lower()
	print(text)
	# Titulo
	text = param.title()
	print(text)
	# Slice positivo
	text = param[2:]
	print(text)
	# Slice negativo
	text = param[-2:]
	print(text)
	# Ejemplo invirtiendo el orden del texto
	text = param[::-1]
	print(text)

	

if __name__ == '__main__':
	modifica_cadena('Este es un texto de prueba') 