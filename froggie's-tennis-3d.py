<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Tennis Accuracy Challenge</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e, #16213e);
            color: white;
            overflow: hidden;
            min-height: 100vh;
        }

        .container {
            display: grid;
            grid-template-columns: 1fr 350px;
            height: 100vh;
        }

        #gameContainer {
            position: relative;
        }

        #gameCanvas {
            width: 100%;
            height: 100%;
            display: block;
        }

        .ui-overlay {
            position: absolute;
            top: 20px;
            left: 20px;
            z-index: 100;
        }

        .stats-panel {
            background: rgba(42, 58, 74, 0.95);
            padding: 25px;
            border-left: 3px solid #4CAF50;
            height: 100%;
            overflow-y: auto;
        }

        .panel-title {
            font-size: 2em;
            color: #4CAF50;
            margin-bottom: 25px;
            text-align: center;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 10px;
        }

        .stat-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 25px;
        }

        .stat-card {
            background: rgba(30, 42, 56, 0.6);
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            border: 1px solid #3a4a5a;
        }

        .stat-value {
            font-size: 2.5em;
            font-weight: bold;
            color: #4CAF50;
            margin-bottom: 5px;
        }

        .stat-label {
            font-size: 0.9em;
            color: #b0b0b0;
        }

        .accuracy-meter {
            width: 100%;
            height: 25px;
            background: #2a3a4a;
            border-radius: 12px;
            margin: 15px 0;
            overflow: hidden;
            border: 2px solid #3a4a5a;
        }

        .accuracy-fill {
            height: 100%;
            background: linear-gradient(90deg, #ff4444, #ffaa00, #4CAF50);
            border-radius: 10px;
            transition: width 0.5s ease;
            width: 0%;
        }

        .targets-info {
            margin: 20px 0;
        }

        .target-item {
            display: flex;
            align-items: center;
            margin: 10px 0;
            padding: 8px;
            background: rgba(255,255,255,0.1);
            border-radius: 6px;
        }

        .target-color {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            margin-right: 10px;
            border: 2px solid white;
        }

        .shot-history {
            max-height: 200px;
            overflow-y: auto;
            margin-top: 15px;
            background: rgba(30, 42, 56, 0.6);
            border-radius: 8px;
            padding: 10px;
        }

        .shot-item {
            padding: 8px;
            margin: 5px 0;
            background: rgba(255,255,255,0.1);
            border-radius: 4px;
            font-size: 0.9em;
        }

        .controls {
            margin: 25px 0;
            padding: 15px;
            background: rgba(30, 42, 56, 0.6);
            border-radius: 8px;
            border-left: 4px solid #2196F3;
        }

        .action-buttons {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }

        .btn {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 6px;
            font-size: 1em;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .btn-download {
            background: linear-gradient(45deg, #4CAF50, #45a049);
            color: white;
        }

        .btn-restart {
            background: linear-gradient(45deg, #2196F3, #1976D2);
            color: white;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }

        .status {
            margin-top: 20px;
            padding: 15px;
            background: rgba(255, 193, 7, 0.1);
            border-radius: 8px;
            border-left: 4px solid #ffc107;
            text-align: center;
        }

        .power-indicator {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0,0,0,0.7);
            padding: 10px 20px;
            border-radius: 20px;
            display: none;
        }

        .power-bar {
            width: 200px;
            height: 10px;
            background: #333;
            border-radius: 5px;
            overflow: hidden;
        }

        .power-fill {
            height: 100%;
            background: linear-gradient(90deg, #4CAF50, #FF9800, #F44336);
            border-radius: 5px;
            width: 0%;
        }

        /* Loading screen */
        #loadingScreen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #1a1a2e;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 1000;
        }

        .loader {
            width: 50px;
            height: 50px;
            border: 5px solid #333;
            border-top: 5px solid #4CAF50;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin-bottom: 20px;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div id="loadingScreen">
        <div class="loader"></div>
        <div>Loading 3D Tennis Game...</div>
    </div>

    <div class="container">
        <div id="gameContainer">
            <canvas id="gameCanvas"></canvas>
            <div class="ui-overlay">
                <div class="power-indicator" id="powerIndicator">
                    <div>POWER: <span id="powerText">0%</span></div>
                    <div class="power-bar">
                        <div class="power-fill" id="powerFill"></div>
                    </div>
                </div>
            </div>
        </div>

        <div class="stats-panel">
            <h2 class="panel-title">🎾 3D Tennis Accuracy</h2>
            
            <div class="stat-grid">
                <div class="stat-card">
                    <div class="stat-value" id="score">0</div>
                    <div class="stat-label">Total Score</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value" id="shots">0</div>
                    <div class="stat-label">Shots Taken</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value" id="accuracy">0%</div>
                    <div class="stat-label">Accuracy</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value" id="streak">0</div>
                    <div class="stat-label">Hit Streak</div>
                </div>
            </div>

            <div class="accuracy-meter">
                <div class="accuracy-fill" id="accuracyBar"></div>
            </div>

            <div class="targets-info">
                <h3>🎯 Target Values</h3>
                <div class="target-item">
                    <div class="target-color" style="background: #4CAF50"></div>
                    <div>Green: 10 points (Easy)</div>
                </div>
                <div class="target-item">
                    <div class="target-color" style="background: #2196F3"></div>
                    <div>Blue: 25 points (Medium)</div>
                </div>
                <div class="target-item">
                    <div class="target-color" style="background: #FF9800"></div>
                    <div>Orange: 50 points (Hard)</div>
                </div>
                <div class="target-item">
                    <div class="target-color" style="background: #F44336"></div>
                    <div>Red: 100 points (Expert)</div>
                </div>
            </div>

            <div class="shot-history" id="shotHistory">
                <div class="shot-item">🎯 Take your first shot!</div>
            </div>

            <div class="controls">
                <h3>🎮 Controls</h3>
                <p><strong>Click & Hold:</strong> Charge shot power</p>
                <p><strong>Release:</strong> Shoot tennis ball</p>
                <p><strong>Mouse Move:</strong> Aim</p>
                <p><strong>Scroll:</strong> Zoom in/out</p>
                <p><strong>Right Click + Drag:</strong> Rotate camera</p>
            </div>

            <div class="action-buttons">
                <button class="btn btn-download" onclick="downloadGame()">
                    💾 Download Game
                </button>
                <button class="btn btn-restart" onclick="restartGame()">
                    🔄 Restart Game
                </button>
            </div>

            <div class="status" id="status">
                Click and hold to charge your shot, then release to shoot!
            </div>
        </div>
    </div>

    <!-- Three.js Library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/controls/OrbitControls.js"></script>

    <script>
        // 3D Tennis Accuracy Game
        class Tennis3DGame {
            constructor() {
                this.score = 0;
                this.shotsTaken = 0;
                this.shotsHit = 0;
                this.currentStreak = 0;
                this.bestStreak = 0;
                this.power = 0;
                this.isCharging = false;
                this.chargeStartTime = 0;
                this.aimDirection = new THREE.Vector3();
                this.balls = [];
                this.targets = [];
                this.hitEffects = [];

                this.init();
            }

            async init() {
                // Initialize Three.js
                this.scene = new THREE.Scene();
                this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                this.renderer = new THREE.WebGLRenderer({ 
                    canvas: document.getElementById('gameCanvas'),
                    antialias: true 
                });

                this.setupRenderer();
                this.setupCamera();
                this.setupLighting();
                this.createCourt();
                this.createTargets();
                this.setupControls();
                this.setupEventListeners();
                
                // Hide loading screen
                document.getElementById('loadingScreen').style.display = 'none';

                this.animate();
            }

            setupRenderer() {
                this.renderer.setSize(window.innerWidth - 350, window.innerHeight);
                this.renderer.setClearColor(0x87CEEB);
                this.renderer.shadowMap.enabled = true;
                this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
            }

            setupCamera() {
                this.camera.position.set(0, 15, 20);
                this.camera.lookAt(0, 0, 0);
            }

            setupLighting() {
                // Ambient light
                const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
                this.scene.add(ambientLight);

                // Directional light (sun)
                const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
                directionalLight.position.set(10, 20, 5);
                directionalLight.castShadow = true;
                directionalLight.shadow.mapSize.width = 2048;
                directionalLight.shadow.mapSize.height = 2048;
                this.scene.add(directionalLight);

                // Point light for targets
                const pointLight = new THREE.PointLight(0xffffff, 0.5, 100);
                pointLight.position.set(0, 10, 0);
                this.scene.add(pointLight);
            }

            createCourt() {
                // Court surface
                const courtGeometry = new THREE.PlaneGeometry(40, 20);
                const courtMaterial = new THREE.MeshLambertMaterial({ 
                    color: 0x2E8B57,
                    roughness: 0.8
                });
                this.court = new THREE.Mesh(courtGeometry, courtMaterial);
                this.court.rotation.x = -Math.PI / 2;
                this.court.receiveShadow = true;
                this.scene.add(this.court);

                // Court lines
                this.createCourtLines();
                
                // Net
                this.createNet();

                // Player position marker
                const playerGeometry = new THREE.SphereGeometry(0.5, 16, 16);
                const playerMaterial = new THREE.MeshBasicMaterial({ color: 0x1E90FF });
                this.playerMarker = new THREE.Mesh(playerGeometry, playerMaterial);
                this.playerMarker.position.set(-15, 0.1, 0);
                this.scene.add(this.playerMarker);
            }

            createCourtLines() {
                const lineMaterial = new THREE.LineBasicMaterial({ color: 0xffffff });
                
                // Court outline
                const outlinePoints = [
                    new THREE.Vector3(-20, 0.01, -10),
                    new THREE.Vector3(20, 0.01, -10),
                    new THREE.Vector3(20, 0.01, 10),
                    new THREE.Vector3(-20, 0.01, 10),
                    new THREE.Vector3(-20, 0.01, -10)
                ];
                const outlineGeometry = new THREE.BufferGeometry().setFromPoints(outlinePoints);
                const outline = new THREE.Line(outlineGeometry, lineMaterial);
                this.scene.add(outline);

                // Center line
                const centerPoints = [
                    new THREE.Vector3(0, 0.01, -10),
                    new THREE.Vector3(0, 0.01, 10)
                ];
                const centerGeometry = new THREE.BufferGeometry().setFromPoints(centerPoints);
                const centerLine = new THREE.Line(centerGeometry, lineMaterial);
                this.scene.add(centerLine);
            }

            createNet() {
                const netGeometry = new THREE.BoxGeometry(20, 2, 0.1);
                const netMaterial = new THREE.MeshLambertMaterial({ color: 0x8B4513 });
                this.net = new THREE.Mesh(netGeometry, netMaterial);
                this.net.position.set(0, 1, 0);
                this.scene.add(this.net);
            }

            createTargets() {
                const targetTypes = [
                    { points: 10, color: 0x4CAF50, radius: 2 },   // Easy
                    { points: 25, color: 0x2196F3, radius: 1.5 }, // Medium
                    { points: 50, color: 0xFF9800, radius: 1 },   // Hard
                    { points: 100, color: 0xF44336, radius: 0.7 } // Expert
                ];

                const positions = [
                    new THREE.Vector3(-10, 2, -5),
                    new THREE.Vector3(0, 2, -5),
                    new THREE.Vector3(10, 2, -5),
                    new THREE.Vector3(-10, 2, 5),
                    new THREE.Vector3(0, 2, 5),
                    new THREE.Vector3(10, 2, 5),
                    new THREE.Vector3(-5, 4, 0),
                    new THREE.Vector3(5, 4, 0)
                ];

                positions.forEach((pos, index) => {
                    const type = targetTypes[index % targetTypes.length];
                    const geometry = new THREE.SphereGeometry(type.radius, 16, 16);
                    const material = new THREE.MeshPhongMaterial({ 
                        color: type.color,
                        emissive: type.color,
                        emissiveIntensity: 0.3,
                        transparent: true,
                        opacity: 0.9
                    });
                    
                    const target = new THREE.Mesh(geometry, material);
                    target.position.copy(pos);
                    target.userData = {
                        points: type.points,
                        color: type.color,
                        hit: false,
                        originalY: pos.y
                    };
                    
                    target.castShadow = true;
                    this.scene.add(target);
                    this.targets.push(target);
                });
            }

            setupControls() {
                this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
                this.controls.enableDamping = true;
                this.controls.dampingFactor = 0.05;
                this.controls.minDistance = 5;
                this.controls.maxDistance = 50;
            }

            setupEventListeners() {
                this.renderer.domElement.addEventListener('mousedown', (e) => this.startCharge(e));
                this.renderer.domElement.addEventListener('mouseup', (e) => this.shootBall(e));
                this.renderer.domElement.addEventListener('mousemove', (e) => this.updateAim(e));
                
                window.addEventListener('resize', () => this.onWindowResize());
            }

            startCharge(e) {
                if (e.button !== 0) return; // Only left click
                
                this.isCharging = true;
                this.chargeStartTime = Date.now();
                this.updateAim(e);
                
                // Show power indicator
                document.getElementById('powerIndicator').style.display = 'block';
            }

            updateAim(e) {
                if (!this.isCharging) return;

                const rect = this.renderer.domElement.getBoundingClientRect();
                const mouse = new THREE.Vector2(
                    ((e.clientX - rect.left) / rect.width) * 2 - 1,
                    -((e.clientY - rect.top) / rect.height) * 2 + 1
                );

                const raycaster = new THREE.Raycaster();
                raycaster.setFromCamera(mouse, this.camera);
                
                const plane = new THREE.Plane(new THREE.Vector3(0, 1, 0), 0);
                const intersection = new THREE.Vector3();
                raycaster.ray.intersectPlane(plane, intersection);
                
                this.aimDirection.subVectors(intersection, this.playerMarker.position).normalize();
                
                // Update power
                const chargeTime = Date.now() - this.chargeStartTime;
                this.power = Math.min(chargeTime / 2000, 1.0);
                
                document.getElementById('powerText').textContent = Math.round(this.power * 100) + '%';
                document.getElementById('powerFill').style.width = (this.power * 100) + '%';
            }

            shootBall(e) {
                if (!this.isCharging || e.button !== 0) return;

                const ballGeometry = new THREE.SphereGeometry(0.3, 16, 16);
                const ballMaterial = new THREE.MeshPhongMaterial({ 
                    color: this.getBallColor(this.power),
                    emissive: this.getBallColor(this.power),
                    emissiveIntensity: 0.3
                });
                
                const ball = new THREE.Mesh(ballGeometry, ballMaterial);
                ball.position.copy(this.playerMarker.position);
                ball.userData = {
                    velocity: this.aimDirection.clone().multiplyScalar(0.5 + this.power * 1.5),
                    startTime: Date.now(),
                    power: this.power
                };
                
                ball.castShadow = true;
                this.scene.add(ball);
                this.balls.push(ball);

                this.shotsTaken++;
                this.isCharging = false;
                
                // Hide power indicator
                document.getElementById('powerIndicator').style.display = 'none';
                
                this.updateStats();
            }

            getBallColor(power) {
                if (power < 0.3) return 0x4CAF50;
                if (power < 0.7) return 0x2196F3;
                return 0xFF5722;
            }

            updateGame() {
                const currentTime = Date.now();

                // Update balls
                for (let i = this.balls.length - 1; i >= 0; i--) {
                    const ball = this.balls[i];
                    const age = (currentTime - ball.userData.startTime) / 1000;
                    
                    if (age > 5) { // Remove old balls
                        this.scene.remove(ball);
                        this.balls.splice(i, 1);
                        continue;
                    }

                    // Apply physics with gravity
                    ball.userData.velocity.y -= 0.02; // Gravity
                    ball.position.add(ball.userData.velocity);

                    // Check for collisions with targets
                    let hitTarget = false;
                    for (let target of this.targets) {
                        if (!target.userData.hit) {
                            const distance = ball.position.distanceTo(target.position);
                            if (distance < target.geometry.parameters.radius + 0.3) {
                                // Hit!
                                this.score += target.userData.points;
                                this.shotsHit++;
                                this.currentStreak++;
                                this.bestStreak = Math.max(this.bestStreak, this.currentStreak);
                                target.userData.hit = true;
                                hitTarget = true;
                                
                                this.createHitEffect(target.position, target.userData.color, target.userData.points);
                                break;
                            }
                        }
                    }

                    // Remove ball if it hits something or goes out of bounds
                    if (hitTarget || ball.position.y < 0 || 
                        Math.abs(ball.position.x) > 25 || 
                        Math.abs(ball.position.z) > 15) {
                        if (!hitTarget) {
                            this.currentStreak = 0;
                        }
                        this.scene.remove(ball);
                        this.balls.splice(i, 1);
                    }
                }

                // Update hit effects
                for (let i = this.hitEffects.length - 1; i >= 0; i--) {
                    const effect = this.hitEffects[i];
                    effect.progress += 0.05;
                    
                    if (effect.progress >= 1) {
                        this.scene.remove(effect.pointsText);
                        this.hitEffects.splice(i, 1);
                    } else {
                        effect.pointsText.position.y += 0.1;
                        effect.pointsText.material.opacity = 1 - effect.progress;
                    }
                }

                // Animate targets
                this.animateTargets(currentTime);
            }

            createHitEffect(position, color, points) {
                // Create floating text
                const canvas = document.createElement('canvas');
                const context = canvas.getContext('2d');
                canvas.width = 256;
                canvas.height = 128;
                
                context.fillStyle = `#${color.toString(16).padStart(6, '0')}`;
                context.font = 'bold 48px Arial';
                context.textAlign = 'center';
                context.textBaseline = 'middle';
                context.fillText(`+${points}`, 128, 64);

                const texture = new THREE.CanvasTexture(canvas);
                const material = new THREE.SpriteMaterial({ 
                    map: texture,
                    transparent: true 
                });
                const sprite = new THREE.Sprite(material);
                sprite.position.copy(position);
                sprite.position.y += 2;
                sprite.scale.set(4, 2, 1);
                
                this.scene.add(sprite);
                
                this.hitEffects.push({
                    pointsText: sprite,
                    progress: 0
                });

                this.addShotToHistory(points, color);
            }

            addShotToHistory(points, color) {
                const history = document.getElementById('shotHistory');
                const shotItem = document.createElement('div');
                shotItem.className = 'shot-item';
                shotItem.innerHTML = `🎯 <span style="color: #${color.toString(16)}">+${points} points</span>`;
                history.appendChild(shotItem);
                history.scrollTop = history.scrollHeight;
            }

            animateTargets(time) {
                this.targets.forEach(target => {
                    if (!target.userData.hit) {
                        // Floating animation
                        target.position.y = target.userData.originalY + Math.sin(time * 0.001) * 0.5;
                        target.rotation.y = time * 0.001;
                    } else {
                        // Sink when hit
                        target.position.y -= 0.02;
                        target.material.opacity = Math.max(0, target.material.opacity - 0.02);
                    }
                });
            }

            updateStats() {
                document.getElementById('score').textContent = this.score;
                document.getElementById('shots').textContent = this.shotsTaken;
                
                const accuracy = this.shotsTaken > 0 ? Math.round((this.shotsHit / this.shotsTaken) * 100) : 0;
                document.getElementById('accuracy').textContent = accuracy + '%';
                document.getElementById('streak').textContent = this.currentStreak;
                
                document.getElementById('accuracyBar').style.width = accuracy + '%';
                
                const status = document.getElementById('status');
                if (this.shotsTaken === 0) {
                    status.textContent = 'Click and hold to charge your shot, then release to shoot!';
                } else if (this.currentStreak >= 3) {
                    status.textContent = `🔥 Hot streak! ${this.currentStreak} hits in a row!`;
                } else if (accuracy >= 80) {
                    status.textContent = '🎾 Excellent accuracy! Professional level!';
                } else if (accuracy >= 50) {
                    status.textContent = '👍 Good shooting! Aim for the smaller targets.';
                }
            }

            onWindowResize() {
                this.camera.aspect = (window.innerWidth - 350) / window.innerHeight;
                this.camera.updateProjectionMatrix();
                this.renderer.setSize(window.innerWidth - 350, window.innerHeight);
            }

            animate() {
                requestAnimationFrame(() => this.animate());
                
                this.updateGame();
                this.controls.update();
                this.renderer.render(this.scene, this.camera);
            }

            restart() {
                this.score = 0;
                this.shotsTaken = 0;
                this.shotsHit = 0;
                this.currentStreak = 0;
                this.balls = [];
                this.hitEffects = [];

                // Reset targets
                this.targets.forEach(target => {
                    target.userData.hit = false;
                    target.material.opacity = 0.9;
                    target.position.y = target.userData.originalY;
                });

                this.updateStats();
                
                const history = document.getElementById('shotHistory');
                history.innerHTML = '<div class="shot-item">🎯 Take your first shot!</div>';
                
                document.getElementById('status').textContent = 'Game restarted! Click and hold to shoot!';
            }
        }

        // Initialize game
        let game3D;
        window.addEventListener('load', () => {
            game3D = new Tennis3DGame();
        });

        // Download function
        function downloadGame() {
            const htmlContent = `<!DOCTYPE html>${document.documentElement.outerHTML}`;
            const blob = new Blob([htmlContent], { type: 'text/html' });
            const url = URL.createObjectURL(blob);
            
            const a = document.createElement('a');
            a.href = url;
            a.download = '3d_tennis_accuracy_game.html';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
            
            document.getElementById('status').textContent = '✅ Game downloaded! Open in any browser.';
        }

        // Restart function
        function restartGame() {
            if (game3D) {
                game3D.restart();
            }
        }
    </script>
</body>
</html>