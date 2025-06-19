if ('serviceWorker' in navigator) {
  navigator
    .serviceWorker
    .register('/static/pwa/sw.js');

}else{
    console.log('browser not supports service workers');
}
let deferredPrompt;
var btnAdd = document.getElementById('install');

window.addEventListener('beforeinstallprompt', function(event) {
  // Prevent Chrome 67 and earlier from automatically showing the prompt
  event.preventDefault();
  // Stash the event so it can be triggered later.
  deferredPrompt = event;
  btnAdd.disabled = false
  console.log('before install prompt  ' + event);
  
});


// Installation must be done by a user gesture! Here, the button click
btnAdd.addEventListener('click', (e) => {
  // hide our user interface that shows our A2HS button
  btnAdd.style.display = 'none';
  // Show the prompt
  
  deferredPrompt.prompt();
  // Wait for the user to respond to the prompt
  deferredPrompt.userChoice
    .then((choiceResult) => {
      if (choiceResult.outcome === 'accepted') {
        console.log('User accepted the A2HS prompt');
        fetch('/?pwa=1')
      } else {
        console.log('User dismissed the A2HS prompt');
      }
      deferredPrompt = null;
    });
});

