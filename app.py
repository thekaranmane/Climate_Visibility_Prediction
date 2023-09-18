from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from MyCode import predict_Batch_Files
from helper import helperClass

app = Flask(__name__, template_folder='template', static_folder='static')
operations = helperClass()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def upload_file_to_predict_from_model():
    if request.method == 'POST':
        print("POST Method")
        from uFile import upload_file
        fileUploadResult = upload_file()
        if fileUploadResult['status'] == 'success':
            Folder_Name = 'uploadFiles'
            path = predict_Batch_Files(Folder_Name)
            path = "Prediction_Output_File/Predictions.csv"
            print(f"Prediction File created at: {path}")
            return jsonify({'result': 'success',
                            'msg': 'File uploaded successfully and Prediction File created',
                            'download': 'Prediction File',
                            'downloadLink': './../static/Prediction_Output_File/Predictions.csv'
                            })
        else:
            return jsonify({'result': 'error', 'msg': 'File uploaded failed'})
    else:
        return jsonify({'result': 'error', 'msg': 'File uploaded failed'})


@app.route('/clear', methods=['POST'])
def clear_files():
    try:
        path1 = "Prediction_Output_File"
        path2 = "static/Prediction_Output_File"
        path3 = "uploadFiles"
        operations.delete_file(path1)
        operations.delete_file(path2)
        operations.delete_folder(path3)
        return jsonify({'result': 'success', 'msg': 'All Output files and folders deleted successfully'})
    except Exception as e:
        return jsonify({'result': 'error', 'msg': 'Failed to delete all Output files and folders'})


if __name__ == "__main__":
    app.run(debug=True)
