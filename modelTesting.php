<?php
include_once "header.php";
?>

<div class="sketchfab-embed-wrapper"> <iframe title="(FREE) 1972 Datsun 240k GT" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/b2303a552b444e5b8637fdf5169b41cb/embed"> </iframe>
  <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;"> <a href="https://sketchfab.com/3d-models/free-1972-datsun-240k-gt-b2303a552b444e5b8637fdf5169b41cb?utm_medium=embed&utm_campaign=share-popup&utm_content=b2303a552b444e5b8637fdf5169b41cb" target="_blank" style="font-weight: bold; color: #1CAAD9;"> (FREE) 1972 Datsun 240k GT </a> by <a href="https://sketchfab.com/karolmiklas?utm_medium=embed&utm_campaign=share-popup&utm_content=b2303a552b444e5b8637fdf5169b41cb" target="_blank" style="font-weight: bold; color: #1CAAD9;"> Karol Miklas </a> on <a href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=b2303a552b444e5b8637fdf5169b41cb" target="_blank" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a></p>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.js"></script>
<!--<script src="GLTFLoader.js"></script>-->
<!--<script src="OrbitControls.js"></script>-->
<script>
  let scene, camera, renderer;

  function init() {
    scene = new THREE.Scene();
    scene.background = new THREE.Color('#FFFFFF') //0xdddddd);
    camera = new THREE.PerspectiveCamera(40, window.innerWidth / window.innerHeight, 1, 5000);
    camera.rotation.y = 45 / 180 * Math.PI;
    camera.position.x = 800;
    camera.position.y = 100;
    camera.position.z = 1000;
    //controls = new THREE.OrbitControls(camera);
    //controls.addEventListener('change', renderer);
    hlight = new THREE.AmbientLight(0x404040, 100);
    scene.add(hlight);
    directionalLight = new THREE.DirectionalLight(0xffffff, 100);
    directionalLight.position.set(0, 1, 0);
    directionalLight.castShadow = true;
    scene.add(directionalLight);
    light = new THREE.PointLight(0xc4c4c4, 10);
    light.position.set(0, 300, 500);
    scene.add(light);
    light2 = new THREE.PointLight(0xc4c4c4, 10);
    light2.position.set(500, 100, 0);
    scene.add(light2);
    light3 = new THREE.PointLight(0xc4c4c4, 10);
    light3.position.set(0, 100, -500);
    scene.add(light3);
    light4 = new THREE.PointLight(0xc4c4c4, 10);
    light4.position.set(-500, 300, 500);
    scene.add(light4);
    renderer = new THREE.WebGLRenderer({
      antialias: true
    });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);
    const loader = new OBJLoader();

    loader.load('Earth.gltf', function(object) {
        //car = gltf.scene.children[0];
        //car.scale.set(0.5, 0.5, 0.5);
        scene.add(object);
      },
      function(xhr) {
        console.log((xhr.loaded / xhr.total * 100) + '% loaded');
        animate();
      }
    );
  }

  function animate() {
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
  }
  init();
</script>

<?php
include_once "footer.php";
?>