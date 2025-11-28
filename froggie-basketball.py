# basketball_game.html
<!DOCTYPE html>
<html>
<head>
    <title>Basketball Game - Play in Browser</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #1a1a2e, #16213e);
            font-family: 'Arial', sans-serif;
            color: white;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }
        
        .container {
            text-align: center;
            max-width: 1000px;
        }
        
        .game-title {
            font-size: 3em;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
        
        .subtitle {
            font-size: 1.2em;
            color: #ccc;
            margin-bottom: 20px;
        }
        
        canvas {
            border: 3px solid #333;
            border-radius: 10px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.6);
            background: #2a2a2a;
            margin-bottom: 20px;
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
            color: #4ecdc4;
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
        
        .status {
            margin-top: 15px;
            padding: 15px;
            background: rgba(255, 193, 7, 0.1);
            border-radius: 8px;
            border-left: 4px solid #ffc107;
            font-size: 1.1em;
        }
        
        .download-btn {
            margin-top: 20px;
            padding: 12px 24px;
            background: linear-gradient(45deg, #4ecdc4, #44a08d);
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 1.1em;
            cursor: pointer;
            transition: transform 0.2s;
        }
        
        .download-btn:hover {
            transform: translateY(-2px);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="game-title">🏀 Basketball Game</h1>
        <div class="subtitle">Play directly in your browser - No installation required!</div>
        
        <div class="controls">
            <div class="control-group">
                <h3>🎮 Controls</h3>
                <div class="key">W</div><div class="key">A</div><div class="key">S</div><div class="key">D</div>
                <span style="color: #ccc;">Move Player</span>
            </div>
            <div class="control-group">
                <div class="key">SPACE</div>
                <span style="color: #ccc;">Shoot Ball</span>
            </div>
            <div class="control-group">
                <div class="key">D</div>
                <span style="color: #ccc;">Dribble</span>
            </div>
            <div class="control-group">
                <div class="key">P</div>
                <span style="color: #ccc;">Pause</span>
            </div>
            <div class="control-group">
                <div class="key">R</div>
                <span style="color: #ccc;">Reset Game</span>
            </div>
        </div>
        
        <canvas id="gameCanvas" width="800" height="600"></canvas>
        
        <button class="download-btn" onclick="downloadGame()">
            💾 Download Game as HTML
        </button>
        
        <div class="status" id="status">
            🎮 Game loading... Use WASD to move and SPACE to shoot!
        </div>
    </div>

    <script>
        // Basketball Game JavaScript Implementation
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const statusDiv = document.getElementById('status');

        // Game Constants
        const SCREEN_WIDTH = 800;
        const SCREEN_HEIGHT = 600;
        const FPS = 60;

        // Colors
        const COLORS = {
            WHITE: '#FFFFFF',
            COURT_BROWN: '#8B4513',
            COURT_LINE: '#FFFFFF',
            RED: '#DC143C',
            BLUE: '#1E90FF',
            BLACK: '#000000',
            ORANGE: '#FF8C00',
            YELLOW: '#FFFF00',
            GREEN: '#008000'
        };

        class Vector2 {
            constructor(x = 0, y = 0) {
                this.x = x;
                this.y = y;
            }
            
            length() {
                return Math.sqrt(this.x * this.x + this.y * this.y);
            }
            
            distance(other) {
                return Math.sqrt((this.x - other.x) ** 2 + (this.y - other.y) ** 2);
            }
            
            normalize() {
                const length = this.length();
                if (length > 0) {
                    this.x /= length;
                    this.y /= length;
                }
            }
            
            add(other) {
                return new Vector2(this.x + other.x, this.y + other.y);
            }
            
            subtract(other) {
                return new Vector2(this.x - other.x, this.y - other.y);
            }
            
            multiply(scalar) {
                return new Vector2(this.x * scalar, this.y * scalar);
            }
        }

        class Basketball {
            constructor() {
                this.position = new Vector2(SCREEN_WIDTH / 2, 100);
                this.velocity = new Vector2(0, 0);
                this.acceleration = new Vector2(0, 0.5);
                this.radius = 12;
                this.inPlay = false;
                this.lastTouchedBy = -1;
                this.spin = 0;
                this.trail = [];
                this.isDribbling = false;
                this.dribbleCount = 0;
            }
            
            update() {
                // Add trail
                if (this.velocity.length() > 3) {
                    this.trail.push(new Vector2(this.position.x, this.position.y));
                    if (this.trail.length > 6) {
                        this.trail.shift();
                    }
                } else {
                    this.trail = [];
                }
                
                // Apply physics
                this.velocity.x += this.acceleration.x;
                this.velocity.y += this.acceleration.y;
                this.position.x += this.velocity.x;
                this.position.y += this.velocity.y;
                
                // Apply spin
                this.velocity.x += this.spin * 0.1;
                this.spin *= 0.95;
                
                // Air resistance
                this.velocity.x *= 0.99;
                this.velocity.y *= 0.99;
                
                // Court boundaries
                if (this.position.x - this.radius < 50) {
                    this.position.x = 50 + this.radius;
                    this.velocity.x = -this.velocity.x * 0.8;
                } else if (this.position.x + this.radius > SCREEN_WIDTH - 50) {
                    this.position.x = SCREEN_WIDTH - 50 - this.radius;
                    this.velocity.x = -this.velocity.x * 0.8;
                }
                
                // Floor collision
                if (this.position.y + this.radius > SCREEN_HEIGHT - 50) {
                    this.position.y = SCREEN_HEIGHT - 50 - this.radius;
                    this.velocity.y = -this.velocity.y * 0.7;
                    this.dribbleCount++;
                    if (this.dribbleCount > 3) {
                        this.isDribbling = false;
                        this.dribbleCount = 0;
                    }
                }
                
                // Ceiling collision
                if (this.position.y - this.radius < 50) {
                    this.position.y = 50 + this.radius;
                    this.velocity.y = -this.velocity.y * 0.7;
                }
                
                // Stop if moving slowly
                if (this.velocity.length() < 0.3) {
                    this.velocity.x = 0;
                    this.velocity.y = 0;
                }
            }
            
            render() {
                // Render trail
                ctx.globalAlpha = 0.3;
                for (let i = 0; i < this.trail.length; i++) {
                    const pos = this.trail[i];
                    const alpha = i / this.trail.length;
                    const radius = this.radius * alpha * 0.5;
                    
                    ctx.fillStyle = COLORS.ORANGE;
                    ctx.beginPath();
                    ctx.arc(pos.x, pos.y, radius, 0, Math.PI * 2);
                    ctx.fill();
                }
                ctx.globalAlpha = 1.0;
                
                // Render basketball
                ctx.fillStyle = COLORS.ORANGE;
                ctx.beginPath();
                ctx.arc(this.position.x, this.position.y, this.radius, 0, Math.PI * 2);
                ctx.fill();
                
                // Basketball lines
                ctx.strokeStyle = COLORS.BLACK;
                ctx.lineWidth = 1;
                for (let i = 0; i < 180; i += 30) {
                    const angle = (i * Math.PI / 180) + this.velocity.x * 0.05;
                    const lineX = this.position.x + (this.radius - 2) * Math.cos(angle);
                    const lineY = this.position.y + (this.radius - 2) * Math.sin(angle);
                    
                    ctx.beginPath();
                    ctx.arc(lineX, lineY, 2, 0, Math.PI * 2);
                    ctx.stroke();
                }
            }
            
            shoot(direction, power) {
                const length = direction.length();
                if (length > 0) {
                    direction.x /= length;
                    direction.y /= length;
                }
                this.velocity = direction.multiply(power * 10);
                this.inPlay = true;
                this.isDribbling = false;
            }
            
            dribble(playerPos) {
                this.position = new Vector2(playerPos.x, playerPos.y - 40);
                this.velocity = new Vector2(0, 8);
                this.isDribbling = true;
                this.dribbleCount = 0;
            }
        }

        class Hoop {
            constructor(x, y, color) {
                this.position = new Vector2(x, y);
                this.width = 100;
                this.height = 5;
                this.color = color;
                this.score = 0;
            }
            
            render() {
                // Backboard
                ctx.fillStyle = COLORS.WHITE;
                ctx.fillRect(this.position.x - 8, this.position.y - 60, 16, 80);
                
                // Rim
                ctx.fillStyle = this.color;
                ctx.fillRect(this.position.x - this.width/2, this.position.y, this.width, this.height);
                
                // Net
                ctx.strokeStyle = COLORS.WHITE;
                ctx.lineWidth = 2;
                for (let i = 0; i < 5; i++) {
                    const netY = this.position.y + 5 + i * 6;
                    ctx.beginPath();
                    ctx.moveTo(this.position.x - this.width/2 + 5, netY);
                    ctx.lineTo(this.position.x + this.width/2 - 5, netY);
                    ctx.stroke();
                }
            }
            
            checkScore(ball) {
                if (ball.position.y > this.position.y && 
                    ball.position.y < this.position.y + 40 &&
                    ball.position.x > this.position.x - this.width/2 && 
                    ball.position.x < this.position.x + this.width/2 &&
                    ball.velocity.y > 0) {
                    this.score++;
                    return true;
                }
                return false;
            }
        }

        class Player {
            constructor(x, y, color, isAI = false, name = "Player") {
                this.position = new Vector2(x, y);
                this.velocity = new Vector2(0, 0);
                this.size = new Vector2(20, 50);
                this.color = color;
                this.speed = isAI ? 2.5 : 3.5;
                this.isAI = isAI;
                this.skillLevel = isAI ? 0.6 : 1.0;
                this.targetPosition = new Vector2(0, 0);
                this.hasBall = false;
                this.name = name;
            }
            
            update(ball, opponent, targetHoop) {
                if (this.isAI) {
                    this.updateAI(ball, opponent, targetHoop);
                }
                
                this.position.x += this.velocity.x;
                this.position.y += this.velocity.y;
                
                // Court boundaries
                const minX = 70;
                const maxX = SCREEN_WIDTH - 70;
                const minY = 80;
                const maxY = SCREEN_HEIGHT - 130;
                
                this.position.x = Math.max(minX, Math.min(maxX, this.position.x));
                this.position.y = Math.max(minY, Math.min(maxY, this.position.y));
                
                // Check ball possession
                if (!this.hasBall && ball.inPlay && !ball.isDribbling) {
                    const dist = this.position.distance(ball.position);
                    if (dist < this.size.x + ball.radius) {
                        this.hasBall = true;
                        ball.lastTouchedBy = this.isAI ? 1 : 0;
                    }
                }
            }
            
            updateAI(ball, opponent, targetHoop) {
                if (this.hasBall) {
                    // Decide to shoot or dribble
                    const distanceToHoop = this.position.distance(targetHoop.position);
                    const shotProbability = (1 - distanceToHoop / 400) * this.skillLevel;
                    
                    if (Math.random() < shotProbability && distanceToHoop < 300) {
                        // Shoot
                        const shootDirection = targetHoop.position.subtract(this.position);
                        shootDirection.y -= 80;
                        this.shoot(shootDirection, 0.8, ball);
                    } else {
                        // Move towards hoop
                        let moveDirection = targetHoop.position.subtract(this.position);
                        if (this.position.distance(opponent.position) < 80) {
                            moveDirection = this.position.subtract(opponent.position);
                        }
                        moveDirection.normalize();
                        this.velocity = moveDirection.multiply(this.speed * 0.7);
                        
                        // Occasionally dribble
                        if (Math.random() < 0.02) {
                            this.dribble(ball);
                        }
                    }
                } else {
                    // Defense or go for ball
                    if (ball.inPlay && !ball.isDribbling) {
                        this.targetPosition = new Vector2(ball.position.x, ball.position.y);
                    } else {
                        this.targetPosition = new Vector2(
                            (ball.position.x + targetHoop.position.x) / 2,
                            (ball.position.y + targetHoop.position.y) / 2
                        );
                    }
                    
                    const direction = this.targetPosition.subtract(this.position);
                    const distance = direction.length();
                    
                    if (distance > 15) {
                        direction.normalize();
                        this.velocity = direction.multiply(this.speed * this.skillLevel);
                    } else {
                        this.velocity = new Vector2(0, 0);
                    }
                }
            }
            
            render() {
                // Player body
                ctx.fillStyle = this.color;
                ctx.fillRect(
                    this.position.x - this.size.x/2,
                    this.position.y - this.size.y/2,
                    this.size.x,
                    this.size.y
                );
                
                // Player number
                ctx.fillStyle = COLORS.WHITE;
                const numberX = this.position.x - 2;
                const numberY = this.position.y - 4;
                
                // Simple number '1'
                for (let i = 0; i < 3; i++) {
                    ctx.fillRect(numberX, numberY + i, 1, 1);
                    ctx.fillRect(numberX + 4, numberY + i, 1, 1);
                }
                for (let i = 0; i < 4; i++) {
                    ctx.fillRect(numberX + 2, numberY + i, 1, 1);
                }
                
                // Ball indicator
                if (this.hasBall) {
                    ctx.fillStyle = COLORS.ORANGE;
                    ctx.beginPath();
                    ctx.arc(this.position.x, this.position.y - this.size.y/2 - 6, 3, 0, Math.PI * 2);
                    ctx.fill();
                }
            }
            
            shoot(direction, power, ball) {
                if (this.hasBall) {
                    ball.shoot(direction, power);
                    this.hasBall = false;
                }
            }
            
            dribble(ball) {
                if (this.hasBall) {
                    ball.dribble(this.position);
                }
            }
        }

        class BasketballGame {
            constructor() {
                this.player = new Player(SCREEN_WIDTH/4, SCREEN_HEIGHT/2, COLORS.BLUE, false, "Player");
                this.ai = new Player(3*SCREEN_WIDTH/4, SCREEN_HEIGHT/2, COLORS.RED, true, "AI");
                this.ball = new Basketball();
                this.playerHoop = new Hoop(SCREEN_WIDTH - 80, 120, COLORS.BLUE);
                this.aiHoop = new Hoop(80, 120, COLORS.RED);
                this.gameRunning = true;
                this.gameClock = 600;
                this.quarter = 1;
                this.isPaused = false;
                this.keys = {};
                
                // Start with player having ball
                this.player.hasBall = true;
                this.ball.position = new Vector2(this.player.position.x, this.player.position.y - 40);
                
                // Set up event listeners
                this.setupEventListeners();
            }
            
            setupEventListeners() {
                document.addEventListener('keydown', (e) => {
                    this.keys[e.key.toLowerCase()] = true;
                    
                    if (e.key === 'p' || e.key === 'P') {
                        this.isPaused = !this.isPaused;
                    }
                    if (e.key === 'r' || e.key === 'R') {
                        this.resetGame();
                    }
                });
                
                document.addEventListener('keyup', (e) => {
                    this.keys[e.key.toLowerCase()] = false;
                });
            }
            
            drawCourt() {
                // Court background
                ctx.fillStyle = COLORS.COURT_BROWN;
                ctx.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);
                
                // Court lines
                ctx.strokeStyle = COLORS.COURT_LINE;
                ctx.lineWidth = 2;
                ctx.strokeRect(50, 50, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100);
                
                // Center line
                ctx.beginPath();
                ctx.moveTo(SCREEN_WIDTH/2, 50);
                ctx.lineTo(SCREEN_WIDTH/2, SCREEN_HEIGHT - 50);
                ctx.stroke();
                
                // Center circle
                ctx.beginPath();
                ctx.arc(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 50, 0, Math.PI * 2);
                ctx.stroke();
                
                // Key areas
                ctx.strokeRect(50, SCREEN_HEIGHT/2 - 60, 120, 120);
                ctx.strokeRect(SCREEN_WIDTH - 170, SCREEN_HEIGHT/2 - 60, 120, 120);
            }
            
            drawUI() {
                // Scoreboard
                ctx.fillStyle = 'rgba(40, 40, 40, 0.8)';
                ctx.fillRect(SCREEN_WIDTH/2 - 120, 10, 240, 50);
                
                ctx.strokeStyle = COLORS.WHITE;
                ctx.lineWidth = 2;
                ctx.strokeRect(SCREEN_WIDTH/2 - 120, 10, 240, 50);
                
                // Scores
                ctx.fillStyle = COLORS.WHITE;
                ctx.font = '16px Arial';
                ctx.textAlign = 'center';
                ctx.fillText(`Player: ${this.playerHoop.score}`, SCREEN_WIDTH/2 - 40, 35);
                ctx.fillText(`AI: ${this.aiHoop.score}`, SCREEN_WIDTH/2 + 40, 35);
                
                // Game clock
                const minutes = Math.floor(this.gameClock / 3600);
                const seconds = Math.floor((this.gameClock % 3600) / 60);
                ctx.fillText(`Q${this.quarter} ${minutes}:${seconds.toString().padStart(2, '0')}`, SCREEN_WIDTH/2, 55);
                
                // Pause indicator
                if (this.isPaused) {
                    ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
                    ctx.fillRect(SCREEN_WIDTH/2 - 60, SCREEN_HEIGHT/2 - 30, 120, 60);
                    ctx.fillStyle = COLORS.WHITE;
                    ctx.font = '24px Arial';
                    ctx.fillText('PAUSED', SCREEN_WIDTH/2, SCREEN_HEIGHT/2);
                }
            }
            
            handleInput() {
                if (this.isPaused) return;
                
                this.player.velocity.x = 0;
                this.player.velocity.y = 0;
                
                if (this.keys['w']) this.player.velocity.y = -this.player.speed;
                if (this.keys['s']) this.player.velocity.y = this.player.speed;
                if (this.keys['a']) this.player.velocity.x = -this.player.speed;
                if (this.keys['d']) this.player.velocity.x = this.player.speed;
                
                // Normalize diagonal movement
                if (this.player.velocity.x !== 0 && this.player.velocity.y !== 0) {
                    this.player.velocity.x *= 0.7071;
                    this.player.velocity.y *= 0.7071;
                }
                
                // Shooting
                if (this.keys[' '] && this.player.hasBall) {
                    const shootDirection = this.aiHoop.position.subtract(this.player.position);
                    this.player.shoot(shootDirection, 0.8, this.ball);
                }
                
                // Dribbling
                if (this.keys['d'] && this.player.hasBall) {
                    this.player.dribble(this.ball);
                }
            }
            
            update() {
                if (this.isPaused) return;
                
                // Update game clock
                if (this.gameClock > 0) {
                    this.gameClock--;
                }
                
                this.player.update(this.ball, this.ai, this.aiHoop);
                this.ai.update(this.ball, this.player, this.playerHoop);
                this.ball.update();
                
                // Check scoring
                if (this.playerHoop.checkScore(this.ball)) {
                    this.resetAfterScore(false);
                    statusDiv.textContent = '🎉 AI scored! Ball goes to Player.';
                } else if (this.aiHoop.checkScore(this.ball)) {
                    this.resetAfterScore(true);
                    statusDiv.textContent = '🎉 Player scored! Ball goes to AI.';
                }
                
                // Reset ball if stuck
                if (!this.ball.inPlay && !this.ball.isDribbling && this.ball.velocity.length() === 0) {
                    this.resetBall();
                }
            }
            
            resetAfterScore(aiScored) {
                if (aiScored) {
                    this.player.hasBall = true;
                    this.ball.position = new Vector2(this.player.position.x, this.player.position.y - 40);
                } else {
                    this.ai.hasBall = true;
                    this.ball.position = new Vector2(this.ai.position.x, this.ai.position.y - 40);
                }
                this.ball.inPlay = false;
                this.ball.velocity = new Vector2(0, 0);
            }
            
            resetBall() {
                this._lastScorerWasAI = !this._lastScorerWasAI;
                if (this._lastScorerWasAI) {
                    this.player.hasBall = true;
                    this.ball.position = new Vector2(this.player.position.x, this.player.position.y - 40);
                } else {
                    this.ai.hasBall = true;
                    this.ball.position = new Vector2(this.ai.position.x, this.ai.position.y - 40);
                }
                this.ball.inPlay = false;
            }
            
            resetGame() {
                this.playerHoop.score = 0;
                this.aiHoop.score = 0;
                this.gameClock = 600;
                this.quarter = 1;
                this.player.hasBall = true;
                this.ai.hasBall = false;
                this.ball.position = new Vector2(this.player.position.x, this.player.position.y - 40);
                this.ball.inPlay = false;
                this.ball.velocity = new Vector2(0, 0);
                this._lastScorerWasAI = false;
                statusDiv.textContent = '🔄 Game reset! Use WASD to move and SPACE to shoot!';
            }
            
            render() {
                this.drawCourt();
                this.playerHoop.render();
                this.aiHoop.render();
                this.player.render();
                this.ai.render();
                this.ball.render();
                this.drawUI();
            }
            
            gameLoop() {
                this.handleInput();
                this.update();
                this.render();
                
                if (this.gameRunning) {
                    requestAnimationFrame(() => this.gameLoop());
                }
            }
            
            start() {
                statusDiv.textContent = '🎮 Game started! Use WASD to move and SPACE to shoot!';
                this.gameLoop();
            }
        }

        // Initialize and start the game
        const game = new BasketballGame();
        game.start();

        // Download function
        function downloadGame() {
            const htmlContent = document.documentElement.outerHTML;
            const blob = new Blob([htmlContent], { type: 'text/html' });
            const url = URL.createObjectURL(blob);
            
            const a = document.createElement('a');
            a.href = url;
            a.download = 'basketball_game.html';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
            
            statusDiv.textContent = '✅ Game downloaded! Open basketball_game.html in any browser.';
        }

        // Update status with score
        setInterval(() => {
            if (!game.isPaused) {
                statusDiv.textContent = `🏀 Player: ${game.playerHoop.score} - AI: ${game.aiHoop.score} | Use WASD+SPACE to play!`;
            }
        }, 2000);
    </script>
</body>
</html>