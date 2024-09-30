from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route 1: Home page
@app.route('/')
def home():
    return render_template('index.html')

# Route 2: User profile page (Dynamic Route)
@app.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', username=username)

# Route 3: Post page with post id (Dynamic Route)
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return render_template('post.html', post_id=post_id)

# Route 4: User overview page where you can search for a user
@app.route('/user-overview', methods=['GET', 'POST'])
def user_overview():
    if request.method == 'POST':
        username = request.form.get('username')
        return redirect(url_for('user_profile', username=username))
    return render_template('user_overview.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
