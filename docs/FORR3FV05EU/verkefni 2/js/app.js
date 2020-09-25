// these need to accessed inside more then one function so we'll declare them first
let countainer;
let camera;
let renderer;
let scene;
let mesh;

function init(){ 
   /* 
   Tutorial: 1.1 
   https://discoverthreejs.com/book/first-steps/first-scene/

   A bare-bones three.js app. The App is divided up into 6 steps:

      1. Initial Setup
         see index.html and main.css + DOM reference to html (container)
      2. The Scene 
         A holder (a data structure - scene graph) for all the visible objects you want to display.
         https://threejsfundamentals.org/threejs/lessons/threejs-scenegraph.html
      3. The Camera  
         To view your scene
      4. Visible Objects  (Mesh)
         A Mesh is just a holder for a Geometry (shape) and a Material (the way that the surface of the Mesh looks.)
         and Mesh also defines the position in 3D space. Can be a dog, person, mountains etc.
         Note! There are also other kinds of visible objects lines and shapes and sprites and particles and so on
      5. The Renderer
         A machine that takes a Camera and a Scene as input 
         and outputs beautiful drawings (or renderings) onto your <canvas>
      6. Render The Scene
   */

   // 1. Get a reference to the container element that will hold our scene
   container = document.querySelector( '#scene-container' );

   // 2. The Scene
   scene = new THREE.Scene(); //  create a scene instance from a Scene constructor
   scene.background = new THREE.Color( 'skyblue' ); // Set the background color (any CSS color name) from a Color constructor

   // 3. Create a Camera and define viewing frustum (parameters)
   const fov = 35; // AKA Field of View, the angle in degrees, valid range is 1 - 179 degrees.
   const aspect = container.clientWidth / container.clientHeight;
   const near = 0.1; // the near clipping plane (1 unit = 1 meter), Objects closer to the camera than .near will not be visible. Must be greater than 0, and less than the .far plane
   const far = 100; // the far clipping plane, Objects further away from the camera than this will not be visible
   /* The goal is to make .near as big as possible, and .far as small as possible while keeping far bigger than .near. 
   This way you can make the area contained in the frustum as small as possible, which is important for efficiency as we chase that elusive goal of 60 frames per second.
   */
   camera = new THREE.PerspectiveCamera( fov, aspect, near, far ); // Create camera with a perspective projection 
   // There is also an OrthographicCamera (2D games or user interfaces drawn on top of a 3D game (or 3D website)
   camera.position.set( 0, 0, 10 ); // We'll move the camera back a bit so that we can view the scene, right handed coordinate system
   // every object is initially created at ( 0, 0, 0 ) so 


   // 4. Visible Objects
   const geometry = new THREE.BoxBufferGeometry( 2, 2, 2 ); // create a geometry
   const textureLoader = new THREE.TextureLoader(); // create a texture loader
   const texture = textureLoader.load( 'textures/uv_test_bw.png' ); // Load a texture. See the note in chapter 4 on working locally, or the page # https://threejs.org/docs/#manual/introduction/How-to-run-things-locally # if you run into problems here
   texture.encoding = THREE.sRGBEncoding; // set the "color space" of the texture
   texture.anisotropy = 16; // reduce blurring at glancing angles
   const material = new THREE.MeshStandardMaterial( { // create a Standard material using the texture we just loaded as a color map
      map: texture,
    } );
   
   mesh = new THREE.Mesh( geometry, material ); // create a Mesh containing the geometry and material
   scene.add( mesh ); // add the mesh to the scene if we want to see it (mesh is called a child of the scene). scene.remove(object) removes from scene
   // to access material then mesh.material

   //Create a directional
   const light = new THREE.DirectionalLight( 0xffffff, 3.0);

   // move the light back and up a bit
   light.position.set( 10, 10, 10 );

   // remember to add the light to the scene
   scene.add( light );

   // 5. Create the renderer (a machine), a number of renderers are available in three.js,
   renderer = new THREE.WebGLRenderer( { antialias: true } ); // most full-featured and powerful, creates canvas automatically
   renderer.setSize( container.clientWidth, container.clientHeight ); // in Chrome that default canvas size is 150 x 300 pixels, needs auto resize fix
   renderer.setPixelRatio( window.devicePixelRatio );

   // set the gamma correction so that output colors look
   // correct on our screens
   renderer.gammaFactor = 2.2;
   renderer.gammaOutput = true;

   container.appendChild( renderer.domElement ); // add the automatically created <canvas> element to the page
   // Note! We can create one manually and tell the renderer to use that instead if we need greater control.

   renderer.setAnimationLoop( () => {

      update();
      render();

   } );

}
function animate() {
   // call animate recursively
   requestAnimationFrame( animate );

   // 6. render, or 'create a still image' with the camera of the scene and output to canvas
   renderer.render( scene, camera );
}

function update(){
   
   // increase the mesh's rotation each frame
   mesh.rotation.z += 0.01;
   mesh.rotation.x += 0.01;
   mesh.rotation.y += 0.01;

}

// render, or 'draw a still image', of the scene
function render(){

   renderer.render( scene, camera );

}

function onWindowResize() {

   // set the aspect ratio to match the new browser window aspect ratio
   camera.aspect = container.clientWidth / container.clientHeight;


   // update the camera's frustum
   camera.updateProjectionMatrix();

   // update the size of the renderer AND the canvas
   renderer.setSize( container.clientWidth, container.clientHeight )
   

   console.log( 'You resized the browser window!' );

}

window.addEventListener( 'resize', onWindowResize );

// call the init function to set everything up
init();

// call on the animate function to start the animateion
animate();