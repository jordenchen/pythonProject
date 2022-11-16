chrome.action.onClicked.addListener(function(tab) {
  chrome.action.setTitle({tabId: tab.id, title: "You are on tab:" + tab.id});
  var title = chrome.tabs.title;
  var url = chrome.tabs.url;
  chrome.tabs.create({
      url: 'https://cms.sekorm.com/content/nps/selfSubject/add'
    },

  );

  chrome.tabs.on
});