import './App.css';
import axios from 'axios'

function handleClick(e) {
  e.preventDefault()
  axios.get('http:/listen').then(res => {
    console.log(res.data)
  })
}

function App() {
  return (
    <input type='submit' onClick={handleClick}></input>
  );
}

export default App;
