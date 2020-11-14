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
              var xhr = new XMLHttpRequest();
              var textMhtml = JSON.stringify(mhtml.text());
              console.log(typeof(textMhtml));
              xhr.open("POST", "http://20.39.216.243/api/caption");
              xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
              xhr.setRequestHeader("Accept", "application/json");
              xhr.onreadystatechange = function(){
                console.log(this.responseText);
              }
              xhr.send(JSON.stringify({"mhtml":textMhtml}));
              console.log("submitMHTML() sent mhtml to server");
            }
          )
        }
      }
    );
  });
});



