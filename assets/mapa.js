/* Mapas del sitio — prototipo.
   Leaflet (BSD-2) sobre teselas de OpenStreetMap (ODbL), sin API key ni cuenta.
   El gris lo pone el CSS (.leaflet-tile-pane), para no salirse de la paleta.
   Cada contenedor declara su configuración en data-mapa:
   {"centro":[lat,lng],"zoom":n,"pines":[[lat,lng,"etiqueta"],...]} */
(function () {
  if (typeof L === 'undefined') return;

  document.querySelectorAll('[data-mapa]').forEach(function (nodo) {
    var cfg;
    try { cfg = JSON.parse(nodo.getAttribute('data-mapa')); } catch (e) { return; }

    var mapa = L.map(nodo, {
      center: cfg.centro,
      zoom: cfg.zoom,
      scrollWheelZoom: false,   // la rueda sigue desplazando la página
      zoomControl: true
    });

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; colaboradores de <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      maxZoom: 19
    }).addTo(mapa);

    (cfg.pines || []).forEach(function (p) {
      L.circleMarker([p[0], p[1]], {
        radius: 9, color: '#1B1917', weight: 2,
        fillColor: '#1B1917', fillOpacity: 0.8
      }).addTo(mapa).bindPopup(p[2]);
    });

    // un clic habilita el zoom con rueda; al salir del mapa se vuelve a desactivar
    nodo.addEventListener('click', function () { mapa.scrollWheelZoom.enable(); });
    nodo.addEventListener('mouseleave', function () { mapa.scrollWheelZoom.disable(); });
  });
})();
