import hashlib
import requests 
import json

def decifra(mensagem, chave):
	decifrado = ""
	for letra in mensagem:
		numero = ord(letra)
		if letra.isalpha():
			numero = numero - chave
			if numero < ord('a'):
				numero += 26
		letraOriginal = chr(numero)
		if letra == " ":
			decifrado += " "
		else:
			decifrado += letraOriginal
	return decifrado



def main():

	url = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=7a0e2c3bc29e536a3f1f931085ca8dd0d3121165")

	response = json.loads(url.text)

	arquivo = open("answer.json", "w")
	json.dump(response, arquivo)
	arquivo.close()

	obj = None
	with open("answer.json", "r") as file:
		obj = json.load(file)


	obj["decifrado"] = decifra(obj["cifrado"], obj["numero_casas"])

	

	obj["resumo_criptografico"] = hashlib.sha1(obj["decifrado"].encode('utf-8')).hexdigest()


	with open("answer.json", "w") as file:
		json.dump(obj, file)

	url2 = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=7a0e2c3bc29e536a3f1f931085ca8dd0d3121165'

	

	multipart_form_data = {'answer': ('answer.json', open('answer.json', 'rb')) }

	r = requests.post(url2, files=multipart_form_data)

	print(r.text)

if __name__== "__main__":
  main()