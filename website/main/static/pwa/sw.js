var cacheKeeplist = {
    'static' : 'static-v' + 1.6,
    'dynamic' : 'dynamic-v' + 1.6,
};

self.addEventListener('install', (event) => {
  console.log('sw installing ...');
  event.waitUntil(
    caches.open(cacheKeeplist['static']).then((cache) => {
      return cache.addAll([
        '/static/bootstrap.bundle.min.js',
        '/static/bootstrap.min.css',
        '/static/sweetalert2.js',
      ]);
    })
  );
});


self.addEventListener('activate', (event) => {
console.log('sw activate ...');
  event.waitUntil(
    caches.keys().then((keyList) => {
      return Promise.all(keyList.map((key) => {
        if (cacheKeeplist['static'] != key) {
          return caches.delete(key);
        }
      }));
    })
  );
  return self.clients.claim();
});


self.addEventListener('fetch', function(event) {
  
  function then_fetch(response){
    var response2 = response.clone();
    caches.open(cacheKeeplist['dynamic']).then(
      function(cache){
        cache.put(event.request, response2);
      }
    )
    return response;
  }

  function then_open_static(cache){
    return cache.match(event.request).then(function (response) {
      return response || fetch(event.request).then(then_fetch)
    });
  }

  // check static cache at 1 level
  var result = caches.open(cacheKeeplist['static']).then(then_open_static)
  
  event.respondWith(result);
});
