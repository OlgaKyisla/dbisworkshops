from flask import Flask, render_template, request, flash, session, url_for, redirect, make_response
from forms.reg_user import RegForm
from forms.log_user import LogForm
from forms.admin_add import AdminAdd
from forms.admin_edit import AdminEdit
from dao.userhelper import *

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/')
def index():

    if 'u_email' in session:
        u_email = session['u_email']
        return redirect(url_for('search'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogForm()
    if request.method == 'POST':
        if not form.validate():
            return render_template('login.html', form=form)
        else:
            u_bool = is_user(u_email=request.form["email"], u_pass=request.form["password"])
            if u_bool == [(1,)]:
                email = request.form["email"]
                role = get_user_role(request.form["email"])
                if role == 'user':
                    session['u_email'] = email
                    redirect(url_for('search'))
                if role == 'admin':
                    session['u_email'] = email
                    redirect(url_for('search'))
                if role == 'blocked_user':
                    return render_template('login.html', blocked=True, form=form)
                return redirect('/')
            else:
                error = "User do not exist"
                return render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form)


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegForm()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required.')
            return render_template('reg.html', form=form)
        else:
            u_bool = count_email(u_email=request.form["email"])
            if u_bool == 1:
                error = "User already exist"
                return render_template('reg.html', form=form, error=error)
            else:
                new_user(request.form["email"], None, request.form["name"], request.form["password"])
                session['u_email'] = request.form["email"]
            return redirect(url_for('search'))

    return render_template('reg.html', form=form)


@app.route('/search', methods=['GET', 'POST'])
def search():

    role = get_user_role(session.get('u_email'))
    admin = False
    if role == 'admin':
        admin=True

    features = [x[0] for x in get_feature()]

    skin_tone = ['fair', 'light', 'medium', 'deep']
    undertone = ['warm', 'neutral', 'cool']
    skin_type = ['dry', 'normal', 'oily', 'combination']
    makeup_benefit = ['anti align', 'all day wear', 'comfortable wear', 'mineral formula']
    makeup_foundation = ['liguid', 'cream', 'powder']
    face_type = ['oval', 'round', 'oblong']
    eyes_color = ['green', 'blue', 'gray', 'broun']

    features_options = {
        'face type': face_type,
        'eyes color': eyes_color,
        'skin type': skin_type,
        'skin tone': skin_tone,
        'skin undertone': undertone,
        'makeup foundation': makeup_foundation,
        'makeup benefit': makeup_benefit
    }

    return render_template('search.html', features=features, features_options=features_options, makeup_display=None, admin=admin)


@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.form["action"] == "update":
        u_email = session.get('u_email')
        insert_to_user_feature('face type', u_email, request.form["face type"])
        insert_to_user_feature('eyes color', u_email, request.form["eyes color"])
        insert_to_user_feature('skin type', u_email, request.form["skin type"])
        insert_to_user_feature('skin tone', u_email, request.form["skin tone"])
        insert_to_user_feature('skin undertone', u_email, request.form["skin undertone"])
        insert_to_user_feature('makeup foundation', u_email, request.form["makeup foundation"])
        insert_to_user_feature('makeup benefit', u_email, request.form["makeup benefit"])

        table = get_users_makeup(u_email)

    return render_template('search.html', table=table, search_display=None)


@app.route('/logout', methods=['GET', 'POST'] )
def logout():
    session.pop('u_email', None)
    return redirect(url_for('login'))


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AdminAdd()
    if request.form["action"] == "add":
        return render_template('admin_add.html', form=form)
    return render_template('admin_add.html', form=form)


@app.route('/add_action', methods=['GET', 'POST'])
def add_action():
    form = AdminAdd()
    if request.method == 'POST':
        if not form.validate():
            return render_template('admin_add.html', form=form)
        else:
            new_makeup(request.form["name"], request.form["price"], request.form["quantity"], request.form["description"])
            return render_template('admin_add.html', form=form, successful=True)
    return render_template('admin_add.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    table = get_makeup()
    makeup_id = [x[0] for x in get_makeup_id()]
    if request.method == 'POST':
        if request.form["action"] == "delete":
            return render_template('admin_delete.html', table=table, makeup_id=makeup_id)
    return render_template('admin_delete.html', table=table, makeup_id=makeup_id)


@app.route('/delete_action', methods=['GET', 'POST'])
def delete_action():
    if request.form["makeup"] == "delete_makeup":
        id = request.form["id"]
        delete_makeup(id)
        return redirect(url_for('delete'))
    return render_template('admin_delete.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    table = get_makeup()
    makeup_id = [x[0] for x in get_makeup_id()]
    if request.method == 'POST':
        if request.form["action"] == "edit":
            return render_template('admin_edit.html', table=table, makeup_id=makeup_id)

    return render_template('admin_edit.html', table=table, makeup_id=makeup_id)


@app.route('/edit_action', methods=['GET', 'POST'])
def edit_action():
    form = AdminEdit()
    id = request.form["id"]

    resp = make_response()
    resp.set_cookie('id', id)
    session['id'] = id

    makeup = get_makeup_by_id(id)
    name = [x[1] for x in makeup][0]
    price = [x[2] for x in makeup][0]
    quantity = [x[3] for x in makeup][0]
    description = [x[4] for x in makeup][0]

    return render_template('admin_edit_action.html', form=form, name=name, price=price, quantity=quantity, description=description, id=id)


@app.route('/to_edit', methods=['GET', 'POST'])
def to_edit():
    form = AdminEdit()
    if request.method == 'POST':
        if not form.validate():
            return render_template('admin_edit_action.html', form=form)
        else:
            edit_makeup(session.get('id'), request.form['name'], request.form['price'], request.form['quantity'], request.form['description'])
            return redirect(url_for('edit'))

    return render_template('admin_edit_action.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)