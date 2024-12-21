import React, { useState, useRef } from 'react';
import '/app/src/App.css'

interface Feedback {
  position: number;
  expected_text: string;
  expected_phoneme: string;
  predicted_text: string;
  predicted_phoneme: string;
  similarity: number;
  message: string;
  audio_url: string;
}

const TEXT = 'بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ'
const PHONEME = 'bɪsmɪ llɑːhɪ rrɑħmɑːnɪ rrɑħiːm'

const App = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);

  const [expectedText, setExpectedText] = useState<string>("");
  const [recognizedText, setRecognizedText] = useState<string>("");
  const [feedback, setFeedback] = useState<Feedback[]>([]);
  

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorderRef.current = mediaRecorder;

    mediaRecorder.ondataavailable = (event) => {
      setAudioBlob(event.data); // 音声データを保存
    };

    mediaRecorder.start();
    setIsRecording(true);
  };

  const stopRecording = () => {
    mediaRecorderRef.current?.stop();
    setIsRecording(false);
  };

  const handleSubmit = async () => {
    if (!audioBlob) {
      alert("音声を録音してください。");
      return;
    }

    setIsLoading(true);
    const formData = new FormData();
    formData.append("audio", audioBlob, "recording.wav");
    formData.append("text", TEXT);

    try {
      const response = await fetch("http://127.0.0.1:5001/api/analyze", {
        method: "POST",
        body: formData,
      });
      const result = await response.json();
      console.log(result);
      // 結果の処理をここに記載
      setExpectedText(result.expected_text);
      setRecognizedText(result.recognized_text);
      setFeedback(result.feedback);  
      console.log(result.feedback);
    } catch (error) {
      console.error("エラーが発生しました:", error);
    } finally {
      setIsLoading(false);
    }
  };

  // 誤った音素が含まれる単語を赤く表示する関数
  const highlightIncorrectWords = (feedback: Feedback[]) => {
    return feedback.map((f, i) => {
      let isCorrect = f.similarity >= 85;
      return (
        <span key={i} style={{ color: isCorrect ? "green" : "red" }}>
          {f.predicted_text}{" "}
        </span>
      );
    });
  };

  return (
    <div className='app-content' style={{ padding: "20px" }}>
      <h1>{TEXT}</h1>
      <h2>/{PHONEME}/</h2>
      <div className='record'>
        {!isRecording ? (
          <button className='record-button' onClick={startRecording}>録音開始</button>
        ) : (
          <button className='record-button' onClick={stopRecording}>録音停止</button>
        )}
      </div>
      <button className='feedback-button' onClick={handleSubmit} disabled={isLoading || !audioBlob}>
        {isLoading ? "送信中..." : "フィードバックを取得"}
      </button>
      <div className='feedback'>
        {expectedText && !isLoading && (
          <div style={{ marginTop: "20px" }}>
            <h2>発音フィードバック</h2>

          <ul className='feedback-table'>
            <ol className='feedback-table-row'>
              <li>
                <p>予想されるテキスト:</p>
                <p>認識されたテキスト:</p>
                <p>適合率:</p>
              </li>
            </ol>

              <ol className='feedback-table-text'>
                {expectedText.split(" ").map((expectedItem, expectedIndex) => (
                  highlightIncorrectWords(feedback).map((recognizedItem, recognizedIndex) => (
                    feedback.map((item, index) => (
                      (recognizedIndex === index && expectedIndex === index) ? (
                        <li key={index}>
                          <p>{expectedItem}</p>
                          <p>{recognizedItem}</p>
                          <p style={{ color: item.similarity >= 85 ? "green" : "red" }}>{item.similarity}%</p>
                        </li>
                      ) : null
                    ))
                  ))
                ))}
              </ol>

              <ol className='feedback-table-text'>
                {feedback.map((item, index) => (
                  <li key={index}>
                  <p>{item.expected_text}</p>
                  <p style={{ color: item.similarity >= 85 ? "green" : "red" }}>{item.predicted_text}</p>
                  <p style={{ color: item.similarity >= 85 ? "green" : "red" }}>{item.similarity}%</p>
                  </li>
                ))}
              </ol>
          </ul>

            {feedback.length > 0 && (
              <div style={{ marginTop: "10px" }}>
                <h3>改善が必要な箇所:</h3>
                <ul className='feedback-list'>
                  {feedback.map((item, index) => (
                    <li key={index}>
                      <strong>ポイント {item.position + 1}</strong>
                      <div className='feedback-comments'>
                        <div>
                          <p>正しい発音</p>
                          <p>あなたの発音</p>
                          <p>適合率</p>
                          <p>改善方法</p>
                        </div>
                        <div>
                          <p>"{item.expected_text}" /{item.expected_phoneme}/ </p>
                          <p><span style={{ color: item.similarity >= 85 ? "green" : "red" }}>"{item.predicted_text}" /{item.predicted_phoneme}/</span></p>
                          <p><span style={{ color: item.similarity >= 85 ? "green" : "red" }}>{item.similarity}%</span></p>
                          <p>{item.message}</p>
                        </div>
                      </div>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
