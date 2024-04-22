from paddleocr import PaddleOCR
from moviepy.editor import VideoFileClip
import speech_recognition as sr
import os

# Inicializa o objeto PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')


class OCRProcessor:
    def __init__(self, model_language='en'):
        """
        Inicializa o processador OCR.

        Args:
            model_language (str): O idioma do modelo OCR a ser utilizado. O padrão é 'en' (inglês).
        """
        self.model_language = model_language
        self.ocr = PaddleOCR(use_angle_cls=True, lang=self.model_language)

    def read_content_file(self, caminho_arquivo):
        """
        Esta função lê o conteúdo de um arquivo de texto.

        Args:
            caminho_arquivo (str): O caminho do arquivo a ser lido.

        Returns:
            str: O conteúdo do arquivo.
        """
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        return conteudo

    def extract_text_from_pdf_paddle(self, pdf_path):
        """
        Extrai texto OCR de um PDF usando PaddleOCR.

        Args:
            pdf_path (str): O caminho do arquivo PDF.

        Returns:
            str: O texto extraído do PDF.
        """
        # Use o método `ocr.ocr()` para extrair texto de uma imagem
        result = self.ocr.ocr(pdf_path, cls=True)

        # Concatene todas as palavras detectadas em uma única string
        text = '\n'.join([' '.join([word[1][0] for word in line]) for line in result])
        return text

    def extract_audio_from_mp4(self, mp4_path):
        """
        Extrai áudio de um arquivo MP4 (video).

        Args:
            mp4_path (str): O caminho do arquivo MP4.

        Returns:
            AudioFileClip: O objeto de áudio extraído.
        """
        video_clip = VideoFileClip(mp4_path)
        audio_clip = video_clip.audio
        return audio_clip

    def extract_text_from_audio(self, audio_clip):
        """
        Extrai texto OCR de um arquivo de áudio.

        Args:
            audio_clip (AudioFileClip): O objeto de áudio.

        Returns:
            str: O texto extraído do áudio.
        """
        recognizer = sr.Recognizer()

        # Salva o áudio temporariamente em um arquivo WAV
        temp_wav_file = "temp_audio.wav"
        audio_clip.write_audiofile(temp_wav_file)

        # Lê o áudio do arquivo WAV
        with sr.AudioFile(temp_wav_file) as source:
            audio = recognizer.record(source)

        # Usa o reconhecimento de fala do Google para converter o áudio em texto
        try:
            text = recognizer.recognize_google(audio, language='pt-BR')  # Especifica o idioma como Português do Brasil
            return text
        except sr.UnknownValueError:
            return "Não foi possível reconhecer o áudio"
        except sr.RequestError as e:
            return f"Erro no serviço de reconhecimento de fala: {e}"
        finally:
            # Remove o arquivo WAV temporário
            os.remove(temp_wav_file)

