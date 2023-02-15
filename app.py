from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('mushrooms.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        cap_shape = int(request.form['cap_shape'])
        cap_surface = int(request.form['cap_surface'])
        cap_color = int(request.form['cap_color'])
        bruises = int(request.form['bruises'])
        odor = int(request.form['odor'])
        gill_attachment = int(request.form['gill_attachment'])
        gill_spacing = int(request.form['gill_spacing'])
        gill_size = int(request.form['gill_size'])
        gill_color = int(request.form['gill_color'])
        stalk_shape = int(request.form['stalk_shape'])
        stalk_root = int(request.form['stalk_root'])
        stalk_surface_above_ring = int(request.form['stalk_surface_above_ring'])
        stalk_surface_below_ring = int(request.form['stalk_surface_below_ring'])
        stalk_color_above_ring = int(request.form['stalk_color_above_ring'])
        stalk_color_below_ring = int(request.form['stalk_color_below_ring'])
        veil_color = int(request.form['veil_color'])
        ring_number = int(request.form['ring_number'])
        ring_type = int(request.form['ring_type'])
        spore_print_color = int(request.form['spore_print_color'])
        population = int(request.form['population'])
        habitat = int(request.form['habitat'])
        
    values = np.array([[cap_shape,cap_surface,cap_color,bruises,odor,gill_attachment,
                        gill_spacing,gill_size,gill_color,stalk_shape,stalk_root,
                        stalk_surface_above_ring,stalk_surface_below_ring,stalk_color_above_ring,
                        stalk_color_below_ring,veil_color,ring_number,ring_type,
                        spore_print_color,population,habitat]])

    prediction = model.predict(values)
    if prediction == 0:
        label = 'Edible'
    else:
        label = 'Poisonous'

    return render_template('result.html', prediction_text='Mushroom is {}'.format(label))





if __name__ == "__main__":
    app.run(debug=True)