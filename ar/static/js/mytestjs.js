window.addEventListener('load', init);

function body_onload(){
  var res = $("#iTestText").val();
  $("#iTestText").val("3");
  console.log(res);
}
  
function init(){
  // サイズを指定
        const width = 320;
        const height = 240;

        // レンダラーを作成
        const renderer = new THREE.WebGLRenderer({
          canvas: document.querySelector('#myCanvas')
        });
        renderer.setPixelRatio(window.devicePixelRatio);
        renderer.setSize(width, height);

        // シーンを作成
        const scene = new THREE.Scene();

        // カメラを作成
        const camera = new THREE.PerspectiveCamera(60, width / height);
        camera.position.set(0, 0, 500);
        camera.lookAt(new THREE.Vector3(0, 0, 0));

        // ドーナツを作る
        const mesh = new Donuts();
        mesh.position.set(100, 0, 0);
        scene.add(mesh);

        // 平行光源
        const directionalLight = new THREE.DirectionalLight(0xFFFFFF);
        directionalLight.position.set(1, 1, 1);
        // シーンに追加
        scene.add(directionalLight);

        // skysphere
        console.log("sky");
        var skyGeo = new THREE.SphereGeometry(1300, 25, 25);
        var loader  = new THREE.TextureLoader(),
        texture = loader.load( "../static/models/spruit_sunrise.jpg" );
        var material0 = new THREE.MeshBasicMaterial({ map: texture,});
        //var material0 = new THREE.MeshNormalMaterial();

        const skyMesh = new THREE.Mesh(skyGeo, material0);
        skyMesh.material.side = THREE.BackSide;
        scene.add(skyMesh);



        tick();

        // 毎フレーム時に実行されるループイベントです
        function tick() {
          mesh.rotation.x += 0.02;
          mesh.rotation.y += 0.01;

          //skyMesh.rotation.y -= 0.001;
          camera.rotation.x += 0.01;
          camera.rotation.y += 0.02;

          // レンダリング
          renderer.render(scene, camera);
          requestAnimationFrame(tick);
        }
}

      /** メッシュを継承したドーナツクラスです。 */
      class Donuts extends THREE.Mesh {
        /** コンストラクターです。 */
        constructor() {
          // ジオメトリを作成
          const geometry = new THREE.TorusGeometry(120, 40, 60, 50,Math.PI * 1.99);

          // マテリアルを作成
          const material = new THREE.MeshNormalMaterial();

          // 継承元のコンストラクターを実行
          super(geometry, material);
        }
      }

