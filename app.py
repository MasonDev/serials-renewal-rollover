from flask import Flask, render_template, request, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        # Perform data transformation using pandas or other libraries
        df = pd.read_excel(file)
        # Perform your data transformation here
        
        # Save the transformed data to a BytesIO object
        output_buffer = io.BytesIO()
        df.to_excel(output_buffer, index=False)
        output_buffer.seek(0)

        # Provide the transformed file for download
        return send_file(
            output_buffer,
            as_attachment=True,
            download_name='output.xlsx',
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
