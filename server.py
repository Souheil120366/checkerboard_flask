from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.errorhandler(404) 
def handle_error(error):
    res="<script>alert('Sorry! No response. Try again.')</script>"
    return res

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def checkerboard_display():
    return render_template("index.html", row=8,column=8,col1="#FF0000",col2="#000000")
    
@app.route('/<int:x>')          # The "@" decorator associates this route with the function immediately following
def checkerboard_display_four(x):
    return render_template("index.html", row=x,column=8,col1="#FF0000",col2="#000000")

@app.route('/<int:x>/<int:y>')          # The "@" decorator associates this route with the function immediately following
def checkerboard_display_x_y(x,y):
    return render_template("index.html", row=x,column=y,col1="#FF0000",col2="#000000")

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')          # The "@" decorator associates this route with the function immediately following
def checkerboard_display_x_y_color(x,y,color1,color2):
    return render_template("index.html", row=x,column=y,col1=color1,col2=color2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
