
from flask import Flask, render_template, request, jsonify
from functions import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page.html')
	
	
@app.route('/valid1', methods=['POST'])
def valid1():
	try:
		txt = request.form.get('txt')
		PNumber = int(request.form.get('PnumA'))
		QNumber = int(request.form.get('Qnum'))
		N_number = comput_N(PNumber,QNumber)
		R_index = indexEuler(PNumber,QNumber)
		Set_prime = nbr_Premier_Euler(PNumber,QNumber)
		Result = {'R_index':R_index, 'N_number': N_number, 'Set_prim':Set_prime}
		return jsonify(Result)
	except Exception as e:
		Error = {'error': 'Erreur : ' + str(e)}
		return jsonify(Error)
	

@app.route('/valid2', methods=['POST'])
def valid2():
	try:
		Nbr_choisi = int(request.form.get('PrimNbr'))
		R_index = int(request.form.get('R_index'))
		private_Key2 = modinv(Nbr_choisi,R_index)
		Result = {'private_Key2':private_Key2}
		return jsonify(Result)
	except Exception as e:
		Error = {'error': 'Erreur : ' + str(e)}
		return jsonify(Error)
	

@app.route('/chiffrer', methods=['POST'])
def chifrer():
	try:
		txt = request.form.get('txt')
		Public_key1 = int(request.form.get('Public_key1'))
		Public_key2 = int(request.form.get('Public_key2'))
		msgcrypte = crypter(txt, Public_key1, Public_key2)
		Result = {'msgcrypte':msgcrypte}
		return jsonify(Result)
	except Exception as e:
		Error = {'error': 'Erreur : ' + str(e)}
		raise e
		return jsonify(Error)
	



	


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)