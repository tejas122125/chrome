import "./index.css"
function App() {
 let color = "green"
const copyButtons = document.querySelectorAll('.copybutton');
copyButtons.forEach(button => {
  button.addEventListener('click', () => {
    // Find the corresponding copy content
    button.classList.add('green-background');
    setTimeout(() => {
      button.classList.remove('green-background');
    }, 10000);
    const copyContent = button.previousElementSibling.textContent;
    // Copy the content to clipboard (You can implement copy functionality here)
    console.log('Copied content:', copyContent);
  });
});


const captureScreenshot = async (e)=>{
color = "red"
const block = document.getElementsByClassName("screenshot");
block[0].style.backgroundColor = color
console.log(block[0])
const [tab] =await chrome.tabs.query({active:true})

console.log(tab.id)
function injectedFunction() {
  document.body.style.backgroundColor = "orange";
}

chrome.scripting.executeScript({
  target : {tabId : tab.id},
  func : injectedFunction,
});


}

  return (
    <>
      
      <div className="main">
        <h2 className="header">Easy Code Snippet</h2>
        <div className="screenshot" style={{backgroundColor:color}}> <h4>Take ScreenShot</h4>
        <button onClick={captureScreenshot} className="screenshotbutton" >Take</button>
        </div>
        <div className="clipboard">
          <div className="clipboardcontent">
            <p className="copycontent">punit jinda bad fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff</p>
            <button className="copybutton">copy</button>
          </div>
          <div className="clipboardcontent">
            <p className="copycontent">punit jinda bad</p>
            <button className="copybutton">copy</button>
          </div>
          <div className="clipboardcontent">
            <p className="copycontent">punit jinda bad</p>
            <button className="copybutton">copy</button>
          </div>
          <div className="clipboardcontent">
            <p className="copycontent">punit jinda bad</p>
            <button className="copybutton">copy</button>
          </div>
          <div className="clipboardcontent">
            <p className="copycontent">punit jinda bad</p>
            <button className="copybutton">copy</button>
          </div>
         
        </div>


      </div>
    </>
  )
}

export default App
