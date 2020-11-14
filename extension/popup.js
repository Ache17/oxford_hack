//let parser = require('mhtml-parser');

document.addEventListener('DOMContentLoaded', function() {
  var link = document.getElementById('trigger');
  // onClick's logic below:
  link.addEventListener('click', function() {
    console.log("click registered");
    chrome.tabs.query(
      {active: true, lastFocusedWindow: true},
      function(array_of_Tabs) {
        if (array_of_Tabs.length > 0) {
          var tab = array_of_Tabs[0];
          console.log("submitMHTML() found the active tab has an ID of " + tab.id);
          chrome.pageCapture.saveAsMHTML({tabId: tab.id}, function(mhtml) {
              //const html = mhtml2html.convert(mhtml);
              console.log(mhtml.text())
              console.log("submitMHTML() sent mhtml to server");
            }
          )
        }
      }
    );
  });
});



