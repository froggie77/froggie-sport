<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Squash Game</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #1a237e, #283593);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
            color: white;
        }
        
        .game-container {
            background: #303f9f;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            border: 5px solid #1a237e;
            max-width: 900px;
            width: 100%;
        }
        
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
        
        .header h1 {
            font-size: 2.8em;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            margin-bottom: 10px;
            color: #ffd54f;
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .game-stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .stat-box {
            background: #1a237e;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            border: 2px solid #ffd54f;
        }
        
        .stat-value {
            font-size: 2.5em;
            font-weight: bold;
            color: #ffd54f;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        
        .stat-label {
            font-size: 1.1em;
            margin-top: 5px;
        }
        
        .game-area {
            position: relative;
            background: #5c6bc0;
            border: 5px solid #3949ab;
            border-radius: 10px;
            height: 500px;
            margin-bottom: 20px;
            overflow: hidden;
            box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.3);
        }
        
        /* Court markings */
        .front-wall {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 100%;
            background: linear-gradient(135deg, #7986cb, #5c6bc0);
            border-bottom: 5px solid #ffd54f;
        }
        
        .tin {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 50px;
            background: #d32f2f;
            border-top: 3px solid #b71c1c;
        }
        
        .service-line {
            position: absolute;
            top: 100px;
            left: 0;
            right: 0;
            height: 3px;
            background: #ffd54f;
        }
        
        .service-box {
            position: absolute;
            top: 100px;
            left: 25%;
            right: 25%;
            bottom: 0;
            border: 2px dashed #ffd54f;
        }
        
        .half-court-line {
            position: absolute;
            top: 100px;
            bottom: 0;
            left: 50%;
            width: 3px;
            background: #ffd54f;
            transform: translateX(-50%);
        }
        
        .out-line {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: #ff5252;
        }
        
        /* Game elements */
        .paddle {
            position: absolute;
            width: 15px;
            height: 80px;
            background: linear-gradient(45deg, #ffd54f, #ffc107);
            border-radius: 5px;
            border: 2px solid #ffb300;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.3);
            z-index: 10;
        }
        
        .ball {
            position: absolute;
            width: 20px;
            height: 20px;
            background: white;
            border-radius: 50%;
            border: 2px solid #e0e0e0;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
            z-index: 5;
        }
        
        .ball-trail {
            position: absolute;
            width: 6px;
            height: 6px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            pointer-events: none;
        }
        
        .controls {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .control-group {
            background: #1a237e;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #ffd54f;
        }
        
        .control-group h3 {
            text-align: center;
            margin-bottom: 10px;
            font-size: 1.3em;
            color: #ffd54f;
        }
        
        .keys {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            justify-items: center;
        }
        
        .key {
            width: 60px;
            height: 60px;
            background: #3949ab;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            font-weight: bold;
            font-size: 1.2em;
            border: 2px solid #5c6bc0;
            box-shadow: 0 4px 0 #283593;
            transition: all 0.1s;
        }
        
        .key.active {
            background: #ffd54f;
            color: #1a237e;
            transform: translateY(2px);
            box-shadow: 0 2px 0 #283593;
        }
        
        .game-info {
            background: #1a237e;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            border: 2px solid #ffd54f;
        }
        
        .controls-info {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 15px;
        }
        
        .control-instruction {
            background: #283593;
            padding: 10px;
            border-radius: 8px;
            font-size: 0.9em;
        }
        
        .buttons {
            display: flex;
            gap: 15px;
            justify-content: center;
        }
        
        .btn {
            background: #ffd54f;
            color: #1a237e;
            border: none;
            padding: 12px 25px;
            border-radius: 8px;
            font-size: 1.1em;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.2s;
            box-shadow: 0 4px 0 #ffb300;
        }
        
        .btn:hover {
            background: #ffecb3;
            transform: translateY(-2px);
        }
        
        .btn:active {
            transform: translateY(2px);
            box-shadow: 0 2px 0 #ffb300;
        }
        
        .btn-reset {
            background: #4caf50;
            box-shadow: 0 4px 0 #388e3c;
        }
        
        .btn-reset:hover {
            background: #81c784;
        }
        
        .message {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0, 0, 0, 0.9);
            color: white;
            padding: 30px 50px;
            border-radius: 15px;
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
            z-index: 100;
            display: none;
            border: 3px solid #ffd54f;
        }
        
        .particle {
            position: absolute;
            width: 8px;
            height: 8px;
            background: #ffd54f;
            border-radius: 50%;
            pointer-events: none;
            z-index: 20;
        }
        
        .score-popup {
            position: absolute;
            color: #ffd54f;
            font-size: 1.5em;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            pointer-events: none;
            z-index: 15;
            animation: floatUp 1s ease-out forwards;
        }
        
        @keyframes floatUp {
            0% {
                opacity: 1;
                transform: translateY(0);
            }
            100% {
                opacity: 0;
                transform: translateY(-50px);
            }
        }
        
        .power-bar {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            width: 200px;
            height: 15px;
            background: #1a237e;
            border: 2px solid #ffd54f;
            border-radius: 10px;
            overflow: hidden;
            z-index: 10;
        }
        
        .power-fill {
            height: 100%;
            background: linear-gradient(90deg, #4caf50, #ffd54f, #f44336);
            width: 0%;
            transition: width 0.1s;
        }
        
        .difficulty-selector {
            display: flex;
            gap: 10px;
            justify-content: center;
            margin-top: 10px;
        }
        
        .difficulty-btn {
            padding: 8px 15px;
            background: #3949ab;
            color: white;
            border: 2px solid #ffd54f;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .difficulty-btn.active {
            background: #ffd54f;
            color: #1a237e;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <div class="header">
            <h1>🎾 Squash Game 🎾</h1>
            <p>Hit the ball against the front wall and keep the rally going!</p>
        </div>
        
        <div class="game-stats">
            <div class="stat-box">
                <div class="stat-value" id="score">0</div>
                <div class="stat-label">Score</div>
            </div>
            <div class="stat-box">
                <div class="stat-value" id="lives">3</div>
                <div class="stat-label">Lives</div>
            </div>
            <div class="stat-box">
                <div class="stat-value" id="highScore">0</div>
                <div class="stat-label">High Score</div>
            </div>
        </div>
        
        <div class="game-area" id="gameArea">
            <!-- Court Markings -->
            <div class="front-wall"></div>
            <div class="tin"></div>
            <div class="service-line"></div>
            <div class="service-box"></div>
            <div class="half-court-line"></div>
            <div class="out-line"></div>
            
            <!-- Game Elements -->
            <div class="paddle" id="paddle"></div>
            <div class="ball" id="ball"></div>
            <div class="power-bar">
                <div class="power-fill" id="powerFill"></div>
            </div>
            
            <!-- Messages -->
            <div class="message" id="message">Game Over!</div>
        </div>
        
        <div class="controls">
            <div class="control-group">
                <h3>Movement Controls</h3>
                <div class="keys">
                    <div class="key" id="keyW">W</div>
                    <div class="key" id="keyA">A</div>
                    <div class="key" id="keyS">S</div>
                    <div class="key" id="keyD">D</div>
                </div>
            </div>
            
            <div class="control-group">
                <h3>Action Controls</h3>
                <div class="keys">
                    <div class="key" id="keySpace">SPACE</div>
                    <div class="key" id="keyShift">SHIFT</div>
                    <div class="key" id="keyEnter">ENTER</div>
                </div>
            </div>
        </div>
        
        <div class="game-info">
            <div class="controls-info">
                <div class="control-instruction">
                    <strong>WASD</strong> - Move paddle<br>
                    <strong>SPACE</strong> - Normal shot
                </div>
                <div class="control-instruction">
                    <strong>SHIFT</strong> - Power shot (hold)<br>
                    <strong>ENTER</strong> - Start game
                </div>
            </div>
            
            <div class="difficulty-selector">
                <div class="difficulty-btn active" data-difficulty="easy">Easy</div>
                <div class="difficulty-btn" data-difficulty="medium">Medium</div>
                <div class="difficulty-btn" data-difficulty="hard">Hard</div>
            </div>
            
            <div class="buttons">
                <button class="btn" id="startBtn">Start Game</button>
                <button class="btn btn-reset" id="resetBtn">Reset</button>
            </div>
        </div>
    </div>

    <script>
        // Game elements
        const gameArea = document.getElementById('gameArea');
        const paddle = document.getElementById('paddle');
        const ball = document.getElementById('ball');
        const scoreElement = document.getElementById('score');
        const livesElement = document.getElementById('lives');
        const highScoreElement = document.getElementById('highScore');
        const messageElement = document.getElementById('message');
        const powerFill = document.getElementById('powerFill');
        const startBtn = document.getElementById('startBtn');
        const resetBtn = document.getElementById('resetBtn');
        
        // Key elements
        const keys = {
            w: document.getElementById('keyW'),
            a: document.getElementById('keyA'),
            s: document.getElementById('keyS'),
            d: document.getElementById('keyD'),
            space: document.getElementById('keySpace'),
            shift: document.getElementById('keyShift'),
            enter: document.getElementById('keyEnter')
        };
        
        // Game state
        let gameState = {
            score: 0,
            lives: 3,
            highScore: localStorage.getItem('squashHighScore') || 0,
            gameActive: false,
            ballInPlay: false,
            difficulty: 'easy',
            keys: {
                w: false, a: false, s: false, d: false,
                space: false, shift: false
            },
            powerCharge: 0,
            isCharging: false,
            rallyCount: 0
        };
        
        // Game objects
        const gameObjects = {
            paddle: {
                x: 400,
                y: 400,
                width: 15,
                height: 80,
                speed: 6
            },
            ball: {
                x: 400,
                y: 200,
                vx: 0,
                vy: 0,
                radius: 10,
                speed: 8,
                maxSpeed: 15
            },
            court: {
                width: 800,
                height: 500,
                frontWall: 0,
                backWall: 800,
                floor: 500,
                ceiling: 0,
                tin: 450, // Height where tin starts
                serviceLine: 100
            }
        };
        
        // Initialize game
        function initGame() {
            updateHighScore();
            resetGame();
            setupEventListeners();
            gameLoop();
        }
        
        // Reset game
        function resetGame() {
            gameState.score = 0;
            gameState.lives = 3;
            gameState.rallyCount = 0;
            resetBall();
            resetPaddle();
            updateDisplay();
        }
        
        // Reset ball to starting position
        function resetBall() {
            gameObjects.ball.x = 400;
            gameObjects.ball.y = 200;
            gameObjects.ball.vx = (Math.random() - 0.5) * 5;
            gameObjects.ball.vy = 5;
            gameState.ballInPlay = true;
        }
        
        // Reset paddle position
        function resetPaddle() {
            gameObjects.paddle.x = 400;
            gameObjects.paddle.y = 400;
        }
        
        // Update high score display
        function updateHighScore() {
            highScoreElement.textContent = gameState.highScore;
        }
        
        // Update game display
        function updateDisplay() {
            scoreElement.textContent = gameState.score;
            livesElement.textContent = gameState.lives;
            
            // Update paddle position
            paddle.style.left = (gameObjects.paddle.x - gameObjects.paddle.width / 2) + 'px';
            paddle.style.top = (gameObjects.paddle.y - gameObjects.paddle.height / 2) + 'px';
            
            // Update ball position
            ball.style.left = (gameObjects.ball.x - gameObjects.ball.radius) + 'px';
            ball.style.top = (gameObjects.ball.y - gameObjects.ball.radius) + 'px';
            
            // Update power bar
            powerFill.style.width = gameState.powerCharge + '%';
        }
        
        // Handle game logic
        function updateGame() {
            if (!gameState.gameActive) return;
            
            // Move paddle based on keys
            movePaddle();
            
            // Update ball physics
            if (gameState.ballInPlay) {
                updateBall();
            }
            
            // Update power charge
            updatePowerCharge();
            
            // Update display
            updateDisplay();
        }
        
        // Move paddle based on keyboard input
        function movePaddle() {
            if (gameState.keys.w && gameObjects.paddle.y > 100) {
                gameObjects.paddle.y -= gameObjects.paddle.speed;
            }
            if (gameState.keys.s && gameObjects.paddle.y < 450) {
                gameObjects.paddle.y += gameObjects.paddle.speed;
            }
            if (gameState.keys.a && gameObjects.paddle.x > 50) {
                gameObjects.paddle.x -= gameObjects.paddle.speed;
            }
            if (gameState.keys.d && gameObjects.paddle.x < 750) {
                gameObjects.paddle.x += gameObjects.paddle.speed;
            }
        }
        
        // Update ball physics
        function updateBall() {
            // Move ball
            gameObjects.ball.x += gameObjects.ball.vx;
            gameObjects.ball.y += gameObjects.ball.vy;
            
            // Ball collisions with walls
            if (gameObjects.ball.x <= gameObjects.ball.radius || 
                gameObjects.ball.x >= gameObjects.court.width - gameObjects.ball.radius) {
                gameObjects.ball.vx = -gameObjects.ball.vx;
                createParticles(gameObjects.ball.x, gameObjects.ball.y, 5);
            }
            
            // Ball collision with front wall (ceiling)
            if (gameObjects.ball.y <= gameObjects.ball.radius) {
                gameObjects.ball.vy = -gameObjects.ball.vy;
                createParticles(gameObjects.ball.x, gameObjects.ball.y, 8);
                gameState.rallyCount++;
                addScore(10);
            }
            
            // Ball collision with paddle
            if (checkPaddleCollision()) {
                handlePaddleHit();
            }
            
            // Ball out of bounds (floor or tin)
            if (gameObjects.ball.y >= gameObjects.court.tin) {
                handleBallLoss();
            }
            
            // Add some randomness to ball movement
            if (Math.random() < 0.02) {
                gameObjects.ball.vx += (Math.random() - 0.5) * 0.5;
            }
        }
        
        // Check if ball collides with paddle
        function checkPaddleCollision() {
            const ball = gameObjects.ball;
            const paddle = gameObjects.paddle;
            
            return ball.x + ball.radius > paddle.x - paddle.width / 2 &&
                   ball.x - ball.radius < paddle.x + paddle.width / 2 &&
                   ball.y + ball.radius > paddle.y - paddle.height / 2 &&
                   ball.y - ball.radius < paddle.y + paddle.height / 2;
        }
        
        // Handle ball hitting paddle
        function handlePaddleHit() {
            const ball = gameObjects.ball;
            const paddle = gameObjects.paddle;
            
            // Calculate hit angle based on where ball hit paddle
            const hitPos = (ball.x - (paddle.x - paddle.width / 2)) / paddle.width;
            const angle = (hitPos - 0.5) * Math.PI * 0.75; // -67.5 to 67.5 degrees
            
            // Calculate new velocity
            let speed = gameObjects.ball.speed;
            if (gameState.isCharging && gameState.powerCharge >= 50) {
                speed *= 1.5 + (gameState.powerCharge / 100);
                createParticles(ball.x, ball.y, 15);
                showScorePopup('POWER SHOT!', ball.x, ball.y);
            }
            
            ball.vx = Math.sin(angle) * speed;
            ball.vy = -Math.cos(angle) * speed;
            
            // Limit maximum speed
            const currentSpeed = Math.sqrt(ball.vx * ball.vx + ball.vy * ball.vy);
            if (currentSpeed > gameObjects.ball.maxSpeed) {
                ball.vx = (ball.vx / currentSpeed) * gameObjects.ball.maxSpeed;
                ball.vy = (ball.vy / currentSpeed) * gameObjects.ball.maxSpeed;
            }
            
            // Add score
            addScore(5);
            gameState.rallyCount++;
            
            // Reset power charge
            gameState.powerCharge = 0;
            gameState.isCharging = false;
            
            createParticles(ball.x, ball.y, 10);
        }
        
        // Handle ball going out of play
        function handleBallLoss() {
            gameState.lives--;
            createParticles(gameObjects.ball.x, gameObjects.ball.y, 20);
            
            if (gameState.lives <= 0) {
                gameOver();
            } else {
                setTimeout(() => {
                    resetBall();
                    resetPaddle();
                }, 1000);
            }
        }
        
        // Update power charge for power shots
        function updatePowerCharge() {
            if (gameState.keys.shift && !gameState.isCharging) {
                gameState.isCharging = true;
            }
            
            if (gameState.isCharging && gameState.powerCharge < 100) {
                gameState.powerCharge += 2;
            }
        }
        
        // Add score and update high score
        function addScore(points) {
            gameState.score += points;
            if (gameState.score > gameState.highScore) {
                gameState.highScore = gameState.score;
                localStorage.setItem('squashHighScore', gameState.highScore);
                updateHighScore();
            }
            
            // Show rally bonus
            if (gameState.rallyCount >= 5) {
                const bonus = Math.floor(gameState.rallyCount / 5) * 10;
                showScorePopup(`Rally x${gameState.rallyCount}! +${bonus}`, gameObjects.ball.x, gameObjects.ball.y);
                gameState.score += bonus;
            }
        }
        
        // Show floating score popup
        function showScorePopup(text, x, y) {
            const popup = document.createElement('div');
            popup.className = 'score-popup';
            popup.textContent = text;
            popup.style.left = x + 'px';
            popup.style.top = y + 'px';
            gameArea.appendChild(popup);
            
            setTimeout(() => {
                popup.remove();
            }, 1000);
        }
        
        // Create particle effects
        function createParticles(x, y, count) {
            for (let i = 0; i < count; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = x + 'px';
                particle.style.top = y + 'px';
                particle.style.background = i % 2 === 0 ? '#ffd54f' : '#4fc3f7';
                
                const angle = Math.random() * Math.PI * 2;
                const speed = 2 + Math.random() * 4;
                const vx = Math.cos(angle) * speed;
                const vy = Math.sin(angle) * speed;
                
                gameArea.appendChild(particle);
                
                // Animate particle
                let opacity = 1;
                const animate = () => {
                    opacity -= 0.02;
                    if (opacity <= 0) {
                        particle.remove();
                        return;
                    }
                    
                    particle.style.opacity = opacity;
                    particle.style.left = (parseFloat(particle.style.left) + vx) + 'px';
                    particle.style.top = (parseFloat(particle.style.top) + vy) + 'px';
                    
                    requestAnimationFrame(animate);
                };
                
                animate();
            }
        }
        
        // Game over
        function gameOver() {
            gameState.gameActive = false;
            messageElement.textContent = `Game Over!\\nFinal Score: ${gameState.score}`;
            messageElement.style.display = 'block';
        }
        
        // Start game
        function startGame() {
            gameState.gameActive = true;
            gameState.ballInPlay = true;
            messageElement.style.display = 'none';
            resetGame();
        }
        
        // Game loop
        function gameLoop() {
            updateGame();
            requestAnimationFrame(gameLoop);
        }
        
        // Event listeners
        function setupEventListeners() {
            // Keyboard events
            document.addEventListener('keydown', (e) => {
                switch(e.key.toLowerCase()) {
                    case 'w': gameState.keys.w = true; keys.w.classList.add('active'); break;
                    case 'a': gameState.keys.a = true; keys.a.classList.add('active'); break;
                    case 's': gameState.keys.s = true; keys.s.classList.add('active'); break;
                    case 'd': gameState.keys.d = true; keys.d.classList.add('active'); break;
                    case ' ': gameState.keys.space = true; keys.space.classList.add('active'); e.preventDefault(); break;
                    case 'shift': gameState.keys.shift = true; keys.shift.classList.add('active'); break;
                    case 'enter': startGame(); keys.enter.classList.add('active'); break;
                }
            });
            
            document.addEventListener('keyup', (e) => {
                switch(e.key.toLowerCase()) {
                    case 'w': gameState.keys.w = false; keys.w.classList.remove('active'); break;
                    case 'a': gameState.keys.a = false; keys.a.classList.remove('active'); break;
                    case 's': gameState.keys.s = false; keys.s.classList.remove('active'); break;
                    case 'd': gameState.keys.d = false; keys.d.classList.remove('active'); break;
                    case ' ': gameState.keys.space = false; keys.space.classList.remove('active'); break;
                    case 'shift': gameState.keys.shift = false; keys.shift.classList.remove('active'); break;
                    case 'enter': keys.enter.classList.remove('active'); break;
                }
            });
            
            // Button events
            startBtn.addEventListener('click', startGame);
            resetBtn.addEventListener('click', resetGame);
            
            // Difficulty selector
            document.querySelectorAll('.difficulty-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    document.querySelectorAll('.difficulty-btn').forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    gameState.difficulty = btn.dataset.difficulty;
                    
                    // Adjust game speed based on difficulty
                    switch(gameState.difficulty) {
                        case 'easy':
                            gameObjects.ball.speed = 6;
                            gameObjects.ball.maxSpeed = 12;
                            break;
                        case 'medium':
                            gameObjects.ball.speed = 8;
                            gameObjects.ball.maxSpeed = 15;
                            break;
                        case 'hard':
                            gameObjects.ball.speed = 10;
                            gameObjects.ball.maxSpeed = 18;
                            break;
                    }
                });
            });
            
            // Prevent space bar from scrolling page
            window.addEventListener('keydown', (e) => {
                if(e.key === ' ' && e.target === document.body) {
                    e.preventDefault();
                }
            });
        }
        
        // Initialize the game
        initGame();
    </script>
</body>
</html>