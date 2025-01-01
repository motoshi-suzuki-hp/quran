from phonemizer import phonemize
import difflib

class EvaluationService:
    @staticmethod
    def text_to_phonemes(text: str) -> list:
        return phonemize(text, language="ar", backend="espeak").split()

    @staticmethod
    def grab_gestalt(word1: str, word2: str) -> float:
        return round(difflib.SequenceMatcher(None, word1, word2).ratio()*100)

    @staticmethod
    def evaluate_pronunciation(predicted_phonemes, expected_phonemes, predicted_text, expected_text):
        feedback = []
        for idx, (predicted, expected) in enumerate(zip(predicted_phonemes, expected_phonemes)):
            feedback_item = {
                "position": idx,
                "expected_text": expected_text.split()[idx],
                "expected_phoneme": expected,
                "predicted_text": predicted_text.split()[idx],
                "predicted_phoneme": predicted,
                "similarity": EvaluationService.grab_gestalt(expected, predicted) if predicted != expected else 100,
                "message": f"位置 {idx+1} の音素 '{predicted}' を '{expected}' に修正してください。" if predicted != expected else "発音が良好です！"
            }
            feedback.append(feedback_item)
        return feedback
    
