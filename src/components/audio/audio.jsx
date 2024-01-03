import { useEffect } from "react";
import SpeechRecognition,{useSpeechRecognition} from "react-speech-recognition/lib/SpeechRecognition";

const SpeechToText  = () => {
  const {
    listening,
    transcript,
    browserSupportsSpeechRecognition,
    resetTranscript,

  }=useSpeechRecognition();
 useEffect(() => {
    if (browserSupportsSpeechRecognition) {
      SpeechRecognition.lang = "am-ET"; // Set the language for speech recognition
    }
  }, [browserSupportsSpeechRecognition]);
  if(!browserSupportsSpeechRecognition){
    return <div className="">
      your browser does't speech to text recognition
    </div>
  }
  return ( <div className="">
    <button onClick={SpeechRecognition.startListening}>Start</button>
    <button onClick={SpeechRecognition.stopListening}>Stop</button>
    <button onClick={resetTranscript}>Reset</button>
    <p>start{transcript}</p>
  </div> );
}
 
export default SpeechToText ;