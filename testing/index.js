async function sayHello() {
    let queryOptions = { active: true, lastFocusedWindow: true };
    let [tab] = await chrome.tabs.query({ active: true });
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: () => {
            console.log("first")
            alert('Hello from my extension!');
        }
    });
}

const butt = document.getElementsByClassName("screenshotbutton")[0]
console.log(butt)
butt.addEventListener("click", sayHello);
