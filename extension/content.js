chrome.runtime.onMessage.addListener(function (msg, sender, sendResponse) {
    // If the received message has the expected format...
    if (msg.text === 'report_back') {
        // Call the specified callback, passing
        // the web-page's DOM content as argument
        console.log(msg.captions[i]);
        let images = document.getElementsByTagName('img');
        for (var i = 0, l = images.length; i < l; i++) {
            images[i].alt = msg.captions[i];    
        }
    }
});