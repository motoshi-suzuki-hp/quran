export interface Data {
    id: number;
    surah_id: number;
    ayah_id: number;
    text: string;
    phoneme: string;
}

export interface Feedback {
    position: number;
    expected_text: string;
    expected_phoneme: string;
    predicted_text: string;
    predicted_phoneme: string;
    similarity: number;
    message: string;
    audio_url: string;
}
