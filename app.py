from flask import Flask, render_template, request, send_file
from text_summary2 import summarizer
from gtts import gTTS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse', methods=['GET', 'POST'])
def analyse():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summary, origenel_text, len_orig_text, len_summary = summarizer(rawtext)
        
        # Generate Audio summary
        language = 'en'
        audio_summary = gTTS(summary, lang=language, slow = False)
        audio_file = 'summary.mp3'
        audio_summary.save(audio_file)
        
    return render_template('summary.html', summary=summary, original_txt = origenel_text,len_orig_text = len_orig_text, len_summary = len_summary)

@app.route('/download')
def download():
    # Send the audio file for download
    return send_file('summary.mp3', as_attachment=True)




if __name__ == "__main__":
    app.run(debug=True)