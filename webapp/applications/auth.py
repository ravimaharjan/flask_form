from applications import *
from forms.login_form import LoginForm
auth_app = Blueprint("auth_app", __name__, template_folder='templates')

@auth_app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login Successful for user {0}, remember_me {1}".format(
            form.username.data, form.remember_me.data))
        # return render_template('index.html')
        return redirect(url_for('home_app.index'))
    return render_template('login.html', form=form)
