from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)
a = [
    'buber',
    'yj@836LqBEQHosnr',
	'buber701',
]

@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "POST":
		i = request.form.get('search').lower()
		if i == "javascript":
			return redirect(url_for('js'))
		if i == "python":
			return redirect(url_for("python"))
		if i == "java":
			return redirect(url_for("java"))
		if i == "scratch":
			return redirect(url_for("scratch"))
		else:
			return redirect(url_for("err", e="400"))
	return render_template('index.html')


@app.route('/err/<e>/')
def err(e):
	return render_template('error.html', e=e)

@app.route('/js/')
def js():
	return render_template('js.html')

@app.route('/python/')
def python():
	return render_template('python.html')

@app.route('/cs/')
def cs():
	return render_template('csharp.html')

@app.route('/java/')
def java():
	return render_template('java.html')

@app.route('/scratch/')
def scratch():
	return render_template('scratch.html')

@app.route("/code/", methods=["GET", "POST"])
def code():
	if request.method == "POST":
		name = request.form.get("name").lower()
		pas = request.form.get("pas").lower()
		if name == "buber" and pas == "buber701":
			return redirect(
			    url_for('code_link',
			            n=name,
			            u='3867&c3aCq9CBEfJ3867&c3aCq9CBEfJ3867&c3aCq9CBEfJ' + name +
			            'JpgsP?rGem8AC?JKJpgsP?rGem8AC?JK',
			            p=pas))
		else:
			return redirect(
			    url_for('permission_admin', n='buber', u=name, p=pas))
	return render_template('code.html')

@app.route('/code/<u>/user/<n>/<p>/')
def code_link(u, n, p):
	if n in a and p in a:
		return render_template('code_user.html', n=n)
	else:
		return redirect(url_for('permission_admin', n='buber', u=n, p=p))

@app.route('/permission_denied/<n>/<u>/<p>/')
def permission_admin(n, u, p):
	return render_template('permission.html', n=n, u=u, p=p)

if __name__ == "__main__":
	app.run(debug=True, port=5500, host="0.0.0.0")
