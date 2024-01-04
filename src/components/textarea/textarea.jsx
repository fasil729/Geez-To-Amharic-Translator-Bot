import { CalculateTextareaHeight } from './textAreaHeight';
import './textarea.css'
const TextArea = ({value}) => {
  return ( <textarea 
    style={{height:CalculateTextareaHeight()}} 
     defaultValue={value} className="textarea"/>);
}
 
export default TextArea;