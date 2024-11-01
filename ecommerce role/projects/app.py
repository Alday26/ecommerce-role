from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Define role-based routes
@app.route('/admin')
def admin_dashboard():
    if session.get('role') == 'admin':
        return render_template('admin_dashboard.html', title="Admin Dashboard")
    return redirect(url_for('unauthorized'))

@app.route('/manager')
def manager_dashboard():
    if session.get('role') == 'manager':
        return render_template('manager_dashboard.html', title="Manager Dashboard")
    return redirect(url_for('unauthorized'))

@app.route('/customer')
def customer_dashboard():
    if session.get('role') == 'customer':
        return render_template('customer_dashboard.html', title="Customer Dashboard")
    return redirect(url_for('unauthorized'))

@app.route('/unauthorized')
def unauthorized():
    return render_template('unauthorized.html')

@app.route('/login/<role>')
def login(role):
    session['role'] = role
    return f"Logged in as {role}"

@app.route('/logout')
def logout():
    session.pop('role', None)
    return redirect(url_for('unauthorized'))

if __name__ == '__main__':
    app.run()
