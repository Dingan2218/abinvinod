const CACHE_NAME = 'abinvinod-seo-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/404.html',
  '/style.css',
  '/app.js',
  '/assets/project1.png',
  '/assets/project2.png',
  '/assets/project3.png',
  '/assets/anime_street_wallpaper.png',
  '/assets/marketing_showcase.png',
  '/assets/trisha_profile.png',
  '/assets/trisha_thumbnail.png',
  'https://unpkg.com/lucide@latest'
];

// Install Event
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    }).then(() => self.skipWaiting())
  );
});

// Activate Event
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cache) => {
          if (cache !== CACHE_NAME) {
            return caches.delete(cache);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch Event - Network first, falling back to cache
self.addEventListener('fetch', (event) => {
  // Only handle GET requests and local/safe schemes
  if (event.request.method !== 'GET' || !event.request.url.startsWith(self.location.origin) && !event.request.url.startsWith('https://unpkg.com')) {
    return;
  }

  event.respondWith(
    // Fetch from network with a timeout fallback
    fetchWithTimeout(event.request, 4000)
      .then((response) => {
        // Cache valid responses dynamically
        if (response && response.status === 200) {
          const responseToCache = response.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache);
          });
        }
        return response;
      })
      .catch(() => {
        // Fallback to cache if network fails or times out
        return caches.match(event.request).then((cachedResponse) => {
          if (cachedResponse) {
            return cachedResponse;
          }
          // Offline fallback
          if (event.request.headers.get('accept').includes('text/html')) {
            return caches.match('/404.html');
          }
        });
      })
  );
});

// Helper for fetch timeout
function fetchWithTimeout(request, timeout = 4000) {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error('Network request timed out')), timeout);
    fetch(request).then(
      (response) => {
        clearTimeout(timer);
        resolve(response);
      },
      (err) => {
        clearTimeout(timer);
        reject(err);
      }
    );
  });
}
