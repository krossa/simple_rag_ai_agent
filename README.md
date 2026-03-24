## necessary libraries:
pypdf
sentence_transformers
chromadb
openai-whisper ffmpeg-python
openai

You also need to install ffmpeg on your machine     

## start up
set OpenAI API key
$env:OPENAI_API_KEY="your_key"

run
python -m app.main
in src/

The data source is located in the input/articles folder, containing articles about AI. All articles can be loaded into RAG as a single action
4) Load Data
It is possible to add more PDF or video files from the input folder (like in RAG project)
1) Upload PDF
2) Upload Video