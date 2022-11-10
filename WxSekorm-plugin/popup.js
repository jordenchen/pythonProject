function reddenPage() {

  window.location.href="https://cms.sekorm.com/content/nps/selfSubject/add" ;
  console.log(document.title);
  console.log(document.URL);
}

chrome.action.onClicked.addListener((tab) => {
  if(!tab.url.includes("chrome://")) {
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      function: reddenPage
    });
  }
});


// chrome.tabs.query({active : true}).then(tabs => submitContent(tabs));
//
// function submitContent(tabs){
//   const url = tabs[0].url;
//   const title = tabs[0].title;
//   console.log(url);
//   console.log(title);
// }

// function getMilestone(tabs) {
//   const div = document.createElement("div");
//   document.body.appendChild(div);
//   const url = tabs[0].url;
//   const origin = 'https://chromium-review.googlesource.com';
//   const search = `^${origin}/c/chromium/src/\\+/(\\d+)`;
//   const match = url.match(search);
//   if (match != undefined && match.length == 2) {
//     getMilestoneForRevId(match[1]).then(
//         (milestone) => milestone != '' ? (div.innerText = `m${milestone}`)
//                                        : window.close());
//   } else {
//     window.close();
//   }
// }
//
// async function getMilestoneForRevId(revId) {
//   const res = await fetch(`https://crrie.com/c/?r=${revId}`);
//   return await res.text();
// }