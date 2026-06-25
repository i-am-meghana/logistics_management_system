from flask import Flask
from packages import get_package,view_packages,create_package,update_package,delete_package



app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/company")
def company():
    return {"name": "FEDx"}


@app.route("/packages/<int:id>")
def find_package_endpoint(id):
    return get_package(id)
    

@app.route("/packages")
def all_packages_endpoint():
    return view_packages()

@app.route("/packages", methods = ["POST"])
def package_creation():
    return create_package()

@app.route("/packages/<int:id>", methods = ["PUT"])
def package_update(id):
    return update_package(id)

@app.route("/packages/<int:id>", methods=["DELETE"])
def package_delete(id):
    return delete_package(id)

app.run(debug=True) #hits this starts the server and stops exe 