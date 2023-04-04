from flask import Flask, request ,render_template ,Response
from PIL import Image, ImageDraw, ImageFont
import io
import json
app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_id = request.form.get("vote", "")
        text = request.form.get("textfield", "")
        with open('votes.json', 'r') as f:
            data = json.load(f)
        data[selected_id]+=1
        with open('votes.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        return f"result = {data}"
    else:
        return render_template("index.html")

@app.route("/himalaya", methods=["GET", "POST"])
def himalaya():
    if request.method == "POST":
        selected_id = request.form.get("vote", "")
        text = request.form.get("textfield", "")
        with open('voteh.json', 'r') as f:
            data = json.load(f)
        data[selected_id]+=1
        with open('voteh.json', 'w') as f:
            json.dump(data, f, indent=4)

        return f"result = {data}"
    else:
        return render_template("index2.html")

@app.route("/reset", methods=["GET", "POST"])
def reset():
    with open('votehr.json', 'r') as f:
        data = json.load(f)
    with open('voteh.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    with open('votesr.json', 'r') as f:
        data = json.load(f)
    with open('votes.json', 'w') as f:
        json.dump(data, f, indent=4)

    return f"done"




app = Flask(__name__)

@app.route('/image')
def get_image():
    name = request.args.get('name')
    
    # Create image with transparent background
    image = Image.new('RGBA', (150, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 20)
    text_width, text_height = draw.textsize(name, font=font)
    draw.text(((150 - text_width) / 2, (50 - text_height) / 2), name, fill='black', font=font)
    
    # Return image as response with "image/png" mimetype
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    
    return Response(img_io.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)






