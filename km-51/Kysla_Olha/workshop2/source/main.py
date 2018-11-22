"""
Створити два словника Makeups_features, Feature  
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/api/<action>', methods=['GET'])
def apiget(action):
    if action == "makeups_features":
        return render_template("makeups_features.html", makeups_features_result=first_table_dict, table_name=action)

    elif action == "features":
        return render_template("features.html", features_result=second_table_dict, table_name=action)

    elif action == "all":
        table_name = ['first_table', 'second_table']
        return render_template("all.html", first_table_result=first_table_dict, second_table_result=second_table_dict, table_name=table_name)

    else:
        return render_template("404.html", action_value=action)


@app.route('/api', methods=['POST'])
def apipost():

    if request.form["action"] == "update_makeups_features":
        first_table_dict["makeup_id_fk"] = request.form["makeup_id_fk"]
        first_table_dict["feature_name_fk"] = request.form["feature_name_fk"]
        first_table_dict["makeup_attribute"] = request.form["makeup_attribute"]

    if request.form["action"] == "update_features":
        second_table_dict["feature_name"] = request.form["feature_name"]


    return redirect(url_for('apiget', action="all"))


if __name__ == '__main__':


    first_table_dict = {
        "makeup_id_fk": 1,
        "feature_name_fk": "face",
        "makeup_attribute": "oval"
    }

    second_table_dict = {
        "feature_name": "face"
    }

    app.run(debug=True)
