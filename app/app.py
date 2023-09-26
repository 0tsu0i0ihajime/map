from flask import Flask, render_template
import subprocess

app = Flask(__name__)

def run_osm_program():
    result = "Hello World!"
    return result
    # try:
    #     result = subprocess.check_output(["python", "osm_map.py"]).decode("utf-8")
    #     return result
    # except Exception as e:
    #     return str(e)
    
@app.route('/')
def index():
    # result = run_osm_program()
    # return render_template('./index.html', result = result)
    return render_template('./index.html')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False, host="0.0.0.0", port=5000)