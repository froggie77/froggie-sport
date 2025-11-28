<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tennis Accuracy Challenge</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a2a3a, #0d1b2a);
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }

        .container {
            max-width: 1000px;
            width: 100%;
            text-align: center;
        }

        .header {
            margin-bottom: 30px;
        }

        .game-title {
            font-size: 3.5em;
            background: linear-gradient(45deg, #4CAF50, #45a049);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
            font-weight: bold;
        }

        .subtitle {
            font-size: 1.3em;
            color: #ccc;
            margin-bottom: 20px;
        }

        .game-area {
            display: flex;
            gap: 30px;
            margin-bottom: 30px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .canvas-container {
            flex: 1;
            min-width: 600px;
            position: relative;
        }

        #gameCanvas {
            border: 4px solid #2a3a4a;
            border-radius: 15px;
            box-shadow: 0 12px 40px rgba(0,0,0,0.5);
            background: linear-gradient(160deg, #87CEEB, #98FB98);
            cursor: crosshair;
        }

        .stats-panel {
            flex: 0 0 300px;
            background: rgba(42, 58, 74, 0.9);
            padding: 25px;
            border-radius: 15px;
            border: 2px solid #3a4a5a;
            text-align: left;
        }

        .panel-title {
            font-size: 1.8em;
            color: #4CAF50;
            margin-bottom: 20px;
            text-align: center;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 10px;
        }

        .stat-item {
            margin-bottom: 15px;
            padding: 10px;
            background: rgba(30, 42, 56, 0.6);
            border-radius: 8px;
            border-left: 4px solid #4CAF50;
        }

        .stat-value {
            font-size: 2em;
            font-weight: bold;
            color: #4CAF50;
        }

        .stat-label {
            font-size: 1em;
            color: #b0b0b0;
        }

        .targets-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin: 20px 0;
        }

        .target-cell {
            background: rgba(30, 42, 56, 0.6);
            padding: 15px;
            border-radius: 8px;
            text-align: center;
        }

        .controls {
            background: rgba(42, 58, 74, 0.8);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            max-width: 600px;
        }

        .control-group {
            margin-bottom: 15px;
        }

        h3 {
            color: #4CAF50;
            margin-bottom: 10px;
        }

        .key {
            display: inline-block;
            background: #2a3a4a;
            padding: 8px 12px;
            margin: 4px;
            border-radius: 6px;
            border: 2px solid #3a4a5a;
            font-family: monospace;
            font-weight: bold;
            min-width: 40px;
            text-align: center;
        }

        .accuracy-meter {
            width: 100%;
            height: 20px;
            background: #2a3a4a;
            border-radius: 10px;
            margin: 10px 0;
            overflow: hidden;
        }

        .accuracy-fill {
            height: 100%;
            background: linear-gradient(90deg, #ff4444, #ffaa00, #4CAF50);
            border-radius: 10px;
            transition: width 0.5s ease;
        }

        .action-buttons {
            display: flex;
            gap: 15px;
            justify-content: center;
            margin: 20px 0;
            flex-wrap: wrap;
        }

        .btn {
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            font-size: 1.1em;
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
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }

        .status {
            margin-top: 20px;
            padding: 15px;
            background: rgba(255, 193, 7, 0.1);
            border-radius: 8px;
            border-left: 4px solid #ffc107;
            font-size: 1.1em;
        }

        .shot-history {
            max-height: 150px;
            overflow-y: auto;
            margin-top: 15px;
        }

        .shot-item {
            padding: 5px;
            margin: 2px 0;
            background: rgba(255,255,255,0.1);
            border-radius: 4px;
            font-size: 0.9em;
        }

        @media (max-width: 1000px) {
            .game-area {
                flex-direction: column;
            }
            
            .canvas-container {
                min-width: auto;
            }
            
            .stats-panel {
                flex: none;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 class="game-title">🎾 Tennis Accuracy Challenge</h1>
            <div class="subtitle">Test your precision! Hit the targets and improve your tennis accuracy</div>
        </div>

        <div class="game-area">
            <div class="canvas-container">
                <canvas id="gameCanvas" width="800" height="600"></canvas>
            </div>
            
            <div class="stats-panel">
                <h2 class="panel-title">Accuracy Stats</h2>
                
                <div class="targets-grid">
                    <div class="target-cell">
                        <div class="stat-value" id="score">0</div>
                        <div class="stat-label">Total Score</div>
                    </div>
                    <div class="target-cell">
                        <div class="stat-value" id="shots">0</div>
                        <div class="stat-label">Shots Taken</div>
                    </div>
                    <div class="target-cell">
                        <div class="stat-value" id="accuracy">0%</div>
                        <div class="stat-label">Accuracy</div>
                    </div>
                    <div class="target-cell">
                        <div class="stat-value" id="streak">0</div>
                        <div class="stat-label">Hit Streak</div>
                    </div>
                </div>

                <div class="stat-item">
                    <div class="stat-label">Overall Accuracy</div>
                    <div class="accuracy-meter">
                        <div class="accuracy-fill" id="accuracyBar" style="width: 0%"></div>
                    </div>
                </div>

                <div class="stat-item">
                    <div class="stat-label">Recent Shots</div>
                    <div class="shot-history" id="shotHistory">
                        <!-- Shot history will appear here -->
                    </div>
                </div>

                <div class="controls">
                    <h3>🎮 How to Play</h3>
                    <p>Click on the tennis court to aim and shoot at targets</p>
                    <p>Different targets have different point values!</p>
                </div>
            </div>
        </div>

        <div class="action-buttons">
            <button class="btn btn-download" onclick="downloadGame()">
                💾 Download Game as HTML
            </button>
            <button class="btn btn-restart" onclick="restartGame()">
                🔄 Restart Game
            </button>
        </div>

        <div class="status" id="status">
            🎯 Click anywhere on the court to take your first shot!
        </div>
    </div>

    <script>
        // Tennis Accuracy Game
        class TennisAccuracyGame {
            constructor() {
                this.canvas = document.getElementById('gameCanvas');
                this.ctx = this.canvas.getContext('2d');
                this.score = 0;
                this.shotsTaken = 0;
                this.shotsHit = 0;
                this.currentStreak = 0;
                this.bestStreak = 0;
                this.targets = [];
                this.balls = [];
                this.power = 0;
                this.isCharging = false;
                this.chargeStartTime = 0;
                
                this.setupEventListeners();
                this.generateTargets();
                this.gameLoop();
            }

            setupEventListeners() {
                this.canvas.addEventListener('mousedown', (e) => this.startCharge(e));
                this.canvas.addEventListener('mouseup', (e) => this.shootBall(e));
                this.canvas.addEventListener('mousemove', (e) => this.updateAim(e));
            }

            generateTargets() {
                this.targets = [];
                // Generate different types of targets
                const targetTypes = [
                    { points: 10, color: '#4CAF50', radius: 25 },  // Easy - green
                    { points: 25, color: '#2196F3', radius: 20 },  // Medium - blue
                    { points: 50, color: '#FF9800', radius: 15 },  // Hard - orange
                    { points: 100, color: '#F44336', radius: 10 }  // Expert - red
                ];

                for (let i = 0; i < 8; i++) {
                    const type = targetTypes[i % targetTypes.length];
                    this.targets.push({
                        x: 150 + (i % 4) * 150,
                        y: 150 + Math.floor(i / 4) * 200,
                        radius: type.radius,
                        color: type.color,
                        points: type.points,
                        hit: false
                    });
                }
            }

            startCharge(e) {
                this.isCharging = true;
                this.chargeStartTime = Date.now();
                this.aimPos = this.getMousePos(e);
            }

            updateAim(e) {
                if (this.isCharging) {
                    this.aimPos = this.getMousePos(e);
                }
            }

            shootBall(e) {
                if (!this.isCharging) return;

                const mousePos = this.getMousePos(e);
                const chargeTime = Date.now() - this.chargeStartTime;
                this.power = Math.min(chargeTime / 1000, 1.0);

                // Create ball
                this.balls.push({
                    x: 100, // Start from left side (player position)
                    y: this.canvas.height - 100,
                    startX: 100,
                    startY: this.canvas.height - 100,
                    targetX: mousePos.x,
                    targetY: mousePos.y,
                    radius: 8,
                    progress: 0,
                    speed: 0.02 + this.power * 0.03,
                    color: this.getBallColor(this.power)
                });

                this.shotsTaken++;
                this.isCharging = false;
                this.updateStats();
            }

            getBallColor(power) {
                if (power < 0.3) return '#4CAF50'; // Green - weak
                if (power < 0.7) return '#2196F3'; // Blue - medium
                return '#FF5722'; // Red - powerful
            }

            getMousePos(e) {
                const rect = this.canvas.getBoundingClientRect();
                return {
                    x: e.clientX - rect.left,
                    y: e.clientY - rect.top
                };
            }

            updateGame() {
                // Update balls
                for (let i = this.balls.length - 1; i >= 0; i--) {
                    const ball = this.balls[i];
                    ball.progress += ball.speed;
                    
                    // Calculate parabolic trajectory
                    const t = ball.progress;
                    ball.x = ball.startX + (ball.targetX - ball.startX) * t;
                    ball.y = ball.startY + (ball.targetY - ball.startY) * t - 
                             (t * (1 - t)) * 300; // Parabolic arc

                    // Check for target hits
                    let hitTarget = false;
                    for (let target of this.targets) {
                        if (!target.hit) {
                            const dx = ball.x - target.x;
                            const dy = ball.y - target.y;
                            const distance = Math.sqrt(dx * dx + dy * dy);
                            
                            if (distance < target.radius + ball.radius) {
                                // Hit!
                                this.score += target.points;
                                this.shotsHit++;
                                this.currentStreak++;
                                this.bestStreak = Math.max(this.bestStreak, this.currentStreak);
                                target.hit = true;
                                hitTarget = true;
                                
                                // Add hit effect
                                this.createHitEffect(target.x, target.y, target.color, target.points);
                                break;
                            }
                        }
                    }

                    // Remove ball if it goes off screen or hits something
                    if (ball.progress >= 1 || hitTarget) {
                        if (!hitTarget) {
                            this.currentStreak = 0; // Reset streak on miss
                        }
                        this.balls.splice(i, 1);
                    }
                }

                // Remove hit effects that are done
                this.hitEffects = this.hitEffects ? this.hitEffects.filter(effect => effect.progress < 1) : [];
            }

            createHitEffect(x, y, color, points) {
                if (!this.hitEffects) this.hitEffects = [];
                this.hitEffects.push({
                    x, y, color, points,
                    progress: 0,
                    speed: 0.05
                });

                // Add to shot history
                this.addShotToHistory(points, color);
            }

            addShotToHistory(points, color) {
                const history = document.getElementById('shotHistory');
                const shotItem = document.createElement('div');
                shotItem.className = 'shot-item';
                shotItem.innerHTML = `🎯 <span style="color: ${color}">+${points} points</span>`;
                history.appendChild(shotItem);
                history.scrollTop = history.scrollHeight;
            }

            updateStats() {
                document.getElementById('score').textContent = this.score;
                document.getElementById('shots').textContent = this.shotsTaken;
                
                const accuracy = this.shotsTaken > 0 ? Math.round((this.shotsHit / this.shotsTaken) * 100) : 0;
                document.getElementById('accuracy').textContent = accuracy + '%';
                document.getElementById('streak').textContent = this.currentStreak;
                
                // Update accuracy bar
                const accuracyBar = document.getElementById('accuracyBar');
                accuracyBar.style.width = accuracy + '%';
                
                // Update status message
                const status = document.getElementById('status');
                if (this.shotsTaken === 0) {
                    status.textContent = '🎯 Click anywhere on the court to take your first shot!';
                } else if (this.currentStreak >= 3) {
                    status.textContent = `🔥 Hot streak! ${this.currentStreak} hits in a row!`;
                } else if (accuracy >= 80) {
                    status.textContent = '🎾 Excellent accuracy! Keep it up!';
                } else if (accuracy >= 50) {
                    status.textContent = '👍 Good shooting! Aim for the smaller targets.';
                }
            }

            drawCourt() {
                const ctx = this.ctx;
                const width = this.canvas.width;
                const height = this.canvas.height;

                // Court background
                ctx.fillStyle = '#2E8B57'; // Forest green
                ctx.fillRect(0, 0, width, height);

                // Court outline
                ctx.strokeStyle = '#FFFFFF';
                ctx.lineWidth = 4;
                ctx.strokeRect(50, 50, width - 100, height - 100);

                // Center line
                ctx.beginPath();
                ctx.moveTo(width / 2, 50);
                ctx.lineTo(width / 2, height - 50);
                ctx.stroke();

                // Service boxes
                ctx.strokeStyle = '#FFFFFF';
                ctx.lineWidth = 2;
                ctx.strokeRect(50, height / 2 - 100, width - 100, 200);

                // Center service line
                ctx.beginPath();
                ctx.moveTo(50, height / 2);
                ctx.lineTo(width - 50, height / 2);
                ctx.stroke();

                // Net
                ctx.strokeStyle = '#8B4513';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(50, height / 2);
                ctx.lineTo(width - 50, height / 2);
                ctx.stroke();

                // Player position indicator
                ctx.fillStyle = 'rgba(30, 144, 255, 0.5)';
                ctx.beginPath();
                ctx.arc(100, height - 100, 20, 0, Math.PI * 2);
                ctx.fill();
            }

            drawTargets() {
                const ctx = this.ctx;
                
                for (let target of this.targets) {
                    if (!target.hit) {
                        // Target circle
                        ctx.fillStyle = target.color;
                        ctx.beginPath();
                        ctx.arc(target.x, target.y, target.radius, 0, Math.PI * 2);
                        ctx.fill();

                        // Target outline
                        ctx.strokeStyle = '#FFFFFF';
                        ctx.lineWidth = 2;
                        ctx.stroke();

                        // Points text
                        ctx.fillStyle = '#FFFFFF';
                        ctx.font = 'bold 14px Arial';
                        ctx.textAlign = 'center';
                        ctx.textBaseline = 'middle';
                        ctx.fillText(target.points, target.x, target.y);
                    }
                }
            }

            drawBalls() {
                const ctx = this.ctx;
                
                for (let ball of this.balls) {
                    ctx.fillStyle = ball.color;
                    ctx.beginPath();
                    ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
                    ctx.fill();

                    // Ball trail
                    ctx.strokeStyle = ball.color + '80';
                    ctx.lineWidth = 2;
                    ctx.beginPath();
                    ctx.moveTo(ball.startX, ball.startY);
                    ctx.lineTo(ball.x, ball.y);
                    ctx.stroke();
                }
            }

            drawHitEffects() {
                if (!this.hitEffects) return;
                
                const ctx = this.ctx;
                
                for (let effect of this.hitEffects) {
                    effect.progress += effect.speed;
                    const alpha = 1 - effect.progress;
                    const radius = 30 * effect.progress;
                    
                    ctx.fillStyle = effect.color + Math.floor(alpha * 255).toString(16).padStart(2, '0');
                    ctx.beginPath();
                    ctx.arc(effect.x, effect.y, radius, 0, Math.PI * 2);
                    ctx.fill();

                    // Points text
                    if (effect.progress < 0.5) {
                        ctx.fillStyle = '#FFFFFF';
                        ctx.font = 'bold 16px Arial';
                        ctx.textAlign = 'center';
                        ctx.textBaseline = 'middle';
                        ctx.fillText('+' + effect.points, effect.x, effect.y - radius - 10);
                    }
                }
            }

            drawAimIndicator() {
                if (this.isCharging && this.aimPos) {
                    const ctx = this.ctx;
                    const powerRadius = 20 + this.power * 30;
                    
                    // Power indicator
                    ctx.strokeStyle = this.getBallColor(this.power);
                    ctx.lineWidth = 3;
                    ctx.beginPath();
                    ctx.arc(this.aimPos.x, this.aimPos.y, powerRadius, 0, Math.PI * 2);
                    ctx.stroke();

                    // Aim line
                    ctx.strokeStyle = '#FFFFFF80';
                    ctx.lineWidth = 1;
                    ctx.setLineDash([5, 5]);
                    ctx.beginPath();
                    ctx.moveTo(100, this.canvas.height - 100);
                    ctx.lineTo(this.aimPos.x, this.aimPos.y);
                    ctx.stroke();
                    ctx.setLineDash([]);
                }
            }

            render() {
                this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
                this.drawCourt();
                this.drawTargets();
                this.drawBalls();
                this.drawHitEffects();
                this.drawAimIndicator();
            }

            gameLoop() {
                this.updateGame();
                this.render();
                requestAnimationFrame(() => this.gameLoop());
            }

            restart() {
                this.score = 0;
                this.shotsTaken = 0;
                this.shotsHit = 0;
                this.currentStreak = 0;
                this.balls = [];
                this.hitEffects = [];
                this.generateTargets();
                this.updateStats();
                
                const history = document.getElementById('shotHistory');
                history.innerHTML = '';
                
                document.getElementById('status').textContent = '🔄 Game restarted! Click to shoot!';
            }
        }

        // Initialize game when page loads
        let game;
        window.addEventListener('load', () => {
            game = new TennisAccuracyGame();
        });

        // Download function
        function downloadGame() {
            const htmlContent = `<!DOCTYPE html>${document.documentElement.outerHTML}`;
            const blob = new Blob([htmlContent], { type: 'text/html' });
            const url = URL.createObjectURL(blob);
            
            const a = document.createElement('a');
            a.href = url;
            a.download = 'tennis_accuracy_game.html';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
            
            document.getElementById('status').textContent = '✅ Game downloaded! Open tennis_accuracy_game.html in any browser.';
        }

        // Restart function
        function restartGame() {
            if (game) {
                game.restart();
            }
        }
    </script>
</body>
</html>