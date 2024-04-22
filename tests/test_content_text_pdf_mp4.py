from utils.content_extract import OCRProcessor
from moviepy.editor import VideoFileClip
import sys
class DocumentProcessor:
    def __init__(self):
        self.ocr_processor = OCRProcessor()

    def process_document_txt(self, txt_path):  # Corrigido para receber o caminho do arquivo TXT
        txt = self.ocr_processor.read_content_file(txt_path)  # Passa o caminho do arquivo TXT
        return txt

    def process_document_pdf(self, pdf_path):  # Corrigido para receber o caminho do arquivo PDF
        ocr_pdf = self.ocr_processor.extract_text_from_pdf_paddle(pdf_path)  # Passa o caminho do arquivo PDF
        return ocr_pdf

    def extract_audio_from_mp4(self, mp4_path):
        """
        Extrai áudio de um arquivo MP4.

        Args:
            mp4_path (str): O caminho do arquivo MP4.

        Returns:
            AudioFileClip: O objeto de áudio extraído.
        """
        video_clip = VideoFileClip(mp4_path)
        audio_clip = video_clip.audio
        try:
            # Verifica se o processo ainda está em execução antes de tentar terminá-lo
            if video_clip.reader.proc.poll() is None:
                video_clip.close()
        except Exception as e:
            pass
        return audio_clip

if __name__ == "__main__":
    document_processor = DocumentProcessor()

    # # TEXTO
    # file_text = "C:/Projects/PESSOAL/aiEngineeringChallenge/challenge-artificial-intelligence/resources/modulos_aprendizagem_gerados_chatGPT"
    # content_txt = document_processor.process_document_txt(file_text)
    # print(content_txt)

    # # PDF
    # file_pdf = "C:/Projects/PESSOAL/aiEngineeringChallenge/challenge-artificial-intelligence/resources/Capítulo do Livro.pdf"
    # content_pdf = document_processor.process_document_pdf(file_pdf)
    # print(content_pdf)

    # # OBJECT MP4
    # mp4_path = "C:/Projects/PESSOAL/aiEngineeringChallenge/challenge-artificial-intelligence/resources/Dica do professor.mp4"
    # extracted_audio = document_processor.ocr_processor.extract_audio_from_mp4(mp4_path)
    # print(extracted_audio)

    # OCR MP4
    mp4_path = "C:/Projects/PESSOAL/aiEngineeringChallenge/challenge-artificial-intelligence/resources/Dica do professor.mp4"

    # Extração de áudio do arquivo MP4
    extracted_audio = document_processor.ocr_processor.extract_audio_from_mp4(mp4_path)
    print(extracted_audio)

    # Extração de texto do áudio
    extracted_text = document_processor.ocr_processor.extract_text_from_audio(extracted_audio)
    print(extracted_text)



