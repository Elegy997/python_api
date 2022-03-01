from flask import *
import json
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/view")
def view():
    con = sqlite3.connect("employee.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Employees")
    rows = cur.fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route("/savedetails/", methods=["POST"])
def saveDetails():
    msg = "msg"
    try:
        data = request.get_json(force=True)
        print(data)
        name = data["name"]
        email = data["email"]
        address = data["address"]
        with sqlite3.connect("employee.db") as con:
            cur = con.cursor()
            cur.execute("INSERT into Employees (name, email, address) values (?,?,?)", (name, email, address))
            con.commit()
            msg = "Employee successfully Added"
    except:
        con.rollback()
        msg = "We can not add the employee to the list"
    finally:
        return name
        con.close()


if __name__ == "__main__":
    app.run(debug=True)
