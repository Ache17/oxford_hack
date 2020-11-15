chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({color: '#3aa757'}, function() {
      console.log('The color is green.');
    });
    chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
      chrome.declarativeContent.onPageChanged.addRules([{
        conditions: [new chrome.declarativeContent.PageStateMatcher({
          
        })
        ],
            actions: [new chrome.declarativeContent.ShowPageAction()]
      }]);
    });
  });
  chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({color: '#3aa757'}, function() {
      console.log('The color is green.');
    });
    chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
      chrome.declarativeContent.onPageChanged.addRules([{
        conditions: [new chrome.declarativeContent.PageStateMatcher({
          
        })
        ],
            actions: [new chrome.declarativeContent.ShowPageAction()]
      }]);
    });
  });
function doStuffWithDom(){
  chrome.pageAction.setTitle({text: 'ON'});
}
chrome.webNavigation.onCompleted.addListener(function(details) {
    chrome.pageCapture.saveAsMHTML({tabId: details.tabId}, function(mhtml) {
        var textMhtml = mhtml.text();
        var res;
        promise = textMhtml.then(function(result){
          res = JSON.stringify(result);
          var xhr = new XMLHttpRequest();
          xhr.open("POST", "http://localhost:8000/api/caption");
          xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
          xhr.setRequestHeader("Accept", "application/json");
          xhr.onreadystatechange = function()
          {
              let response1 =  JSON.parse(this.responseText);
              let xhrg = new XMLHttpRequest();
              xhrg.open("POST", "http://localhost:8000/api/captions");
              xhrg.setRequestHeader("Content-Type", "application/json");
              xhrg.setRequestHeader("Accept", "application/json"); 

              final = JSON.stringify({"ID": response1['ID']});
              xhrg.onreadystatechange = function(){
                  let respo =  JSON.parse(this.responseText);
                  if(respo['done']=="yes"){
                    //CODE TO ALTER IMAGES
                    chrome.tabs.sendMessage(details.tabId, {text: 'report_back', captions: respo["result"]}, doStuffWithDom);
                }
              }
              
              xhrg.send(final);
          }
          xhr.send(JSON.stringify({"mhtml": res}));
        });
      }
    );
});
