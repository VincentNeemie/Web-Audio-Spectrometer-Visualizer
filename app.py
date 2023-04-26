import io
import librosa
import librosa.display
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

def process_audio(filename):
    # Load the audio file
    y, sr = librosa.load(filename)

    # Compute the short-time Fourier transform (STFT)
    stft = librosa.stft(y)

    # Compute the magnitude spectrogram
    spectrogram = librosa.amplitude_to_db(abs(stft))

    # Plot the magnitude spectrogram
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(spectrogram, sr=sr, y_axis='linear')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Spectrogram')
    plt.tight_layout()

    # Save the plot to a memory buffer
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)

    return img_buf

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        img_buf = process_audio(f.filename)
        return send_file(img_buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
