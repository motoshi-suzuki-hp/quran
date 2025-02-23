import '/app/src/App.css'
import '/app/src/pages/home.css'

const Home:React.FC = () => {

  const token = sessionStorage.getItem("access_token");


  return (
    <div className='app-content' style={{ padding: "20px" }}>
        <h1>Welcome to Quran.ai! 🎙️📖</h1>
        <div className="container">

          <p>Master the beauty of the <strong>Qur'an</strong> with correct pronunciation.</p>
          <p>Using advanced speech analysis, our app provides real-time feedback on your pronunciation.</p>
          <p>Whether you're a beginner or an advanced learner, our features will help you improve effectively!</p>

          <ul>
              <li>✅ <strong>Native Audio Comparison</strong> - Listen and mimic to enhance your listening skills</li>
              <li>✅ <strong>Automatic Pronunciation Check</strong> - AI analyzes your pronunciation and provides instant feedback</li>
              <li>✅ <strong>Record & Compare</strong> - Record your pronunciation and compare it with the correct version</li>
          </ul>

          {token ? <p className="startNow">Please select from the menu above 👆</p> : <a href="/login" className="startNow">Start Now 🚀</a>}
        </div>
    </div>
  );
};

export default Home;
