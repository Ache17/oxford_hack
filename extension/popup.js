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
              var textMhtml = mhtml.text();
              var res;
              promise = textMhtml.then(function(result){
                res = JSON.stringify(result);
                var xhr = new XMLHttpRequest();
                xhr.open("POST", "http://143.110.166.160:8000/api/caption");
                xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                xhr.setRequestHeader("Accept", "application/json");
                xhr.onreadystatechange = function(){
                  console.log(this.responseText);
                }
                xhr.send(JSON.stringify({"mhtml": res}));
                console.log("submitMHTML() sent mhtml to server");
              });
            }
          )
        }
      }
    );
  });
});



